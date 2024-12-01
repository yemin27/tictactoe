... """
... projekt_2.py: druhý projekt do Engeto Online Python Akademie
... author: Yegor Gladush
... email: ygladush@seznam.cz
... discord: yegi95
... """
... 
... def print_intro():
...     """Vypíše úvodní text a pravidla hry."""
...     print("""
...     Vítejte ve hře piškvorky.
...     ========================================
...     Pravidla hry:
...     Každý hráč může umístit jeden symbol (křížek nebo kolečko) za jeden tah na mřížce 3x3. Vítězem se stává ten, kterému se podaří umístit tři ze svých symbolů v:
...     * horizontální,
...     * vertikální nebo
...     * diagonální řádek.
...     ========================================
...     Spusťme hru.
...     """)
... 
... def print_board(board):
...     """Vypíše aktuální stav hracího pole."""
...     print("=" * 40)
...     for row in range(3):
...         print("+---+---+---+")
...         print(f"| {board[row][0]} | {board[row][1]} | {board[row][2]} |")
...     print("+---+---+---+")
...     print("=" * 40)
... 
... def check_win(board, symbol):
...     """Zkontroluje, zda hráč s daným symbolem vyhrál."""
...     for row in board:
...         if all(cell == symbol for cell in row):
...             return True
...     for col in range(3):
...         if all(board[row][col] == symbol for row in range(3)):
...             return True
...     if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
...         return True
...     return False
... 
... def is_draw(board):
...     """Zkontroluje, zda je remíza."""
...     return all(cell != " " for row in board for cell in row)
... 
... def get_move(player, board):
...     """Získá validní tah od hráče."""
...     while True:
...         try:
...             move = int(input(f"Hráč {player} | Zadejte prosím číslo tahu a stiskněte Enter (1-9): "))
...             if move < 1 or move > 9:
...                 print("Neplatný tah. Zvolte prosím číslo mezi 1 a 9.")
...                 continue
...             row, col = divmod(move - 1, 3)
...             if board[row][col] != " ":
...                 print("Tato buňka je již obsazená. Zkuste to znovu.")
...                 continue
...             return row, col
        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo od 1 do 9.")

def main():
    """Hlavní funkce programu."""
    print_intro()
    x_wins = 0
    o_wins = 0

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        print_board(board)
        current_player = "X"

        while True:
            row, col = get_move(current_player, board)
            board[row][col] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"Gratulujeme, hráč {current_player} vyhrává!")
                if current_player == "X":
                    x_wins += 1
                else:
                    o_wins += 1
                break
            if is_draw(board):
                print("Je to remíza! Už nezbývají žádné tahy.")
                break

            current_player = "O" if current_player == "X" else "X"

        print(f"\nSkóre:")
        print(f"Hráč X: {x_wins} výher")
        print(f"Hráč O: {o_wins} výher\n")

        restart = input("Chcete hrát znovu? (ano/ne): ").strip().lower()
        if restart != "ano":
            print("Děkujeme za hraní! Nashledanou.")
            break

if __name__ == "__main__":
