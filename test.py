# import multiprocessing as mp
# from cube import Cube
# from tree import TreeCube


# def isUDColor(cube, items=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
#     for i in items:
#         if cube.face_up.item(i)[0] != 'U' and cube.face_up.item(i)[0] != 'D':
#             return (False)
#     for i in items:
#         if cube.face_down.item(i)[0] != 'U' and cube.face_down.item(i)[0] != 'D':
#             return(False)
#     return (True)


# def find(cube, i, return_dict, run):
#     cube1 = Cube()
#     cube1.copy(cube)
#     if i == 1:
#         cube1.reset()
#         cube1.BACK()
#     tree = TreeCube(cube1, run, allowed=["F", "R", "B", "L", "U", "D"])
#     m = tree.search(isUDColor)
#     print(m)
#     return_dict[i] = f"Found: {i}, start: {m}"
#     run.clear() # Stop running.


# def search():
#     cube = Cube()
#     cube.scramble(cube.reducePattern(cube.random(40)))
#     processes = []
#     manager = mp.Manager()
#     return_code = manager.dict()
#     run = manager.Event()
#     run.set()  # We should keep running.
#     for i in range(2):
#         process = mp.Process(
#             target=find, args=(cube, i, return_code, run)
#         )
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()
#     print(return_code)

# if __name__ == '__main__':
#     search()


a = {'start_U': 'U D', 'start_': ' R2', 'start_D': 'D F2', 'start_F2': 'F2 U', 'start_R2': 'R2 U', 'start_L2': 'L2 U', "start_U'": "U' D", 'start_U2': 'U2 D', "start_D'": "D' F2", 'start_D2': 'D2 F2'}
print(" ".join(sorted([x.split() for x in a.values() if x is not None], key=len)[0]))