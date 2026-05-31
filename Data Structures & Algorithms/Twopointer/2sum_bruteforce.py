nums = [1,2,3,4]
target = 3
print(nums)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
       print("i is", i,"nums[i] is", nums[i],"j is", j,"nums[j] is", nums[j])
       current_sum = nums[i] + nums[j]
       print("Sum is:", current_sum)
       if current_sum == target:
            result = [i, j]

print("Final Result:", result)

