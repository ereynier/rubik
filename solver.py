from cube import Cube
from tree import TreeCube

def rotate(cube, s):
    faces = {"F" : cube.FRONT, "R": cube.RIGHT, "U": cube.UP, "B": cube.BACK, "L": cube.LEFT, "D": cube.DOWN}
    moves = s.split()
    for move in moves:
        if len(move) > 2 or not move[0] in faces or (len(move) == 2 and (move[1] != "2" and move[1] != "'")):
            print(f"{move} not existing")
            return
        else:
            if len(move) == 2:
                if move[1] == "'":
                    faces[move[0]](True)
                elif move[1] == "2":
                    faces[move[0]]()
                    faces[move[0]]()
            else:
                faces[move[0]]()
        pattern.append(move)
    return (cube)    

def exploration(cube, allowed, func, **kwargs):
    cube1 = Cube()
    cube1.copy(cube)
    tree = TreeCube(cube1, allowed=allowed)
    return(tree.search(func, **kwargs))

def badEdges(sticker, sticker2):
    if sticker[0] == "L" or sticker[0] == "R" or ((sticker[0] == "F" or sticker[0] == "B") and (sticker2[0] == "U" or sticker2[0] == "D")):
        return (1)
    return (0)

def eoDetection(cube):
    bad_edges = {}
    #U face edges
    bad_edges["u1"] = badEdges(cube.face_up.item(1), cube.face_back.item(1))
    bad_edges["u3"] = badEdges(cube.face_up.item(3), cube.face_left.item(1))
    bad_edges["u5"] = badEdges(cube.face_up.item(5), cube.face_right.item(1))
    bad_edges["u7"] = badEdges(cube.face_up.item(7), cube.face_front.item(1))

    #D face edges
    bad_edges["d1"] = badEdges(cube.face_down.item(1), cube.face_front.item(7))
    bad_edges["d3"] = badEdges(cube.face_down.item(3), cube.face_left.item(7))
    bad_edges["d5"] = badEdges(cube.face_down.item(5), cube.face_right.item(7))
    bad_edges["d7"] = badEdges(cube.face_down.item(7), cube.face_back.item(7))

    #F E-slice edges
    bad_edges["f3"] = badEdges(cube.face_front.item(3), cube.face_left.item(5))
    bad_edges["f5"] = badEdges(cube.face_front.item(5), cube.face_right.item(3))

    #B E-slice edges
    bad_edges["b3"] = badEdges(cube.face_back.item(3), cube.face_right.item(5))
    bad_edges["b5"] = badEdges(cube.face_back.item(5), cube.face_left.item(3))

    #print(f"bad edges: {sum(bad_edges.values())}")
    return (bad_edges)


def edgeOrienting(cube, bad_edges):
    bad = [k for k, v in bad_edges.items() if v == 1]
    if len(bad) == 0:
        return (cube)

    if bad == ['u1', 'u7', 'd1', 'd7'] or bad == ['u3', 'u5', 'd3', 'd5']:
        cube = rotate(cube, "U") 
    elif len(bad) > 2:
        # only use <R, U, L, D, F2, B2>
        # exploration to 4 bad edge on F or B
        m = exploration(cube, ["R", "U", "L", "D", "F2", "B2"], badEdgesOnFB, nb=4)
        cube = rotate(cube, m)
        if badEdgesOnFB(cube, 4, True)[0] == 4:
            cube = rotate(cube, "F")
        else:
            cube = rotate(cube, "B")
    else:
        # only use <R, U, L, D, F2, B2>
        # exploration to 1 bad edges on F or B
        m = exploration(cube, ["R", "U", "L", "D", "F2", "B2"], badEdgesOnFB, nb=1)
        cube = rotate(cube, m)
        if badEdgesOnFB(cube, 1, True)[0] == 1:
            cube = rotate(cube, "F")
        else:
            cube = rotate(cube, "B")
    return (cube)

def badEdgesOnFB(cube, nb, get=False):
    bad_edges = eoDetection(cube)
    bad = [k for k, v in bad_edges.items() if v == 1]
    f = [k[0] for k in bad].count("f") + bad_edges["u7"] + bad_edges["d1"]
    b = [k[0] for k in bad].count("b") + bad_edges["u1"] + bad_edges["d7"]
    if get:
        return ((f, b))
    else:
        if f == nb or b == nb:
            return (True)
    return (False)

