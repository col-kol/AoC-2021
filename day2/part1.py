# --- Day 2: Dive! ---

depth = 0
horizontal = 0

with open("input.txt") as f:
   lines = f.readlines() 
   for line in lines:
      (direction, value) = line.split() 
      value = int(value)
      if direction == "forward":
         horizontal += value
      elif direction == "up":
         depth += value
      elif direction == "down":
         depth -= value
      else:
         print("invalid direction")

print("Part 1: {} ".format(abs(depth * horizontal)))

