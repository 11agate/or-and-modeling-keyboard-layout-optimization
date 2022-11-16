set Position;

set Block;  # 1-10
param BlockKeyNum{Block};
param BlockCost{Block, Block};

set PositionsInBlock{Block};

set Key;       # a-z
set UsingKeys within {Key, Key};

param KeyMove{UsingKeys};
param PositionCost{Position, Position};

var x {Key, Block} binary;
var y {Key, Position} binary;

minimize COST:
   sum {(ki, kj) in UsingKeys, bi in Block, bj in Block}
         x[ki, bi] * x[kj, bj] * BlockCost[bi, bj] * KeyMove[ki, kj];

minimize COSTY:
   sum {(ki, kj) in UsingKeys, pi in Position, pj in Position}
      y[ki, pi] * y[kj, pj] * PositionCost[pi, pj] * KeyMove[ki, kj];

subject to ValidationBlock{bi in Block}:
   sum {kj in Key} x[kj, bi] = BlockKeyNum[bi];

subject to ValidationKey{ki in Key}:
   sum {bj in Block} x[ki, bj] = 1;

subject to ValidationPosition{block in Block, key in Key}:
   sum {p in PositionsInBlock[block]} y[key, p] = x[key, block];
