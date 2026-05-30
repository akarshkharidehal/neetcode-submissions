
nums=[-1,0,1,2,-1,-4]
print(nums)
res = set()
for i in range(0,len(nums)):
   for j in range(i+1,len(nums)):
      for k in range(j+1,len(nums)):
         print("i is",i,"nums[i] is",nums[i] ,"j is",j,"nums[j] is",nums[j],"k is",k,"nums[k] is",nums[k])
         if nums[i]+nums[j]+nums[k]==0:
            res.add(tuple(sorted([nums[i],nums[j],nums[k]])))

print(res)
