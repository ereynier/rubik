from ast import pattern
from time import sleep
import solver
from cube import Cube
from rubik3D import Game
import sys

def main():
    cube = Cube()
    pattern = cube.random()
    cube.scramble(pattern)
    solved = pattern
    cube.printCube()

    if len(sys.argv) > 1:
        if sys.argv[1] == "-v":
            game = Game()
            game.setScramble(pattern)
            game.solved = solved
            game.game_mode = "solver"
            game.run()
    return

if __name__ == "__main__":
    main()