from dataclasses import dataclass, field
from src.utils import get_data
from typing import Iterator, List, Optional


@dataclass
class File:
    name: str
    size: int
    parent: Optional["Directory"] = field(default=None, init=False, compare=False)


@dataclass
class Directory:
    name: str
    files: List[File] = field(default_factory=list)
    subdirectories: List["Directory"] = field(default_factory=list)
    parent_directory: Optional["Directory"] = field(
        default=None, init=False, compare=False
    )

    def add_file(self, file: File):

        if file.name in self.files:
            raise RuntimeError(
                f"File {file.name} already exists in directory {self.name}"
            )

        file.parent = self
        self.files.append(file)

    def add_subdirectory(self, subdirectory: "Directory"):

        if subdirectory.name in self.files:
            raise RuntimeError(
                f"Subdirectory {subdirectory.name} already exists in directory {self.name}"
            )

        subdirectory.parent_directory = self
        self.subdirectories.append(subdirectory)

    def try_get_subdirectory(self, subdirectory_name: str) -> Optional["Directory"]:
        for subdirectory in self.subdirectories:
            if subdirectory.name == subdirectory_name:
                return subdirectory
        return None

    def get_total_dir_size(self):
        total_file_size = sum(file.size for file in self.files)
        total_subdirectory_size = sum(
            subdirectory.get_total_dir_size() for subdirectory in self.subdirectories
        )
        return total_file_size + total_subdirectory_size

    def yield_all_subdirectories(self) -> Iterator["Directory"]:
        for subdirectory in self.subdirectories:
            yield subdirectory
            for subsubdirectory in subdirectory.yield_all_subdirectories():
                yield subsubdirectory


def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


class FileManager:

    root_directory: Directory
    current_location: Directory

    def __init__(self):
        self.root_directory = Directory("/")
        self.current_location = self.root_directory

    def cd(self, dirname: str):
        if dirname == "/":
            self.current_location = self.root_directory
        elif dirname == "..":
            if self.current_location.parent_directory is not None:
                self.current_location = self.current_location.parent_directory
        else:
            new_subdirectory = self.current_location.try_get_subdirectory(dirname)
            if new_subdirectory is None:
                new_subdirectory = Directory(name=dirname)
                self.current_location.add_subdirectory(new_subdirectory)
            self.current_location = new_subdirectory

    def add_file(self, filename: str, filesize: int):
        self.current_location.add_file(File(name=filename, size=filesize))

    def add_folder(self, dirname: str):
        self.current_location.add_subdirectory(Directory(name=dirname))

    def get_sum_of_directory_size_less_than_threshold(self, threshold: int) -> int:

        running_sum = 0

        if self.root_directory.get_total_dir_size() <= threshold:
            running_sum += self.root_directory.get_total_dir_size()

        for subdir in self.root_directory.yield_all_subdirectories():
            total_size = subdir.get_total_dir_size()
            if total_size <= threshold:
                running_sum += total_size

        return running_sum

    def get_size_of_smallest_sufficient_directory_to_delete(
        self, total_disk_space: int, required_space: int
    ) -> int:

        total_used_space = self.root_directory.get_total_dir_size()
        total_free_space = total_disk_space - total_used_space
        total_needed_space = required_space - total_free_space

        smallest_dir_size = total_used_space
        for subdir in self.root_directory.yield_all_subdirectories():
            total_size = subdir.get_total_dir_size()
            if total_needed_space < total_size < smallest_dir_size:
                smallest_dir_size = total_size

        return smallest_dir_size


def process_commands(
    commands: List[str],
    file_manager: FileManager,
):
    i = 0
    while i < len(commands):
        command = commands[i]
        command_parts = command.split(" ")
        if command_parts[0] == "$":

            if command_parts[1] == "cd":
                file_manager.cd(dirname=command_parts[2])

            elif command_parts[1] == "ls":

                i += 1
                listed_split_entries = []

                # aggregate all entries listed
                while i < len(commands):
                    entry = commands[i]
                    split_entry = entry.split(" ")
                    if split_entry[0] == "$":
                        i -= 1
                        break
                    listed_split_entries.append(split_entry)
                    i += 1

                # iterate through and process listed entries
                for split_entry in listed_split_entries:
                    if split_entry[0] == "dir":
                        file_manager.add_folder(dirname=split_entry[1])
                    else:
                        file_manager.add_file(
                            filename=split_entry[1], filesize=int(split_entry[0])
                        )

        i += 1


def run_part_a() -> str:
    data = get_data()
    file_manager = FileManager()
    process_commands(commands=data, file_manager=file_manager)

    return str(
        file_manager.get_sum_of_directory_size_less_than_threshold(threshold=100000)
    )


def run_part_b() -> str:
    data = get_data()
    file_manager = FileManager()
    process_commands(commands=data, file_manager=file_manager)

    return str(
        file_manager.get_size_of_smallest_sufficient_directory_to_delete(
            total_disk_space=70000000, required_space=30000000
        )
    )