##########################################################################################################

def badEdges2(sticker, sticker2):
    if sticker[0] == "B" or sticker[0] == "F" or ((sticker[0] == "L" or sticker[0] == "R") and (sticker2[0] == "U" or sticker2[0] == "D")):
        return (1)
    return (0)

def eoDetection2(cube):
    bad_edges = {}
    #U face edges
    bad_edges["u1"] = badEdges2(cube.face_up.item(1), cube.face_back.item(1))
    bad_edges["u3"] = badEdges2(cube.face_up.item(3), cube.face_left.item(1))
    bad_edges["u5"] = badEdges2(cube.face_up.item(5), cube.face_right.item(1))
    bad_edges["u7"] = badEdges2(cube.face_up.item(7), cube.face_front.item(1))

    #D face edges
    bad_edges["d1"] = badEdges2(cube.face_down.item(1), cube.face_front.item(7))
    bad_edges["d3"] = badEdges2(cube.face_down.item(3), cube.face_left.item(7))
    bad_edges["d5"] = badEdges2(cube.face_down.item(5), cube.face_right.item(7))
    bad_edges["d7"] = badEdges2(cube.face_down.item(7), cube.face_back.item(7))

    #F E-slice edges
    bad_edges["r3"] = badEdges2(cube.face_right.item(3), cube.face_front.item(5))
    bad_edges["r5"] = badEdges2(cube.face_right.item(5), cube.face_back.item(3))

    #B E-slice edges
    bad_edges["l3"] = badEdges2(cube.face_left.item(3), cube.face_back.item(5))
    bad_edges["l5"] = badEdges2(cube.face_left.item(5), cube.face_front.item(3))

    #print(f"bad edges: {sum(bad_edges.values())}")
    return (bad_edges)


def edgeOrienting2(cube, bad_edges):
    bad = [k for k, v in bad_edges.items() if v == 1]
    if len(bad) == 0:
        return (cube)

    if bad == ['u1', 'u7', 'd1', 'd7'] or bad == ['u3', 'u5', 'd3', 'd5']:
        cube = rotate(cube, "U")
    if len(bad) > 2:
        # only use <R2, U, L2, D, F, B>
        # exploration to 4 bad edge on R or L
        m = exploration(cube, ["R2", "U", "L2", "D", "F", "B"], badEdgesOnRL, nb=4)
        cube = rotate(cube, m)
        if badEdgesOnRL(cube, 4, True)[0] == 4:
            cube = rotate(cube, "R")
        else:
            cube = rotate(cube, "L")
    else:
        # only use <R2, U, L2, D, F, B>
        # exploration to 1 bad edges on R or L
        m = exploration(cube, ["R2", "U", "L2", "D", "F", "B"], badEdgesOnRL, nb=1)
        cube = rotate(cube, m)
        if badEdgesOnRL(cube, 1, True)[0] == 1:
            cube = rotate(cube, "R")
        else:
            cube = rotate(cube, "L")
    return (cube)

def badEdgesOnRL(cube, nb, get=False):
    bad_edges = eoDetection2(cube)
    bad = [k for k, v in bad_edges.items() if v == 1]
    r = [k[0] for k in bad].count("r") + bad_edges["u5"] + bad_edges["d5"]
    l = [k[0] for k in bad].count("l") + bad_edges["u3"] + bad_edges["d3"]
    if get:
        return ((r, l))
    else:
        if r == nb or l == nb:
            return (True)
    return (False)

#---------------------------------------------------------------------------------------------------------


