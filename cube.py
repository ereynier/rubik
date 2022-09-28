import numpy as np
from random import randint

#                      U
#              [['U1' 'U2' 'U3']]
#              [['U4' 'U5' 'U6']]
#              [['U7' 'U8' 'U9']]
#         L                  F                  R                  B
# [['L1' 'L2' 'L3']] [['F1' 'F2' 'F3']] [['R1' 'R2' 'R3']] [['B1' 'B2' 'B3']]                              <-┐  
# [['L4' 'L5' 'L6']] [['F4' 'F5' 'F6']] [['R4' 'R5' 'R6']] [['B4' 'B5' 'B6']]                  rot90 1 ->    |
# [['L7' 'L8' 'L9']] [['F7' 'F8' 'F9']] [['R7' 'R8' 'R9']] [['B7' 'B8' 'B9']] 
#                      D
#              [['D1' 'D2' 'D3']]
#              [['D4' 'D5' 'D6']]
#              [['D7' 'D8' 'D9']]

class Cube:
    def __init__(self):
        self.reset()

    def reset(self):
        self.face_left = np.matrix([["L1", "L2", "L3"], ["L4", "L5", "L6"], ["L7", "L8", "L9"]])
        self.face_right = np.matrix([["R1", "R2", "R3"], ["R4", "R5", "R6"], ["R7", "R8", "R9"]])
        self.face_front = np.matrix([["F1", "F2", "F3"], ["F4", "F5", "F6"], ["F7", "F8", "F9"]])
        self.face_up = np.matrix([["U1", "U2", "U3"], ["U4", "U5", "U6"], ["U7", "U8", "U9"]])
        self.face_down = np.matrix([["D1", "D2", "D3"], ["D4", "D5", "D6"], ["D7", "D8", "D9"]])
        self.face_back = np.matrix([["B1", "B2", "B3"], ["B4", "B5", "B6"], ["B7", "B8", "B9"]])

    def printCube(self):
        a = f"""
                             U
                     {self.face_up[0]}
                     {self.face_up[1]}
                     {self.face_up[2]}
                L                  F                  R                  B
        {self.face_left[0]} {self.face_front[0]} {self.face_right[0]} {self.face_back[0]}
        {self.face_left[1]} {self.face_front[1]} {self.face_right[1]} {self.face_back[1]}
        {self.face_left[2]} {self.face_front[2]} {self.face_right[2]} {self.face_back[2]}
                             D
                     {self.face_down[0]}
                     {self.face_down[1]}
                     {self.face_down[2]}
        """
        print(a)
        return

    def primeInvert(self, faces):
        f_tmp = faces[1]
        faces[1] = faces[3]
        faces[3] = f_tmp
        return (faces)

    def UP(self, prime=False):
        face = self.face_up
        faces = [self.face_back, self.face_left, self.face_front, self.face_right]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][0] = faces[i+1][0]
        self.face_up = face
    
    def DOWN(self, prime=False):
        face = self.face_down
        faces = [self.face_back, self.face_right, self.face_front, self.face_left]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][2] = faces[i+1][2]
        self.face_down = face
    
    def RIGHT(self, prime=False):
        face = self.face_right
        faces = [np.rot90(self.face_back, k=2), self.face_up, self.face_front, self.face_down]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][:, 2] = faces[i+1][:, 2]
        self.face_right = face

    def LEFT(self, prime=False):
        face = self.face_left
        faces = [np.rot90(self.face_back, k=2), self.face_down, self.face_front, self.face_up]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][:, 0] = faces[i+1][:, 0]
        self.face_left = face

    def FRONT(self, prime=False):
        face = self.face_front
        faces = [np.rot90(self.face_left, k=2), np.rot90(self.face_down), self.face_right, np.rot90(self.face_up, k=-1)]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][:, 0] = faces[i+1][:, 0]
        self.face_front = face
    
    def BACK(self, prime=False):
        face = self.face_back
        faces = [np.rot90(self.face_left, k=2), np.rot90(self.face_up, k=-1), self.face_right, np.rot90(self.face_down)]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][:, 2] = faces[i+1][:, 2]
        self.face_back = face

    def reverseScramble(self, pattern):
        faces = ["F", "R", "U", "B", "L", "D"]
        moves = pattern.split()
        reversed = []
        l = len(moves)
        for i in range(l):
            move = moves[l - 1 - i]
            if len(move) > 2 or not move[0] in faces or (len(move) == 2 and (move[1] != "2" and move[1] != "'")):
                print(f"{move} not existing")
                return
            if len(move) == 1:
                move = move + "'"
            elif len(move) == 2 and move[1] == "'":
                move = move[0]
            reversed.append(move)
        return(" ".join(reversed))


    def random(self, nb_moves=randint(1, 40)):
        faces = ["F", "R", "U", "B", "L", "D"]
        extras = ["", "'", "2"]
        pattern = ""
        for i in range(nb_moves):
            pattern = pattern + " " + faces[randint(0, 5)] + extras[randint(0, 2)]
        return (pattern)

    def scramble(self, pattern: str):
        faces = {"F" : self.FRONT, "R": self.RIGHT, "U": self.UP, "B": self.BACK, "L": self.LEFT, "D": self.DOWN}
        moves = pattern.split()
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
        return


    def solver():
        pass
    