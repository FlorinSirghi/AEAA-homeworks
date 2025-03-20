"""
Production Plan Optimization using Google OR-Tools CP-SAT solver.
This program maximizes profit by determining optimal production quantities
for gas and chloride products under given constraints.
"""
from ortools.sat.python import cp_model


def main():
    """Solve the production plan optimization problem."""
    # Create the model
    model = cp_model.CpModel()

    # Constants
    MAX_TOTAL_PRODUCTION = 50
    MAX_CHLORIDE = 40
    MAX_RESOURCE_USAGE = 180
    
    GAS_PROFIT = 40
    CHLORIDE_PROFIT = 50
    
    GAS_RESOURCE_USAGE = 3
    CHLORIDE_RESOURCE_USAGE = 4

    # Decision variables
    gas = model.NewIntVar(0, MAX_TOTAL_PRODUCTION, 'gas')
    chloride = model.NewIntVar(0, MAX_CHLORIDE, 'chloride')

    # Constraints
    model.Add(gas + chloride <= MAX_TOTAL_PRODUCTION)
    model.Add(GAS_RESOURCE_USAGE * gas + CHLORIDE_RESOURCE_USAGE * chloride <= MAX_RESOURCE_USAGE)
    model.Add(chloride <= MAX_CHLORIDE)

    # Objective: maximize profit
    model.Maximize(GAS_PROFIT * gas + CHLORIDE_PROFIT * chloride)

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Process results
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Status: {solver.StatusName(status)}")
        print(f"Optimal production plan:")
        print(f"  Gas: {solver.Value(gas)} units")
        print(f"  Chloride: {solver.Value(chloride)} units")
        print(f"Total profit: {solver.ObjectiveValue()}")
    else:
        print(f"No solution found. Status: {solver.StatusName(status)}")


if __name__ == '__main__':
    main()