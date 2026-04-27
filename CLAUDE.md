# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running Solutions

All commands must be run from the repo root using the `advent_of_code.sh` script:

```bash
# Run a single day
./advent_of_code.sh {year} {-p|-c} {day} [-t]

# Run a range of days
./advent_of_code.sh {year} {-p|-c} {start-end} [-t]
```

- `-p` = Python, `-c` = C
- `-t` = use test input instead of full puzzle input
- The `build/` directory holds compiled C binaries (gitignored)

**Examples:**
```bash
./advent_of_code.sh 2024 -p 5        # Python, day 5, real input
./advent_of_code.sh 2024 -p 1-16     # Python, days 1–16
./advent_of_code.sh 2024 -p 3 -t     # Python, day 3, test input
./advent_of_code.sh 2024 -c 1        # C, day 1 (compile + run + cleanup)
```

## Architecture

### Year layout

Each year lives in `AdventOfCode{year}/` and is self-contained:

| Year | Languages | Entry point |
|------|-----------|-------------|
| 2024 | Python, C | `main.py` / `main.c` |
| 2025 | C++ | `c++_solutions/` (no shell script integration yet) |

### 2024 — Python

- `main.py` — parses CLI args (day number or `start-end` range, optional `-t`), calls the matching `day_N()` function, passes the resolved input file path.
- `python_solutions/day{N}.py` — each file exports a single `day_N(filename)` function that prints its own results.
- `helper.py` — shared file-reading utilities: `read_to_list`, `read_to_integer_matrix`, `read_to_char_matrix`, `read_by_line`.

### 2024 — C

- `main.c` — single file containing all day solutions; compiled fresh each run by the shell script via `gcc main.c helper.c -o build/main`.
- `helper.c` / `helper.h` — shared C utilities (`read_to_list`, `compare`).

### Puzzle inputs

Stored in `AdventOfCode{year}/puzzle_inputs/` following the naming convention:
- `day_{N}_input.txt` — full puzzle input
- `day_{N}_test_input.txt` — example/test input from the problem statement

### Adding a new day (2024 Python)

1. Create `AdventOfCode2024/python_solutions/day{N}.py` with a `day_N(filename)` function.
2. Import and add it to the `days` list in `main.py`.
3. Add puzzle input files to `puzzle_inputs/`.
