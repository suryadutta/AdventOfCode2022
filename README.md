# Advent Of Code 2022

Code for my submissions to Advent of Code 2022
Python 3.11 + Poetry

Heavily relies on the excellent AOCD package created by @wimglenn: https://github.com/wimglenn/advent-of-code-data

### Prerequisites

1. If Python 3.11 isn't installed on your computer, install it such that it can be run using the `python3.11` command
2. [Follow the instructions here](https://github.com/wimglenn/advent-of-code-wim/issues/1) to save your AOCD session token to ` ~/.config/aocd/token` 

### Quickstart

#### Running code

```shell
AOC_DAY=1 make run
```

### Submitting solutions

```shell
AOC_DAY=1 \
make submit_part_a \
make submit_part_b
```