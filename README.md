# rubik
## 42 project - rubik's cube solver in 20 movments or less
---
https://www.speedsolving.com/wiki/index.php/Thistlethwaite%27s_algorithm
https://math.stackexchange.com/questions/1362471/rubiks-cube-thistlethwaite-four-phase-algorithm


## Phase 1 <U,D,L,R,F2,B2> F and B to switch BAD to GOOD and GOOD to BAD
EO (edge orientation) : all edge to good pos, (ZZ method) 7 moves worst case
https://www.speedsolving.com/wiki/index.php/Edge_Orientation#ZZ



## Phase 2 <U,D,L,R,F2,B2> 
Corner orientation :  10 moves worst case
### 2.1 placement of U/D edges in U/D faces (whatever if it's U or D just place it on U or D)
https://www.speedsolving.com/wiki/index.php/Edge_Orientation#2-axis_EO

## 2.2 Corner Orientation
https://www.cuberoot.me/dr-trigger/

## Phase 3 <U,D,L2,R2,F2,B2>
Every colors are on there face or the opposit, 13 moves worst case 
3.1 Corners
3.2 Edges


## Phase 4 <U2,D2,L2,R2,F2,B2> 
Final resolution : 15 moves worst case