def isUDColor(cube, items=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
    for i in items:
        if cube.face_up.item(i)[0] != 'U' and cube.face_up.item(i)[0] != 'D':
            return (False)
    for i in items:
        if cube.face_down.item(i)[0] != 'U' and cube.face_down.item(i)[0] != 'D':
            return(False)
    return (True)


def tweakCOAlgo(algo: str, face_up):
    new_algo = ""
    if face_up == "U":
        new_algo = algo
    elif face_up == "D":
        new_algo = algo.replace('U', 'temp').replace('B', 'F').replace('D', 'U').replace('F', 'B').replace('temp', 'D')
    elif face_up == "F":
        new_algo = algo.replace('U', 'temp').replace('B', 'U').replace('D', 'B').replace('F', 'D').replace('temp', 'F')
    elif face_up == "B":
        new_algo = algo.replace('U', 'temp').replace('B', 'D').replace('D', 'F').replace('F', 'U').replace('temp', 'B')
    elif face_up == "R":
        new_algo = algo.replace('U', 'temp').replace('L', 'U').replace('D', 'L').replace('R', 'D').replace('temp', 'R')
    elif face_up == "L":
        new_algo = algo.replace('U', 'temp').replace('L', 'D').replace('D', 'R').replace('R', 'U').replace('temp', 'L')
    return (new_algo)

def countBadCorner(cube, f):
    opposit = {"F" : "B", "R": "L", "U": "D", "B": "F", "L": "R", "D": "U"}
    bad = 0
    for i in [0, 2, 6, 8]:
        if cube.sides()[f].item(i)[0] != f and cube.sides()[f].item(i)[0] != opposit[f]:
            bad += 1
    return (bad)

def isGoodColor(color, f):
    opposit = {"F" : "B", "R": "L", "U": "D", "B": "F", "L": "R", "D": "U"}
    if color == f or color == opposit[f]:
        return (True)
    return (False)

def cornerDirection():
    return

def twoCorners(cube, f):
    
    return ()

def UDCornersOrientation(cube):

    for f in ["F", "R", "U", "B", "L", "D"]:
        # count bad color
        # while >= 2 turn to known pos, if not known found -> next face
        while countBadCorner(cube, f) >= 2:
            m = twoCorners(cube, f)
            if m == 0:
                break
            rotate(cube, m)
            # exec algo
        pass
    return (cube)

def solver(cube):
    global pattern
    pattern = []
    # Step 1 + 2.1
    while isUDColor(cube, [1, 3, 5, 7]) == False:
        bad_edges = eoDetection(cube)
        while sum(bad_edges.values()) > 0:
            cube = edgeOrienting(cube ,bad_edges)
            bad_edges = eoDetection(cube)
        if isUDColor(cube, [1, 3, 5, 7]):
            break
        bad_edges = eoDetection2(cube)
        while sum(bad_edges.values()) > 0:
            cube = edgeOrienting2(cube ,bad_edges)
            bad_edges = eoDetection2(cube)
    print("2 axis EO done")
    # Step 2.2
    #cube = UDCornersOrientation(cube)
    return (cube.reducePattern(" ".join(pattern)))

from random import randint
from time import time
def main():
    cube = Cube()
    scramble = "L2 F R2 B U2 B' F2 U2 F L2 D' L' B' R' F D' F U2 B2 B'"
    cube.scramble(scramble)
    cube.printCube()
    solver(cube)

    timer = []
    for i in range(2000):
        cube.reset()
        scramble = cube.random(randint(20, 200))
        cube.scramble(scramble)
        print(scramble)
        print(f"cube : {i}")
        start = time()
        solver(cube)
        end = time()
        timer.append(end - start)
    print(f"time avg: {sum(timer) / len(timer)}")
    print(f"max time: {max(timer)}")

    return


if __name__ == "__main__":
    main()



# https://www.speedsolving.com/wiki/index.php/Thistlethwaite%27s_algorithm
# https://math.stackexchange.com/questions/1362471/rubiks-cube-thistlethwaite-four-phase-algorithm


# Phase 1 <U,D,L,R,F2,B2> F and B to switch BAD to GOOD and GOOD to BAD
# EO (edge orientation) : all edge to good pos, (ZZ method) 7 moves worst case
# https://www.speedsolving.com/wiki/index.php/Edge_Orientation#ZZ



# Phase 2 <U,D,L,R,F2,B2> 
# Corner orientation :  10 moves worst case
# 2.1 placement of U/D edges in U/D faces (whatever if it's U or D just place it on U or D)
# https://www.speedsolving.com/wiki/index.php/Edge_Orientation#2-axis_EO

# 2.2 Corner Orientation, and placement
# https://www.speedsolving.com/wiki/index.php/Corner_Orientation

# Phase 3 <U,D,L2,R2,F2,B2>
# Every colors are on there face or the opposit, 13 moves worst case 
# 3.1 Corners
# 3.2 Edges


# Phase 4 <U2,D2,L2,R2,F2,B2> 
# Final resolution : 15 moves worst case





# F2 D2 R' F2 R D2 F2 R2 U' F D R2 B2 L' F' R D' U2 F R2