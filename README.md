# py-sudoku
A relatively fast and capable sudoku solver written in Python.

# Installation
Clone/download `sudoku_solver.py` and run `python3 sudoku_solver.py`.

# Usage
Follow the instructions.

# Motivation
I wanted to implement a simple backtracking algorithm, but then I cringed at how slow it can be. By also implementing some basic logic rules and constraints for our puzzle solver, I managed to not rely on backtracking at all for easy puzzles.

These rules consist of simple row/column/box constraints, along with finding naked pairs and singles (is this a thing? I don't know, but it works). Since implementing naked triples and all hidden pairs/triples can be complicated, filling the runner with many, many functions, I found these constraints sufficient.

For more 'evil' puzzles that cannot be solved using these logical rules, the incomplete puzzle is then passed onto the backtracker, which then should solve the puzzle much faster than solving with backtracking alone.

Inputting the sudoku is a painfully annoying process, I don't know how it can be made easier.
