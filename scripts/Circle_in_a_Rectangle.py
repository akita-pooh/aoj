input_sets = list(map(int, input().split()))
w, h = input_sets[0], input_sets[1]
x, y, r = input_sets[2], input_sets[3], input_sets[4]

if ((x - r >= 0) and (x + r <= w)) and ((y - r >= 0) and (y + r <= h)):
    print("Yes")
else:
    print("No")
