from src.day07 import FileManager, process_commands


def test_file_manager():

    manager = FileManager()

    manager.cd("/")
    manager.cd("level_1")
    manager.cd("level_2")
    manager.add_file("test_file", 12345)

    assert manager.filetree == {"/": {"level_1": {"level_2": {"test_file": 12345}}}}

    manager.cd("..")
    manager.cd("level_2b")
    manager.add_file("test_file_2", 23456)

    assert manager.filetree == {
        "/": {
            "level_1": {
                "level_2": {"test_file": 12345},
                "level_2b": {"test_file_2": 23456},
            }
        }
    }

    assert manager.get_sum_of_directory_size_less_than_threshold(threshold=100000) == (12345 + 23456) * 3

    manager.cd("..")
    manager.add_folder("level_2c")
    assert manager.filetree == {
        "/": {
            "level_1": {
                "level_2": {"test_file": 12345},
                "level_2b": {"test_file_2": 23456},
                "level_2c": {},
            }
        }
    }


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

    assert test_file_manager.filetree == {
        "/": {
            "a": {"e": {"i": 584}, "f": 29116, "g": 2557, "h.lst": 62596},
            "b.txt": 14848514,
            "c.dat": 8504156,
            "d": {"j": 4060174, "d.log": 8033020, "d.ext": 5626152, "k": 7214296},
        }
    }

    assert test_file_manager.get_sum_of_directory_size_less_than_threshold(threshold=100000) == 95437
