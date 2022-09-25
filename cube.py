import numpy as np

#                   U
#              [41][42][43]
#              [44][45][46]
#              [47][48][49]
#      L            F            R            B
# [11][12][13] [31][32][33] [21][22][23] [61][62][63]                         <-┐ 
# [14][15][16] [34][35][36] [24][25][26] [64][65][66]             rot90 1 ->    |
# [17][18][19] [37][38][39] [27][28][29] [67][68][69]
#                   D
#              [51][52][53]
#              [54][55][56]
#              [57][58][59]


class Cube:
    def __init__(self):
        self.reset()

    def reset(self):
        self.face_left = np.matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
        self.face_right = np.matrix([[21, 22, 23], [24, 25, 26], [27, 28, 29]])
        self.face_front = np.matrix([[31, 32, 33], [34, 35, 36], [37, 38, 39]])
        self.face_up = np.matrix([[41, 42, 43], [44, 45, 46], [47, 48, 49]])
        self.face_down = np.matrix([[51, 52, 53], [54, 55, 56], [57, 58, 59]])
        self.face_back = np.matrix([[61, 62, 63], [64, 65, 66], [67, 68, 69]])

    def printCube(self):
        a = f"""
                          U
                     {self.face_up[0]}
                     {self.face_up[1]}
                     {self.face_up[2]}
             L            F            R            B
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

    def random(self):
        faces = ["F", "R", "U", "B", "L", "D"]
        extras = ["", "'", "2"]
        return

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

    