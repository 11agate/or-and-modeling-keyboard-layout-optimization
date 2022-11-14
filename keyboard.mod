set Position;  # A-Z
set Key;
param KeyMove{Key, Key} default 0;
param PositionCost{Position, Position};

var x {Position, Key} binary;

minimize COST:
   sum {i in Key, j in Key, pi in Position, pj in Position}
      x[pi, i] * x[pj, j] * PositionCost[pi, pj] * KeyMove[i, j];

subject to KEYVALIDATION1{i in Position}:
   sum {j in Key} x[i, j] = 1;

subject to KEYVALIDATION2{i in Key}:
   sum {j in Position} x[j, i] = 1;
 