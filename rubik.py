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
    pattern = cube.reducePattern("L2 R B2 D F F F2 B' F R L' U D' D L2 D' U B2 D2 R' R' F2 R2 F2 B D2 D2 F F D' R B L2 U' B U' D B' D' F' B B F' U2 B' R2 D' B2 R' D B2 F B' F2 U' R' R2 L' U L L2 U L' D L' L B' F2 L' U2 D' L2 R U2 B2 R F' F' D R U L' L' D' L2 U2 B D' D2 L' B L U2 D' R' R2 D' L2 B2 F2 L U2 R B U R' B U' F2 U U D' F' L' R' R R' F2 L R2 L2 U U2 L U' D F2 R' B2 R U2 D U' R2 F' R R' U' D2 R2 L' B' U' D D2 F2 F' U' L F' R' F2 B' D2 U'")
    print(pattern)
    cube.scramble(pattern)
    start = time.time()
    solved = solver(cube)
    print(solved)
    print(f"len: {len(solved.split(' '))}")
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


# L2 R B2 D F F F2 B' F R L' U D' D L2 D' U B2 D2 R' R' F2 R2 F2 B D2 D2 F F D' R B L2 U' B U' D B' D' F' B B F' U2 B' R2 D' B2 R' D B2 F B' F2 U' R' R2 L' U L L2 U L' D L' L B' F2 L' U2 D' L2 R U2 B2 R F' F' D R U L' L' D' L2 U2 B D' D2 L' B L U2 D' R' R2 D' L2 B2 F2 L U2 R B U R' B U' F2 U U D' F' L' R' R R' F2 L R2 L2 U U2 L U' D F2 R' B2 R U2 D U' R2 F' R R' U' D2 R2 L' B' U' D D2 F2 F' U' L F' R' F2 B' D2 U'