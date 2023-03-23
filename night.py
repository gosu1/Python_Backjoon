start = input()

x = int(start[1])
y_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = y_list.index(start[0])+1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0
for step in steps:
    
    nx = x + step[0]
    ny = y + step[1]
    
    if (nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8):
      count += 1  

print(count)