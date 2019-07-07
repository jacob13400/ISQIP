# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = float(input())
bc = float(input())
tang = ab / bc
rad = math.atan(tang)
print('{}°'.format(int(round(math.degrees(rad)))))

