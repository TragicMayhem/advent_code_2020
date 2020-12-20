import re

print("Advent of Code 2020 - Day 2 part 2")

# Input file is a list of policy and passwords
# n-m: passwordstring
# How many on the input file are valid with new policy

valid_pwd = 0

#handle = open('test.txt', 'r')
handle = open('input.txt', 'r')
lines = handle.readlines()
handle.close()

for line in lines:
  chk = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line)
  lower, upper, letter, password = chk.group(1, 2, 3, 4)
  # print(lower, upper, letter, password)
  lower = int(lower)
  upper = int(upper)

  if ((password[lower-1]==letter) or (password[upper-1]==letter)) and not ((password[lower-1]==letter) and (password[upper-1]==letter)):
    validation = True
    valid_pwd += 1

print("Number of valid passwords is ", valid_pwd)

  


