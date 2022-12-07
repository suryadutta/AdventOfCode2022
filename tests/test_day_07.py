from src.day07 import File, Directory, FileManager, process_commands


def test_file_manager():

    manager = FileManager()

    manager.cd(dirname="/")
    manager.cd(dirname="level_1")
    manager.cd(dirname="level_2")
    manager.add_file(filename="test_file", filesize=12345)

    assert manager.root_directory == Directory(
        name="/",
        subdirectories=[
            Directory(
                "level_1",
                subdirectories=[
                    Directory("level_2", files=[File(name="test_file", size=12345)])
                ],
            )
        ],
    )

    manager.cd("..")
    manager.cd("level_2b")
    manager.add_file("test_file_2", 23456)

    assert manager.root_directory == Directory(
        name="/",
        subdirectories=[
            Directory(
                name="level_1",
                subdirectories=[
                    Directory(
                        name="level_2", files=[File(name="test_file", size=12345)]
                    ),
                    Directory(
                        name="level_2b", files=[File(name="test_file_2", size=23456)]
                    ),
                ],
            )
        ],
    )

    manager.cd("..")
    manager.add_folder("level_2c")

    assert manager.root_directory == Directory(
        name="/",
        subdirectories=[
            Directory(
                name="level_1",
                subdirectories=[
                    Directory(
                        name="level_2", files=[File(name="test_file", size=12345)]
                    ),
                    Directory(
                        name="level_2b", files=[File(name="test_file_2", size=23456)]
                    ),
                    Directory(name="level_2c"),
                ],
            )
        ],
    )


def test_process_commands():

    test_commands = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]

    test_file_manager = FileManager()

    process_commands(test_commands, file_manager=test_file_manager)

    assert test_file_manager.root_directory == Directory(
        name="/",
        subdirectories=[
            Directory(
                name="a",
                subdirectories=[Directory(name="e", files=[File(name="i", size=584)])],
                files=[
                    File(name="f", size=29116),
                    File(name="g", size=2557),
                    File(name="h.lst", size=62596),
                ],
            ),
            Directory(
                name="d",
                files=[
                    File(name="j", size=4060174),
                    File(name="d.log", size=8033020),
                    File(name="d.ext", size=5626152),
                    File(name="k", size=7214296),
                ],
            ),
        ],
        files=[File(name="b.txt", size=14848514), File(name="c.dat", size=8504156)],
    )

    assert (
        test_file_manager.get_sum_of_directory_size_less_than_threshold(
            threshold=100000
        )
        == 95437
    )

    assert (
        test_file_manager.get_size_of_smallest_sufficient_directory_to_delete(
            total_disk_space=70000000, required_space=30000000
        )
        == 24933642
    )
