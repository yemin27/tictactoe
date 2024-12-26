"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Yegor Gladush
email: ygladush@seznam.cz
discord: yegi95
"""

def print_intro():
    """Vypíše úvodní text a pravidla hry."""
    print("""
    Vítejte ve hře piškvorky.
    ========================================
    Pravidla hry:
    Každý hráč může umístit jeden symbol (křížek nebo kolečko) za jeden tah na mřížce NxN. 
    Vítězem se stává ten, kterému se podaří umístit všechny své symboly v:
    * horizontální,
    * vertikální nebo
    * diagonální řadě.
    ========================================
    Spusťme hru.
    """)

def print_board(board):
    """Vypíše aktuální stav hracího pole s rovnoměrným zarovnáním."""
    size = len(board)
    cell_width = len(str(size * size))  # Určí šířku každé buňky podle největšího čísla
    print("=" * (size * (cell_width + 3) + 1))
    for row in board:
        print("+".join(["-" * (cell_width + 2)] * size) + "+")
        print("| " + " | ".join(f"{cell:>{cell_width}}" for cell in row) + " |")
    print("+".join(["-" * (cell_width + 2)] * size) + "+")
    print("=" * (size * (cell_width + 3) + 1))

def check_win(board, symbol):
    """Zkontroluje, zda hráč s daným symbolem vyhrál."""
    size = len(board)

    # Kontrola horizontálních a vertikálních řad
    for i in range(size):
        if all(cell == symbol for cell in board[i]):  # Horizontální
            return True
        if all(board[j][i] == symbol for j in range(size)):  # Vertikální
            return True

    # Kontrola diagonál
    if all(board[i][i] == symbol for i in range(size)):  # Hlavní diagonála
        return True
    if all(board[i][size - 1 - i] == symbol for i in range(size)):  # Vedlejší diagonála
        return True

    return False

def is_draw(board):
    """Zkontroluje, zda je remíza."""
    return all(cell in ("X", "O") for row in board for cell in row)

def get_move(player, board):
    """Získá validní tah od hráče."""
    size = len(board)
    while True:
        try:
            move = int(input(f"Hráč {player} | Zadejte číslo tahu (1-{size * size}): "))
            if move < 1 or move > size * size:
                print(f"Neplatný tah. Zvolte číslo mezi 1 a {size * size}.")
                continue
            row, col = divmod(move - 1, size)
            if board[row][col] in ("X", "O"):
                print("Tato buňka je již obsazená. Zkuste to znovu.")
                continue
            return row, col
        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo.")

def main():
    """Hlavní funkce programu."""
    print_intro()
    x_wins = 0
    o_wins = 0

    while True:
        # Dotaz na velikost hracího pole před každou hrou
        size = int(input("Zadejte velikost hracího pole (např. 3 pro 3x3): "))
        
        # Vytvoří nové hrací pole s číselnými označeními
        board = [[str(i * size + j + 1) for j in range(size)] for i in range(size)]
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
    main()