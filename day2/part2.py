# --- Day 2: Dive! ---

depth = 0
horizontal = 0
aim = 0

with open("input.txt") as f:
   lines = f.readlines() 
   for line in lines:
      
      (direction, value) = line.split() 
      value = int(value)
      if direction == "forward":
         horizontal += value
         depth += value * aim
      elif direction == "up":
         aim -= value
      elif direction == "down":
         aim += value
      else:
         print("invalid direction")
      

print("Part 2: {} ".format(abs(depth * horizontal)))

