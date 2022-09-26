from ast import pattern
from time import sleep
from cube import Cube
import solver
from rubik3D import Game
import sys

def main():
    cube = Cube()
    pattern = "F2 D2 R' F2 R D2 F2 R2 U' F D R2 B2 L' F' R D' U2 F R2"
    cube.scramble(pattern)
    solved = " ".join("F2 D2 R F2 R' D2 F2 R2 U F' D' R2 B2 L F R' D U2 F' R2".split()[::-1])
    cube.printCube()

    if len(sys.argv) > 1:
        if sys.argv[1] == "-v":
            game = Game()
            game.setScramble(pattern)
            game.setSolver(solved)
            game.game_mode = "solver"
            game.run()
    return

if __name__ == "__main__":
    main()


#menu avec input ?
# menu choisir ouvrir rendu 3D ?