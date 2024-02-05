#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
pattern = r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])'

string=""
decoded_script=""
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m):
   
    for j in range(n):
        string += str(matrix[j][i])


decoded_string = re.sub(pattern, ' ', string)

print(decoded_string)
