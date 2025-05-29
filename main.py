from uno import Game
from sys import exit as sys_exit

if __name__ == "__main__":
    game = Game()
    game.start()
    # Ensures safe and clean exit, unsure of its necessity tho
    sys_exit(0)
