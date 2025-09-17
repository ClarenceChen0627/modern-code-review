def is_win(game):
    win = False
    # Check rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # Check columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):
        turn = not turn  # Switch turns
        if not turn:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        
        # 完善的输入处理逻辑
        while True:
            print("Which cell to mark? i:[1..3], j:[1..3]: ")
            try:
                # 尝试解析输入
                i, j = map(int, input().split())
                # 检查范围
                if not (1 <= i <= 3 and 1 <= j <= 3):
                    print("Error: i and j must be between 1 and 3. Try again.")
                    continue
                # 转换为0-based索引
                i -= 1
                j -= 1
                # 检查单元格是否已被占用
                if game[i][j] != ' ':
                    print("Error: That cell is already occupied. Try again.")
                    continue
                # 所有验证通过，退出循环
                break
            except ValueError:
                print("Error: Please enter two integers separated by space. Try again.")
        
        # 放置棋子
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        
        # 显示当前棋盘（包括最后一步）
        print("Current board:")
        for row in game:
            print(" ".join(row))
        
        # 检查游戏结束条件
        if is_win(game):
            print(f"Player {1 if not turn else 2} wins!")
            break  # 游戏结束
        if n == 8:  # 所有格子填满
            print("It's a tie!")

if __name__ == "__main__":
    main()
