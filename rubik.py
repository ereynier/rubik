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
    #pattern = cube.reducePattern(cube.random(55))
    #pattern = "R U R2 F B L2 F' D' R2 B2 D' B' F' R2 U' L D F' D U2 L' R2 B L' B' F U2 B2 F L U' L2 F2 L R2 F B D2 U' R D B' L' R' B U' B' L D' F L2 U B2 R L' F' U' D2 B2 R' L2 D' L2 R F"
    #pattern = cube.reducePattern("L R D2 U2 D2 U L' U' R' F' R L' B' L2 B L' R2 U2 B' R L R' U' R' D2 F2 R D2 L U' R2 B' R2 U2 R' L F2 B' L2 B' L2 R' F' L2 U B2 L D U2 L2 D2 B2 R' L B2 U B2 F U2 R2 B R2 D U' D2 F2 U2 L R2 U2 L U F2 L' D' U2 L' F2 B' D U D' L' R2 U' B2 U' F D' U B D U D2 R U' F2 R B2 L D2 U L D' F L' D' R2 L' B L' D2 L2 D2 L2 U2 F' D' F' L2 R2 U R' D2 B R B2 R' D' B' L' F R L' B R")
    #680 move wirh multiprocerss V
    #pattern = cube.reducePattern("R2 L' F D2 U' F2 B' D' L R2 D2 U' L2 D F L' B' D2 F2 L2 D2 L U R' B2 R' D R' F L' U2 L2 B R2 U' F2 B U L D2 L2 D' U2 R2 F U L2 U' R L U B2 F2 L' U' L R2 U2 R2 F D2 U R' B2 L' D2 L D2 U2 F2 R' D' F' R2 D R2 F R' B' U' D2 L2 F' B2 L' R D' F2 L2 F2 L2 F2 R' F L D2 L' R F2 R' L2 U D' U L' R' U' D B L D2 F L' B' D R' F2")
    print(pattern)
    cube.scramble(pattern)
    start = time.time()
    solved = solver(cube)
    print(solved)
    print(f"len: {len(solved.split(' '))}")
    end = time.time()
    print(f"Time elapsed: {end - start}")
    #cube.printCube()

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


# L2 R B2 D F F F2 B' F R L' U D' D L2 D' U B2 D2 R' R' F2 R2 F2 B D2 D2 F F D' R B L2 U' B U' D B' D' F' B B F' U2 B' R2 D' B2 R' D B2 F B' F2 U' R' R2 L' U L L2 U L' D L' L B' F2 L' U2 D' L2 R U2 B2 R F' F' D R U L' L' D' L2 U2 B D' D2 L' B L U2 D' R' R2 D' L2 B2 F2 L U2 R B U R' B U' F2 U U D' F' L' R' R R' F2 L R2 L2 U U2 L U' D F2 R' B2 R U2 D U' R2 F' R R' U' D2 R2 L' B' U' D D2 F2 F' U' L F' R' F2 B' D2 U'