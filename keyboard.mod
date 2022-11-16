set Position;  # A-Z
set Key;       # a-z
set UsingKeys within {Key, Key};

param KeyMove{UsingKeys};
param PositionCost{Position, Position};

var x {Position, Key} binary;

minimize COST:
   sum {(ki, kj) in UsingKeys, pi in Position, pj in Position}
         x[pi, ki] * x[pj, kj] * PositionCost[pi, pj] * KeyMove[ki, kj];

subject to ValidationPosition{pi in Position}:
   sum {kj in Key} x[pi, kj] = 1;

subject to ValidationKey{ki in Key}:
   sum {pj in Position} x[pj, ki] = 1;
 