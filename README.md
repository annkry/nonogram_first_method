# nonogram_first_method
The program you will solve simplified logical puzzles called "nonograms" using an algorithm inspired by the WalkSat algorithm. Here's how it works:
• The program starts with an initial color assignment for all fields in the puzzle (all zeros).
• During the algorithm's operation, it will change the color of a selected field in the puzzle (one at a time) until the puzzle is complete.
• The selection of a field is done as follows:

A row (or column) is randomly chosen that violates the puzzle's rules (i.e., black pixels do not form a block of the required length).
A pixel with coordinates (i, j) is selected, whose change will most significantly improve the overall fit in row i and column j.
• Some of the selections are made suboptimally with a small probability (e.g., only fixing the row instead of both the row and column).
• If the program has not found a solution for a long time, the initial settings are randomized and the algorithm restarts.

To run all tests: python validator.py zad5 python main.py
