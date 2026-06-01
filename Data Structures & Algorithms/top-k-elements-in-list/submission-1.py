class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

          # Step 1: Create counter using hashmap
        d = {}
        n =[[] for _ in range(len(nums)+1)]

        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] +=1

    # Step 2 : Store elements in new array based on their frequency
        for num, freq in d.items():
            n[freq].append(num)


    # Step 3: 
        l = []

        for t in range(len(nums), 0, -1):
            for x in n[t]:
                l.append(x)
                if len(l) == k:
                   return l                   


