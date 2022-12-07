from src.utils import get_data
from typing import List


def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


class FileManager:

    filetree: dict
    current_location: List

    def __init__(self):
        self.filetree = {}
        self.current_location = ["/"]

    def cd(self, dirname: str):
        if dirname == "/":
            self.current_location = ["/"]
        elif dirname == "..":
            self.current_location.pop(-1)
        else:
            self.current_location.append(dirname)

    def add_file(self, filename: str, filesize: int):
        nested_set(
            dic=self.filetree, keys=self.current_location + [filename], value=filesize
        )

    def add_folder(self, dirname: str):
        nested_set(dic=self.filetree, keys=self.current_location + [dirname], value={})

    def get_directory_sizes(self):

        directory_sizes = {}

        def _get_nodes(tree):
            for key, value in tree.items():
                yield (key, value)
                if isinstance(value, dict):
                    yield from _get_nodes(value)

        def _get_total_filesize_from_dict(dict_to_evaluate: dict):
            def _paths(tree, cur=()):
                if not tree or not isinstance(tree, dict):
                    yield cur
                else:
                    for n, s in tree.items():
                        for path in _paths(s, cur + (n,)):
                            yield path

            total_filesize: int = 0

            for path in _paths(dict_to_evaluate):
                locator = dict_to_evaluate.copy()
                for path_segment in path:
                    locator = locator[path_segment]
                if isinstance(locator, int):
                    total_filesize += locator

            return total_filesize

        all_nodes = _get_nodes(self.filetree)
        for node in all_nodes:
            if isinstance(node[1], dict):
                dirsize = _get_total_filesize_from_dict(node[1])
                directory_sizes[node[0]] = dirsize

        return directory_sizes

    def get_sum_of_directory_size_less_than_threshold(self, threshold: int) -> int:
        return sum(
            dirsize
            for dirsize in self.get_directory_sizes().values()
            if dirsize < threshold
        )

    def get_size_of_smallest_sufficient_directory_to_delete(
        self, total_disk_space: int, required_space: int
    ) -> int:
        directory_sizes = self.get_directory_sizes()
        total_used_space = directory_sizes["/"]

        total_free_space = total_disk_space - total_used_space
        total_needed_space = required_space - total_free_space

        smallest_dir_size = total_used_space
        for dir, dirsize in directory_sizes.items():
            if dirsize > total_needed_space and dirsize < smallest_dir_size:
                smallest_dir_size = dirsize

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
