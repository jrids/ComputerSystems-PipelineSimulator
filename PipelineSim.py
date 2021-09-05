# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:59:18 2021

@author: Johri
"""

class Ins(object):

	def __init__(self):
		self.opcode = 'NOP'
		self.str = 'NULL'
		self.stage = 'NULL'
		self.scr1 = 'NULL'
		self.scr2 = 'NULL'
		self.dest = 'NULL'

	def __init__(self, opcode, scr1, scr2, dest,instr,x):
		self.opcode = opcode
		self.instr = instr
		self.stage = x
		self.scr1 = scr1
		self.scr2 = scr2
		self.dest = dest
        
        
import re

registers = [0] * 32
instructionsList = []
infile = open('Input2.txt','r');

def parse_ins(ins_string):
	instruction = 'NULL'
	if ins_string[0] == 'LW':
		a = ins_string[2].split('(')
		dest = ins_string[1]
		scr2 = 'NULL'
		scr1 = re.sub("\)", "", a[1])
		instruction = Ins('LW', scr1, scr2, dest,ins_string,1)

	elif ins_string[0] == 'SW':
		a = ins_string[2].split('(')
		dest = a[1][0:2]
		scr1 = ins_string[1]
		scr2 = 'NULL'
		instruction = Ins('SW', scr1, scr2, dest, ins_string,1)

	elif ins_string[0] == 'ADD':
		dest = ins_string[1]
		scr1 = ins_string[2]
		scr2 = ins_string[3]
		instruction = Ins('ADD', scr1, scr2, dest, ins_string,1)

	elif ins_string[0] == 'SUB':
		dest = ins_string[1]
		scr1 = ins_string[2]
		scr2 = ins_string[3]
		instruction = Ins('SUB', scr1, scr2, dest, ins_string,1)

	elif ins_string[0] == 'MUL':
		dest = ins_string[1]
		scr1 = ins_string[2]
		scr2 = ins_string[3]
		instruction = Ins('MUL', scr1, scr2, dest, ins_string,1)

# 	elif ins_string[0] == 'JNZ':
# 		scr1 = ins_string[1]
# 		branch_ref = ins_string[2]
# 		instruction = Ins('JNZ', scr1, 'NULL', 'NULL', ins_string,1)

# 	elif ins_string[0] == 'BEQ':
# 		scr1 = ins_string[1]
# 		src2 = ins_string[2]
# 		instruction = Ins('BEQ', scr1, src2, 'NULL', ins_string,1)

	return instruction


def IF(instruction):
    if(instruction.dest != 'NULL'):
        num = 0
        for c in instruction.dest:
            if c.isdigit():
                num = num + int(c)
            registers[num]=1
            #print(instruction.dest,'register',num,registers[num])
            
    
    if(instructionsList[0]==instruction):
        print(instruction.instr)
        return
    flag1=0        
    if(instruction.scr1 !='NULL'):
        num = 0
        for c in instruction.scr1:
            if c.isdigit():
                num = num + int(c)
        #if(registers[num]==0):
         #   flag1=-1
        # if(registers[num]==1 or registers[num]==2):
        #     flag1=1
        if(registers[num]!=0):
            flag1=registers[num]
            
    flag2=0        
    if(instruction.scr2 !='NULL'):
        #print(instruction.opcode , ' ', flag2)
        num = 0
        for c in instruction.scr2:
            if c.isdigit():
                num = num + int(c)
        #if(registers[num]==0):
         #   flag2=-1
        # if(registers[num]==1 or registers[num]==2):
        #     flag2=1
        if(registers[num]!=0):
            flag2=registers[num]
            #print(instruction.opcode , ' ', flag2)
    
    if(instruction.opcode=='ADD' or instruction.opcode=='SUB' or instruction.opcode=='MUL'):
        index=instructionsList.index(instruction)
        if(instructionsList[index-1].opcode=='LW' or instructionsList[index-1].opcode=='SW'):
            if(flag1==0 and flag2==0 or flag1>4 or flag2>4):
                print(instruction.instr)
            
            elif(flag1>=3):
                    print('[',instruction.opcode,', ', instruction.dest, ', L',flag1+1,'[', instruction.scr1, '], ', instruction.scr2,']')
            elif(flag2>=3):
                    print('[',instruction.opcode,', ', instruction.dest, ', ', instruction.scr1, ', L',flag2+1,'[', instruction.scr2 ,']]')
    
            else:
                print('delay')
                if(flag1>0 and flag1<3):
                    print('[',instruction.opcode,', ', instruction.dest, ', [L4]', instruction.scr1, instruction.scr2,']')
                elif(flag2>0 and flag2<3):
                    print('[',instruction.opcode,', ', instruction.dest, ', ', instruction.scr1, ', [L4]', instruction.scr2 ,']')
        elif(flag1==0 and flag2==0 or flag1>=4 or flag2>=4):
            print(instruction.instr)
        elif(flag1==1 or flag2==1):
            #print('flag 1 and 2', flag1, flag2)
            print('delay')
            print(instruction.instr)
        elif(flag1>=2):
            print('[',instruction.opcode,', ', instruction.dest, ', L',flag1+1,'[', instruction.scr1, '], ', instruction.scr2,']')
        elif(flag2>=2):
            print('[',instruction.opcode,', ', instruction.dest, ', ', instruction.scr1, ', L',flag2+1,'[', instruction.scr2 ,']]')
    else:
        if(flag1==0 and flag2==0 or flag1>=4 or flag2>=4):
            print(instruction.instr)
        elif(flag1==1 or flag2==1):
        #print('flag 1 and 2', flag1, flag2)
            print('delay')
            print(instruction.instr)
        elif(flag1>=2):
            print('[',instruction.opcode,', ', instruction.dest, ', L',flag1+1,'[', instruction.scr1, '], ', instruction.scr2,']')
        elif(flag2>=2):
            print('[',instruction.opcode,', ', instruction.dest, ', ', instruction.scr1, ', L',flag2+1,'[', instruction.scr2 ,']]')
    
    #RR(instruction,st)
    
    
def nextStep(instruc):
    if(instruc.stage ==1):
        IF(instruc)
    elif(instruc.stage>5):
        return
    else:
        if(instruc.dest != 'NULL'):
            num = 0
            for c in instruc.dest:
                if c.isdigit():
                    num = num + int(c)
            registers[num]=instruc.stage
            #print(instruc.dest,'register',num,registers[num])
    instruc.stage = instruc.stage+1
    
    
y=0
for line in infile:
    print(line.strip())
    y=y+1
    i = parse_ins(line.strip().split())
    instructionsList.append(i)
    #print(i)

print('Output:')
r=1
for i in range(y):
    m = r
    for x in instructionsList:
        #print('print',x,m)
        #print(registers[1],'reg1')
        nextStep(x)
        m=m-1
        if m==0:
            r=r+1
            break
        