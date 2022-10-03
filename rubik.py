from cube import Cube
from solver import solver
from rubik3D import Game
import time
import sys

def main():
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
    else:
        print("Please enter a scramble pattern")
        return
    cube = Cube()
    pattern = "L2 F R2 B U2 B' F2 U2 F L2 D' L' B' R' F D' F U2 B2 B'"
    # pattern = cube.random(55)
    pattern = "R U R2 F B L2 F' D' R' R' B2 D' B' F' R2 U' L D F' D U2 L2 L R' R' B L' B' F U2 B2 F L U' L2 F2 L2 L' R2 F B2 B' D2 U' R U' D D' U D B' L' R' B U2 U B' L D' F L' L' U B2 R L' F' U' D2 B2 R' L L2 L' D' L' L' R F"
    print(pattern)
    cube.scramble(pattern)
    start = time.time()
    solved = solver(cube)
    print(solved)
    end = time.time()
    print(f"Time elapsed: {end - start}")
    cube.printCube()

    graph = input("Do you want to display 3D render ? y/n\n")
    if graph == "y":
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