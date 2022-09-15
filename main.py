import pickle

with open("win_log_player_x.pkl", 'wb') as file:
    empty = ''
    pickle.dump(empty, file)

with open("win_log_player_o.pkl", 'wb') as file:
    empty = ''
    pickle.dump(empty, file)


def new_game():
    turn_x = True
    board = '7 8 9\n4 5 6\n1 2 3'
    print(board)

    def check_winner():
        if board[0] == board[2] == board[4] \
                == 'X' or board[6] == board[8] == board[10] \
                == 'X' or board[12] == board[14] == board[16] \
                == 'X' or board[0] == board[6] == board[12] \
                == 'X' or board[2] == board[8] == board[14] \
                == 'X' or board[4] == board[10] == board[16] \
                == 'X' or board[0] == board[8] == board[16] \
                == 'X' or board[4] == board[8] == board[12] \
                == 'X':
            with open("win_log_player_x.pkl", "rb") as file:
                win = 0.5
                entries = list(pickle.load(file))
                with open("win_log_player_x.pkl", "wb") as file2:
                    entries.append(win)
                    pickle.dump(entries, file2)
            return 'Player X is the winner!'

        elif board[0] == board[2] == board[4] \
                == 'O' or board[6] == board[8] == board[10] \
                == 'O' or board[12] == board[14] == board[16] \
                == 'O' or board[0] == board[6] == board[12] \
                == 'O' or board[2] == board[8] == board[14] \
                == 'O' or board[4] == board[10] == board[16] \
                == 'O' or board[0] == board[8] == board[16] \
                == 'O' or board[4] == board[8] == board[12] \
                == 'O':
            with open("win_log_player_o.pkl", "rb") as file:
                win = 0.5
                entries = list(pickle.load(file))
                with open("win_log_player_o.pkl", "wb") as file2:
                    entries.append(win)
                    pickle.dump(entries, file2)
            return 'Player O is the winner!'

        elif '1' not in board and '2' not in board and '3' not in board \
                and '4' not in board and '5' not in board and '6' not in board \
                and '7' not in board and '8' not in board and '9' not in board:
            print("It's a draw!")
            return play_again()
        else:
            return False

    def play_again():
        answer = input('Play again? (Y/N) Check wins?(C) Exit?(any key) ')
        if answer == 'Y':
            new_game()
        elif answer == 'C':
            check_wins()
        else:
            print('Bye!')

    def check_wins():
        with open("win_log_player_x.pkl", 'rb') as file:
            entries_x = list(pickle.load(file))

        with open("win_log_player_o.pkl", 'rb') as file:
            entries_o = list(pickle.load(file))
        print(f'Player X wins: {int(sum(entries_x))}\nPlayer O wins: {int(sum(entries_o))}')
        return play_again()

    while True:
        if turn_x:
            try:
                selection_x_int = int(input('Player X select your placement: '))
                selection_x = str(selection_x_int)
                if selection_x_int not in range(1, 10):
                    raise ValueError
                if board.find(selection_x) == -1 and selection_x_int != 0:
                    raise TypeError
            except TypeError:
                print('Placement is already occupied!')
                turn_x = True
            except ValueError:
                print('Wrong selection entered. Enter a number (1-9)')
                turn_x = True
            else:
                new_board = board.replace(selection_x, 'X')
                print(new_board)
                board = new_board
                turn_x = False
                if check_winner():
                    print(check_winner())
                    play_again()
                    break

        if not turn_x:
            try:
                selection_o_int = int(input('Player O select your placement: '))
                selection_o = str(selection_o_int)
                if selection_o_int not in range(1, 10):
                    raise ValueError
                if board.find(selection_o) == -1 and selection_o_int != 0:
                    raise TypeError
            except TypeError:
                print('Placement is already occupied!')
                turn_x = False
            except ValueError:
                print('Wrong selection entered. Enter a number (1-9)')
                turn_x = False
            else:
                new_board = board.replace(selection_o, 'O')
                print(new_board)
                board = new_board
                turn_x = True
                if check_winner():
                    print(check_winner())
                    play_again()
                    break


new_game()
