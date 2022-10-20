from cube import Cube
from solverv2 import solver
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
    #1300 move wirh multiprocerss V
    #pattern = cube.reducePattern("D' R2 F U2 D F U2 L F2 R' F' U L2 B R F' B L' U B F2 D2 B F B2 F' R2 U' D R U B' L2 U2 F2 U2 B' U' F L F' U B2 F2 B R D' R2 L2 D' F B2 L' U L' R' B' F D U' R' L' B D' R' U2 L D L R2 F' U' D' U L U' R' D' L2 R2 U2 B F B2 D' U F' U' L' U L F' U F D' U L' B' D2 R2 B L2 R' F2 R2 L2 D' U2 B2 U' L U' L' B L2 B' D' U F' D' L2 F D B' F")
    #68s without multiprocess V
    #pattern = cube.reducePattern("R' D2 B' F' R U' L' B' F2 L2 U R' U' F2 R D2 B2 F L' R' D2 R2 F' B2 R L2 B2 R2 B2 F2 D' U2 D' L2 F' U' L' R' L2 B2 U B' R' B' L B2 L' D U B' D2 B2 F' B' R L2 D2 L2 R L' U F U R F U L D L D F2 B U F R B2 U2 D' U D2 R2 F2 D R' F D U2 L' R' F' R F D U L2 F' L B U2 L' F' L2 U R2 L2 B R' U' L2 B D' F' L R' F' U' D' L2 D R2 U R' F2 D' L U' D2 B L2 R L2 U R' B")
    #pattern = "D2 B2 L' U D2 L2 U2 R2 B R' B2 R F' D' F2 D' L2 D2 B R' D' R2 D' U' F2 L2 B2 U2 D' U D L2"
    #45s CP V
    #pattern = "B' D2 U2 F D R B F' U2 R2 F2 R2 F2 D' L' R' L2 F' U' B F2 B' F2 R' B2 L' F' R2 U2 B' L2 D R2 F2 B F2 U D2 U' D2 L' D2 L D2 L' U F R U F' D F' R L' B2 D' B2 L2 R F2 L' B U' L R' U2 B F D L2 U L F' L2 B' U2 L2 R B U' D2 F' B F2 U R B' U' D' U2 B' R' B2 R'"
    #89s with searching final edges V
    #pattern = "B' U' F2 U2 D2 F' D' U' F' D R2 D F' L2 B F' U' B U L2 R' F' R F2 B' F D' U2 D2 B R2 B U' D L' U L U2 F U' R2 B F' D L B' U D' B' F' D F2 B2 F' R2 U' L R' B' F' U2 L B U' F B2 R' F' D2 U R B' F2 B2"
    # 86 move with searching final edge V
    #pattern = "B' D2 L R' L2 R U D B2 R D' U' L' F B U D F2 L2 F L' R2 L B2 F2 D' R L D' R B' L R U2 F' D' U D B L B R F B' D2 R' F' B' D'"
    #pattern = "L2 U R L R' B L F2 L2 R D' L2 B2 R' D2 L2 D' R' B L' R F' L U B F U D F' B R2 D2 L2 B2 D B2 U' R F' R2 D' B2 R' L2 F' U D' U' R2 B L D' F2 D' F' U D L' R U D2 B2 L2 U D' L2"
    #pattern = "L R2 L R L' F2 L' F2 U' D2 R2 L D B' R2 U2 B' U2 B' D B2 U D2 R' L' R L2 R' U2 R' D U2 R' U D2 U2 L B' D R' B' R2 B' F U' B' U D2 B R' L' U L' D2 U' B' F U L2 D' R2 L' F' L R' F2 D U' B F2 B2 L' R' F2"
    #pattern = "L' U2 F R L' B R' D2 F L B2 U2 L' U L2 D L2 R U2 B' R' U2 L2 F' D' L2 F B2 U' F B2 F' B' U2 L2 R2 F2 B U' L2 R' L2 B2 U' B2 R L2 D' F2 U' R' B2 F2 R U' F2 B2 D2 R L B' L B' L F2 U2 F B' R B' F2 L2 F D' R2 L D2 L R2 F' B' D' R2 L2 U' F' D' L2 F' R2 B' L' F2 B D2 B' F2 U2 D B2 D2 F' R2 B F2 R2 D2 R' L R U' D2 F' D2 B2 U' R' F2 L U' D' F' R2 D' R2 B U' R' L' B F2 U L' U L U L2 U2 B' U' R D U R2 B F2 L' F2 U2 L R F D U' F U B' U2 F"
    #pattern = "B2 R' B' F2 U2 F' R F' B F2 L2 U2 B' U' R2 B2 F' L' R2 B' U2 R B2 F L2 B' F' B' F B F D R' L' D L' D' B' L F R' B2 F L2 R F R2 F B' L' R B U2 D' R' B L B D' R2 F' U2 D B' U' L2 R2 U' L D2 F2 U' B U B2 L' U' L' D2 U2 F L2 D' B F2 B2 L D F' L' R2 F2 D' U2 L2 R B D F' U F L D' U' R' D U R' L' D F' U' F R B' L2 R F2 B L2 B' U' F D2 R2 B' D' B' L2 R' D B' R'"
    #pattern = "R2 B' L' D' B' R' D R2 D2 L2 U2 R U2 R' B2 L' F B2 L U' L2 R2 D F D' F' R2 B F L2 D R' F R' U2 L2 U' L2 B' D U' L' U' L' R2 L B F' B U2 F B2 F U2 L2 U' B' R' L B' D B' U2 L U2 F' D2 B D L2 F2 U2 F U' D2 F2 D2 F2 L F D' B' D' B' U B2 R2 L2 D F' D2 F D' B' D2 L R' L R2 F R' F' D' R' D F' U2 L R2 F U D' R2 D2 U F' R F' R F R2 U"
    #99 move V
    #pattern = "D' U' F L R U F L2 R' B2 F' L' R F2 D' B R2 U2 F U2 B2 F' B' F' B U' R' U2 F2 U2 D' R' L R' L F' L' B2 U R D2 F U D R2 F' R F U2 L2 U B U' R F L' B2 F2 U R F2 L' R2 B D B' R2 B D' L2 D2 B2 F' U2 D2 L' B D L2 R D' B' U2 L B2 F2 U R B' D' U F2 D2 B2 R U2 D' R L F2 B' R F2 L D B U2 L' B' U' L' D2 R2 U2 D' L2 B' R2 F L' F' R"
    # 104 moves V
    #pattern = "R' L2 D2 R' B2 U F2 U L2 R' U' R2 L2 D' U' R' B2 L F R F D U D2 U2 L F R2 F2 R' D2 L2 D' F2 L2 B2 F' B R2 L' R2 U' B2 L U' L2 B' R2 F' D' B' L2 R F U2 D F' B F' U2 B R U' B' F' B' L' D2 U' R' U' D B2 F' U' D' L F2 D' L' B2 U' L2 D2 B' D B2 L2 B F' R2 L B2 R' D' B2 L2 D B' U D' B2 U2 L2 B L2 U F2 R2 B L' D L' B U R2 B2 D' R' L D' B' R' L' R B' R2 L B' R' D2 L2 B2 L' U' L D2 U2 L B D2 L2 R"
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