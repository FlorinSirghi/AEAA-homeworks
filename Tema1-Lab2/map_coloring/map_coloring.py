from ortools.sat.python import cp_model

def main():
    print('Solving the map coloring problem:')
    # Create the model
    model = cp_model.CpModel()

    # Define the countries
    countries = ['Belgium', 'Denmark', 'France', 'Germany', 'Luxembourg', 'Netherlands']

    # Create variables for each country with domain 0-3 (representing 4 colors)
    color_vars = {country: model.NewIntVar(0, 3, country) for country in countries}

    # Define the neighboring countries
    neighbors = [
        ('Belgium', 'France'),
        ('Belgium', 'Germany'),
        ('Belgium', 'Luxembourg'),
        ('Belgium', 'Netherlands'),
        ('Denmark', 'Germany'),
        ('France', 'Germany'),
        ('France', 'Luxembourg'),
        ('Germany', 'Luxembourg'),
        ('Germany', 'Netherlands')
    ]

    # Add constraints that neighboring countries must have different colors
    for country1, country2 in neighbors:
        model.Add(color_vars[country1] != color_vars[country2])

    # Create the solver and solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print the solution
    if status == cp_model.OPTIMAL:
        for country in countries:
            print(f'{country}: {solver.Value(color_vars[country])}')
    else:
        print('No solution found.')
def germany_and_denmark_same_color():
    print('Germany and Denmark must have the same color:')
    # Create the model
    model = cp_model.CpModel()

    # Define the countries
    countries = ['Belgium', 'Denmark', 'France', 'Germany', 'Luxembourg', 'Netherlands']

    # Create variables for each country with domain 0-3 (representing 4 colors)
    color_vars = {country: model.NewIntVar(0, 3, country) for country in countries}

    # Define the neighboring countries
    neighbors = [
        ('Belgium', 'France'),
        ('Belgium', 'Germany'),
        ('Belgium', 'Luxembourg'),
        ('Belgium', 'Netherlands'),
        ('Denmark', 'Germany'),
        ('France', 'Germany'),
        ('France', 'Luxembourg'),
        ('Germany', 'Luxembourg'),
        ('Germany', 'Netherlands')
    ]

    # Add constraints for neighboring countries - different colors except for Germany-Denmark
    for country1, country2 in neighbors:
        if not (country1 == 'Denmark' and country2 == 'Germany') and not (country1 == 'Germany' and country2 == 'Denmark'):
            model.Add(color_vars[country1] != color_vars[country2])

    # Add constraint that Germany and Denmark must have the same color
    model.Add(color_vars['Germany'] == color_vars['Denmark'])

    # Create the solver and solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        for country in countries:
            print(f'{country}: {solver.Value(color_vars[country])}')
    else:
        print('No solution found.')
def including_switzerland():
    print('Including Switzerland in the map coloring problem:')
    # Create the model
    model = cp_model.CpModel()

    # Define the countries - now including Switzerland
    countries = ['Belgium', 'Denmark', 'France', 'Germany', 'Luxembourg', 'Netherlands', 'Switzerland']

    # Create variables for each country with domain 0-3 (representing 4 colors)
    color_vars = {country: model.NewIntVar(0, 3, country) for country in countries}

    # Define the neighboring countries, including Switzerland's borders
    neighbors = [
        ('Belgium', 'France'),
        ('Belgium', 'Germany'),
        ('Belgium', 'Luxembourg'),
        ('Belgium', 'Netherlands'),
        ('Denmark', 'Germany'),
        ('France', 'Germany'),
        ('France', 'Luxembourg'),
        ('Germany', 'Luxembourg'),
        ('Germany', 'Netherlands'),
        ('France', 'Switzerland'),  # Switzerland borders France
        ('Germany', 'Switzerland')  # Switzerland borders Germany
    ]

    # Add constraints that neighboring countries must have different colors
    for country1, country2 in neighbors:
        model.Add(color_vars[country1] != color_vars[country2])

    # Create the solver and solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print the solution
    if status == cp_model.OPTIMAL:
        for country in countries:
            print(f'{country}: {solver.Value(color_vars[country])}')
    else:
        print('No solution found.')

if __name__ == '__main__':
    main()
    germany_and_denmark_same_color()
    including_switzerland()