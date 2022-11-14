set Position;  # A-Z
set Key;       # a-z

param KeyMove{Key, Key} default 0;
param PositionCost{Position, Position};

var x {Position, Key} binary;

minimize COST:
   sum {i in Key, j in Key, pi in Position, pj in Position}
      x[pi, i] * x[pj, j] * PositionCost[pi, pj] * KeyMove[i, j];

subject to ValidationPosition{i in Position}:
   sum {j in Key} x[i, j] = 1;

subject to ValidationKey{i in Key}:
   sum {j in Position} x[j, i] = 1;
 