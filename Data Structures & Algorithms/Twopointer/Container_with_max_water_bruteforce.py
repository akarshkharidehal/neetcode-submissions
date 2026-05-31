
heights = [1,7,2,5,4,7,3,6]

max_water = 0
best_pair = ()

for i in range(len(heights)):
    for j in range(i + 1, len(heights)):
       print("i is", i, "heights[i] is", heights[i],"j is", j, "heights[j] is", heights[j])
       vertical = min(heights[i], heights[j])
       horizontal = j - i
       area = vertical * horizontal
       print("Area is", area)
       if area > max_water:
          max_water = area
          best_pair = (i, j)

print("\nMaximum water is:", max_water)
print("Best pair indexes are:", best_pair)
