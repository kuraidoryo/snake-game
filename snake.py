import curses
import time
import random
from curses import wrapper


def main(stdscr):
    def main_menu(lang="en"):
        max_y, max_x = stdscr.getmaxyx()

        stdscr.clear()
        if lang == "en":
            stdscr.addstr(int(max_y / 2) - 2, int(max_x / 2) - len("Welcome to Snake Game made by Kuraidoryo!") // 2, "Welcome to Snake Game made by Kuraidoryo!")
            stdscr.addstr(int(max_y / 2) - 1, int(max_x / 2) - len("Press 'l' to change the language") // 2, "Press 'l' to change the language")
            stdscr.addstr(int(max_y / 2), int(max_x / 2) - len("Press 's' to Start Game") // 2, "Press 's' to Start Game")
            stdscr.addstr(int(max_y / 2) + 1, int(max_x / 2) - len("Press 'i' for Instructions") // 2, "Press 'i' for Instructions")
            stdscr.addstr(int(max_y / 2) + 2, int(max_x / 2) - len("Press 'q' to Quit") // 2, "Press 'q' to Quit")
        else:
            stdscr.addstr(int(max_y / 2) - 2, int(max_x / 2) - len("Witaj w grze snake autorstwa Kuraidoryo!") // 2, "Witaj w grze snake autorstwa Kuraidoryo!")
            stdscr.addstr(int(max_y / 2) - 1, int(max_x / 2) - len("Kliknij 'l' aby zmienić język") // 2, "Kliknij 'l' aby zmienić język")
            stdscr.addstr(int(max_y / 2), int(max_x / 2) - len("Kliknij 's' aby rozpocząć grę") // 2, "Kliknij 's' aby rozpocząć grę")
            stdscr.addstr(int(max_y / 2) + 1, int(max_x / 2) - len("Kliknij 'i' aby zobaczyć instrukcje") // 2, "Kliknij 'i' aby zobaczyć instrukcje")
            stdscr.addstr(int(max_y / 2) + 2, int(max_x / 2) - len("Kliknij 'q' aby zakończyć") // 2, "Kliknij 'q' aby zakończyć")
        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if key == ord('s'):
                main_game(lang)
                break
            elif key == ord('i'):
                instructions(lang)
                break
            elif key == ord('l'):
                lang = "pl" if lang == "en" else "en"
                return main_menu(lang) 
            elif key == ord('q'):
                return

    def instructions(lang):
        max_y, max_x = stdscr.getmaxyx()

        stdscr.clear()
        if lang == "en":
            stdscr.addstr(int(max_y / 2) - 2, int(max_x / 2) - len("Instructions:") // 2, "Instructions:")
            stdscr.addstr(int(max_y / 2) - 1, int(max_x / 2) - len("Use 'WASD' keys to move the snake.") // 2, "Use 'WASD' keys to move the snake.")
            stdscr.addstr(int(max_y / 2), int(max_x / 2) - len("Eat the '$' to grow and earn points.") // 2, "Eat the '$' to grow and earn points.")
            stdscr.addstr(int(max_y / 2) + 1, int(max_x / 2) - len("Avoid running into walls or yourself.") // 2, "Avoid running into walls or yourself.")
            stdscr.addstr(int(max_y / 2) + 2, int(max_x / 2) - len("Press 'q' to quit during the game.") // 2, "Press 'q' to quit during the game.")
            stdscr.addstr(int(max_y / 2) + 3, int(max_x / 2) - len("Press any key to return to the main menu.") // 2, "Press any key to return to the main menu.")
        else:
            stdscr.addstr(int(max_y / 2) - 2, int(max_x / 2) - len("Instrukcje:") // 2, "Instrukcje:")
            stdscr.addstr(int(max_y / 2) - 1, int(max_x / 2) - len("Użyj klawiszy 'WASD' aby poruszać wężem.") // 2, "Użyj klawiszy 'WASD' aby poruszać wężem.")
            stdscr.addstr(int(max_y / 2), int(max_x / 2) - len("Zjadaj '$' aby rosnąć i zdobywać punkty.") // 2, "Zjadaj '$' aby rosnąć i zdobywać punkty.")
            stdscr.addstr(int(max_y / 2) + 1, int(max_x / 2) - len("Unikaj uderzania w ściany lub siebie.") // 2, "Unikaj uderzania w ściany lub siebie.")
            stdscr.addstr(int(max_y / 2) + 2, int(max_x / 2) - len("Naciśnij 'q' aby zakończyć grę.") // 2, "Naciśnij 'q' aby zakończyć grę.")
            stdscr.addstr(int(max_y / 2) + 3, int(max_x / 2) - len("Naciśnij dowolny klawisz aby wrócić do menu głównego.") // 2, "Naciśnij dowolny klawisz aby wrócić do menu głównego.")

        stdscr.refresh()
        stdscr.getch()
        main_menu(lang)

    def pause_menu(lang):
        max_y, max_x = stdscr.getmaxyx()
        
        stdscr.clear()
        if lang == "en":
            stdscr.addstr(int(max_y / 2) - 1, int(max_x / 2) - len("Game Paused") // 2, "Game Paused")
            stdscr.addstr(int(max_y / 2), int(max_x / 2) - len("Press 'r' to Resume") // 2, "Press 'r' to Resume")
            stdscr.addstr(int(max_y / 2) + 1, int(max_x / 2) - len("Press 'q' to Quit to Main Menu") // 2, "Press 'q' to Quit to Main Menu")
        else:
            stdscr.addstr(int(max_y / 2) - 1, int(max_x / 2) - len("Gra wstrzymana") // 2, "Gra wstrzymana")
            stdscr.addstr(int(max_y / 2), int(max_x / 2) - len("Naciśnij 'r' aby wznowić") // 2, "Naciśnij 'r' aby wznowić")
            stdscr.addstr(int(max_y / 2) + 1, int(max_x / 2) - len("Naciśnij 'q' aby wrócić do menu głównego") // 2, "Naciśnij 'q' aby wrócić do menu głównego")

        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if key == ord('r'):
                stdscr.nodelay(True)
                return
            elif key == ord('q'):
                main_menu(lang)
                return

    def main_game(lang):
        direction = "East"
        points = 0
        try:
            with open("highscore.txt", "r") as f:
                highscore = int(f.read())
        except:
            highscore = 0
        y, x = 10, 10
        max_y, max_x = stdscr.getmaxyx()
        food_x, food_y = random.randint(1, max_x - 2), random.randint(1, max_y - 2)
        snake = [(y, x)]
        snake_length = 1

        stdscr.nodelay(True)
        stdscr.timeout(100)

        while True:
            key = stdscr.getch()

            if key == ord('w') and direction != "South":
                direction = "North"
            elif key == ord('s') and direction != "North":
                direction = "South"
            elif key == ord('a') and direction != "East":
                direction = "West"
            elif key == ord('d') and direction != "West":
                direction = "East"
            elif key == ord('p'):
                pause_menu(lang)
            elif key == ord('q'):
                break
            
            head_y, head_x = snake[0]
            
            if direction == "North":
                head_y -= 1
            elif direction == "South":
                head_y += 1
            elif direction == "West":
                head_x -= 1
            elif direction == "East":
                head_x += 1

            if head_x < 0 or head_y < 0 or head_x >= max_x or head_y >= max_y or (head_y, head_x) in snake:
                break

            new_head = (head_y, head_x)
            snake.insert(0, new_head)

            if (food_y, food_x) == new_head:
                points += 1
                if points > highscore:
                    highscore = points
                snake_length += 1
                food_x, food_y = random.randint(1, max_x - 2), random.randint(1, max_y - 2)
            else:
                snake.pop()

            stdscr.clear()
            if lang == "en":
                stdscr.addstr(0, 0, f'Points: {points} Highscore: {highscore}')
            else:
                stdscr.addstr(0, 0, f'Punkty: {points} Rekord: {highscore}')
            stdscr.addstr(food_y, food_x, '$')
            for seg in snake:
                stdscr.addstr(seg[0], seg[1], '#')
            stdscr.refresh()

        with open("highscore.txt", "w") as f:
            f.write(str(highscore))

    main_menu()
    
if __name__ == "__main__":
    wrapper(main)