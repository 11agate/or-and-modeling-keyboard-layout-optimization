set Position;

set Block;  # 1-10
param BlockKeyNum{Block};
param BlockCost{Block, Block};

set Key;       # a-z
set UsingKeys within {Key, Key};

param KeyMove{UsingKeys};
param PositionCost{Position, Position};

var x {Key, Block} binary;

minimize COST:
   sum {(ki, kj) in UsingKeys, bi in Block, bj in Block}
         x[ki, bi] * x[kj, bj] * BlockCost[bi, bj] * KeyMove[ki, kj];

subject to ValidationBlock{bi in Block}:
   sum {kj in Key} x[kj, bi] = BlockKeyNum[bi];

subject to ValidationKey{ki in Key}:
   sum {bj in Block} x[ki, bj] = 1;
