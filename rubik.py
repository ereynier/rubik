from ast import pattern
from time import sleep
from cube import Cube
#import solver
from rubik3D import Game
import sys

def main():
    cube = Cube()
    pattern = "D' B U2 L2 D2 B2 R' B F R D F' U' D F D2 F2 L' B L R2 D2 F2 D2 U"
    cube.scramble(pattern)
    solved = cube.reverseScramble(pattern)
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