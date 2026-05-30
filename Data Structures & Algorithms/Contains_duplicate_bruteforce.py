def duplicate(nums):
 count =0
 for i in range(0,len(nums)-1):
   for j in range(i+1,len(nums)):
     print("i is",i,"nums[i] is",nums[i],"j is",j,"nums[j] is",nums[j])
     if nums[i]==nums[j]:
        count +=1
     else:
        pass
 return count>0

arr=[1,2,3,4]
b=duplicate(arr)
print(b)
