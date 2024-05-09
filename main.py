import random

print("Welcome to Tic Tac Toe(text version)")

end_of_game = False

# user_column = input('Which column would you like to enter player X')
# column = int(user_column)
options = ['X', 'O']

row_1 = {'1': "_", '2': "_", '3': "_"}
row_2 = {'1': "_", '2': "_", '3': "_"}
row_3 = {'1': "_", '2': "_", '3': "_"}

table = {
    "row_1": row_1,
    'row_2': row_2,
    'row_3': row_3
}

while not end_of_game:
    user_column = input('Which column would you like to enter player X (press 0 to exit)')
    try:
        column = int(user_column)
    except ValueError:
        print('You must enter a number between 0-3')
    else:
        if column == 1:
            user_row = input("Which row would you like to place?")
            row = int(user_row)
            if row == 1 and row_1['1'] == '_':
                row_1['1'] = 'X'
            elif row == 2 and row_2['1'] == '_':
                row_2['1'] = 'X'
            elif row == 3 and row_3['1'] == '_':
                row_3['1'] = 'X'
            else:
                print("Remember you can only choose an available spot up to 3")
        elif column == 2:
            user_row = input("Which row would you like to place?")
            row = int(user_row)
            if row == 1 and row_1['2'] == '_':
                row_1['2'] = 'X'
            elif row == 2 and row_2['2'] == '_':
                row_2['2'] = 'X'
            elif row == 3 and row_3['2'] == '_':
                row_3['2'] = 'X'
            else:
                print("Remember you can only choose an available spot up to 3")
        elif column == 3:
            user_row = input("Which row would you like to place?")
            row = int(user_row)
            if row == 1 and row_1['3'] == '_':
                row_1['3'] = 'X'
            elif row == 2 and row_2['3'] == '_':
                row_2['3'] = 'X'
            elif row == 3 and row_3['3'] == '_':
                row_3['3'] = 'X'
            else:
                print("Remember you can only choose up to 3")
        elif column == 0:
            print("Thanks for playing, until next time")
            end_of_game = True
        else:
            print("Hmm, there are only 3 columns. Please try again.")

    for n in options:
        if n == row_1['1'] and n == row_1['2'] and n == row_1['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['1'] and n == row_2['2'] and n == row_3['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['3'] and n == row_2['2'] and n == row_3['1']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['2'] and n == row_2['2'] and n == row_3['2']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['1'] and n == row_2['1'] and n == row_3['1']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['3'] and n == row_2['3'] and n == row_3['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_2['1'] and n == row_2['2'] and n == row_2['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_3['1'] and n == row_3['2'] and n == row_3['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif '_' in table.values() == False:
            print('This Game is a Tie!')
            end_of_game = True

    # user_column = input('Which column would you like to enter player O (press 0 to exit)')
    column = random.randint(1, 3)
    try:
        column = int(user_column)
    except ValueError:
        print('You must enter a number between 0-3')
    else:
        if column == 1:
            # user_row = input("Which row would you like to place?")
            # row = int(user_row)
            row = random.randint(1, 3)
            if row == 1 and row_1['1'] == '_':
                row_1['1'] = 'O'
            elif row == 2 and row_2['1'] == '_':
                row_2['1'] = 'O'
            elif row == 3 and row_3['1'] == '_':
                row_3['1'] = 'O'
            else:
                print("Remember you can only choose an available spot up to 3!")
        elif column == 2:
            # user_row = input("Which row would you like to place?")
            # row = int(user_row)
            row = random.randint(1, 3)
            if row == 1 and row_1['2'] == '_':
                row_1['2'] = 'O'
            elif row == 2 and row_2['2'] == '_':
                row_2['2'] = 'O'
            elif row == 3 and row_2['2'] == '_':
                row_3['2'] = 'O'
            else:
                print("Remember you can only choose an available spot up to 3!")
        elif column == 3:
            # user_row = input("Which row would you like to place?")
            # row = int(user_row)
            row = random.randint(1, 3)
            if row == 1 and row_1['3'] == '_':
                row_1['3'] = 'O'
            elif row == 2 and row_2['3'] == '_':
                row_2['3'] = 'O'
            elif row == 3 and row_3['3'] == '_':
                row_3['3'] = 'O'
            else:
                print("Remember you can only choose up to 3")
        elif column == 0:
            print("Thanks for playing, until next time!")
            end_of_game = True
        else:
            print("Remember you can only choose an available spot up to 3!")

    [print(values) for values in table.values()]

    for n in options:
        if n == row_1['1'] and n == row_1['2'] and n == row_1['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['1'] and n == row_2['2'] and n == row_3['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['3'] and n == row_2['2'] and n == row_3['1']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['2'] and n == row_2['2'] and n == row_3['2']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['1'] and n == row_2['1'] and n == row_3['1']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_1['3'] and n == row_2['3'] and n == row_3['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_2['1'] and n == row_2['2'] and n == row_2['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif n == row_3['1'] and n == row_3['2'] and n == row_3['3']:
            print(f"{n} wins!")
            end_of_game = True
        elif '_' in table.values() == False:
            print('This Game is a Tie!')
            end_of_game = True
