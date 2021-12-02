# --- Day 1: Sonar Sweep ---
increased = 0 
with open("day1.txt") as f:
   m = f.readlines()   
   for i in range(1, len(m)):
      if int(m[i-1]) < int(m[i]):
          increased += 1
print("Part 1: {} measurements are larger than the previous measurement".format(increased))

