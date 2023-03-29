board_size = 3  # Размер игрового поля (3 на 3).
empty_mark = '_'  # Заполнитель пустой ячейки
x_mark = 'X'  # Крестик
o_mark = 'O'  # Нолик


# Функция создания доски
def create_board():
    return [[empty_mark for j in range(board_size)] for i in range(board_size)]


# Функция которая отрисовывает доску на экране.
def show_board(board):
    print(' ', *range(1, board_size + 1))
    for i in range(board_size):
        row_str = str(i + 1) + ' '
        for j in range(board_size):
            row_str += board[i][j] + ' '
        print(row_str)


# Функция проверки на выигрыш.
def check_win(board, mark):
    # Проверка строк на выигрыш.
    for i in range(board_size):
        if all(board[i][j] == mark for j in range(board_size)):
            return True
    # Проверка столбцов на выигрыш.
    for j in range(board_size):
        if all(board[i][j] == mark for i in range(board_size)):
            return True
    # Проверка диагоналей на выигрыш.
    if all(board[i][i] == mark for i in range(board_size)):
        return True
    if all(board[i][board_size - 1 - i] == mark for i in range(board_size)):
        return True
    return False


# Основная функция игры.
def main():
    board = create_board()  # Отрисовка игрового поля.
    current_player = x_mark  # Метка игрока. Начинает крестик.
    winner = None  # Флаг победителя
    num_turns = 0  # Счетчик ходов.
    max_turns = board_size ** 2  # Максимальное количество ходов.

    # Игровой цикл.
    while num_turns < max_turns and not winner:  # Пока не достигнуто максимальное количество ходов и нет победителя.
        show_board(board)
        print(f"Ход игрока {current_player}")
        row = int(input("Введите номер строки: "))
        col = int(input("Введите номер столбца: "))

        if board[row - 1][col - 1] == empty_mark:
            board[row - 1][col - 1] = current_player
            num_turns += 1

            if check_win(board, current_player):
                winner = current_player
            else:
                # Смена игрока
                current_player = o_mark if current_player == x_mark else x_mark
        else:
            print("Эта ячейка уже занята, введите другую")

    show_board(board)
    if winner:
        print(f'Игрок {winner} победил!')
    else:
        print('Ничья.')


# Запуск игры
main()
