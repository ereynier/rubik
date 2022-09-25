from cube import Cube


def main():
    cube = Cube()
    cube.printCube()
    cube.scramble("F2 D2 R' F2 R D2 F2 R2 U' F D R2 B2 L' F' R D' U2 F R2")
    #cube.printCube()
    cube.scramble(" ".join("F2 D2 R F2 R' D2 F2 R2 U F' D' R2 B2 L F R' D U2 F' R2".split()[::-1]))
    cube.printCube()
    return


if __name__ == "__main__":
    main()