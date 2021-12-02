# --- Day 1: Sonar Sweep ---
increased = 0
subset_sums = [] 

with open("day1.txt") as f:
   m = f.readlines()   
   last_sum = None
   for i in range(len(m) - 2):
      subset = [int(m[i]), int(m[i+1]), int(m[i+2])]
      subset_sum = sum(subset)
      if last_sum is None:
         last_sum = subset_sum
      if subset_sum > last_sum:
         increased += 1 
      last_sum = subset_sum 
print("Part 2: {} measurements are larger than the previous measurement".format(increased))

