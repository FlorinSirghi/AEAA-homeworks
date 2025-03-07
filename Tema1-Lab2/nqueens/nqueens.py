from ortools.sat.python import cp_model

def solve_n_queens(n, blocked_positions=[], output_file="n_queens_solution.txt"):
    model = cp_model.CpModel()

    # Variables: Each row gets exactly one queen in a column (0 to n-1)
    queens = [model.NewIntVar(0, n - 1, f'q{i}') for i in range(n)]

    # Constraints:
    # 1. All queens must be in different columns
    model.AddAllDifferent(queens)

    # 2. No two queens can be on the same diagonal
    model.AddAllDifferent([queens[i] + i for i in range(n)])  # Left-to-right diagonal
    model.AddAllDifferent([queens[i] - i for i in range(n)])  # Right-to-left diagonal

    # 3. Blocked positions constraint (queen cannot be placed at blocked positions)
    for row, col in blocked_positions:
        model.Add(queens[row] != col)

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Save results to a file
    with open(output_file, "w") as f:
        if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for i in range(n):
                board[i][solver.Value(queens[i])] = 'Q'  # Place the queen
            for row, col in blocked_positions:
                board[row][col] = 'X'  # Mark blocked positions

            # Write board to file
            for row in board:
                f.write(' '.join(row) + "\n")
            print(f"Solution saved to {output_file}")
        else:
            f.write("No solution found.\n")
            print("No solution found.")

# Run for 4x4 without blocked positions and save to file
solve_n_queens(4, output_file="n_queens_4x4.txt")

# Run for 4x4 with blocked positions and save to file
solve_n_queens(4, blocked_positions=[(1,1), (2,2)], output_file="n_queens_4x4_blocked.txt")
