Simulator of a 5 stage MIPS pipeline that works with a subset of MIPS instructions and outputs the instructions to be scheduled.

Example:

Input:


ADD R1, R2, R3

MUL R4, R1, R2

LW R3, 0(R5)

SUB R6, R2, R4

SW R7, 0(R4)


Output:


['ADD', 'R1,', 'R2,', 'R3']

[ MUL ,  R4, , L 3 [ R1, ],  R2 ]

['LW', 'R3,', '0(R5)']

[ SUB ,  R6, ,  R2, , L 4 [ R4 ]]

['SW', 'R7,', '0(R4)']

