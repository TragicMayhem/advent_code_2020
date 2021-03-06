import sys

# https://adventofcode.com/2016/day/2

print("Advent of Code 2016 - Day 2 part 2")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'  # Code 5DB3
filename = 'input.txt'  # Code C1A88

keypad_layout1 = [[1,2,3],[4,5,6],[7,8,9]]
keypad_layout2 = [
  [None, None, None, None, None, None, None],
  [None, None, None, 1, None, None, None],
  [None, None, 2, 3, 4, None, None],
  [None, 5, 6, 7, 8, 9, None],
  [None, None, 'A', 'B', 'C', None, None],
  [None, None, None, 'D', None, None, None],
  [None, None, None, None, None, None, None]]

max_grid_rows = len(keypad_layout2)   
max_grid_cols = len(keypad_layout2[0])   

pos_ud = 3
pos_lr = 1
pos = [pos_ud, pos_lr]

code = []


def convert(ch):
  '''
    Convert character (ch) to direction +ve down or right, -ve up or left
  '''
  if ch == 'D' or ch == 'R': return 1
  if ch == 'U' or ch == 'L': return -1
  return 0


with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')  # Read file make list bu splitting on new line \n
  data = [[char for char in d] for d in data]
  
  # print(data)

  for line in data:
    print()
    # print(line)
    print("Number of instructions:", len(line))

    for char in line:
      # print('START:', ' pos ', pos_ud, pos_lr, 'Instr:', char, convert(char) )
      change = convert(char)
      curr_lr, curr_ud = pos_lr, pos_ud 

      if char == 'D':
        pos_ud += change
      elif char == 'R':  
        pos_lr += change
      elif char == 'U':
        pos_ud += change
      elif char == 'L':
        pos_lr += change
      
      if  keypad_layout2[pos_ud][pos_lr] == None:  # edge 
          pos_ud = curr_ud
          pos_lr = curr_lr

      # print('END:', '   pos ', pos_ud, pos_lr, "Number:", keypad_layout2[pos_ud][pos_lr])
    
    code.append(keypad_layout2[pos_ud][pos_lr])
    print('FINAL NUMBER:', keypad_layout2[pos_ud][pos_lr])
  
  print()
  print("Code:", ''.join(str(c) for c in code))