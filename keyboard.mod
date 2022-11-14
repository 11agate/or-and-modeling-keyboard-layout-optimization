set POSITION;  # A-Z
set KEY;
param charset{KEY, KEY} default 0;
param COSTMAP{POSITION, POSITION};

var x {POSITION, KEY} binary;

minimize COST:
   sum {i in KEY, j in KEY, pi in POSITION, pj in POSITION}
      x[pi, i] * x[pj, j] * COSTMAP[pi, pj] * charset[i, j];

subject to KEYVALIDATION1{i in POSITION}:
   sum {j in KEY} x[i, j] = 1;

subject to KEYVALIDATION2{i in KEY}:
   sum {j in POSITION} x[j, i] = 1;
 
