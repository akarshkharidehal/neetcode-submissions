1. Core Concepts
Both HashSets and HashMaps rely on a fundamental computer science mechanism called Hashing. Hashing transforms an input key (using a hash function) into a numerical index representing a location in memory (a bucket).

What is a HashSet?
A HashSet is an unordered collection of unique elements. It is designed for fast existence checks and mathematical set operations.
● Core Feature: Prevents duplicate entries.
● Analogy: A guest list where names can only be entered once. 


What is a HashMap (or HashTable/Dictionary)?
A HashMap is an unordered collection of Key-Value Pairs. It maps a unique key to a specific value.
● Core Feature: Key-value association; keys are unique, values can be duplicated.
● Analogy: A coat check where a unique ticket number (key) is paired with a specific coat (value).


3. Under the Hood: How They Work
To understand why hash structures are incredibly fast, we must look at how they manage memory and lookups:
1. Hash Function: Takes a key and outputs an integer. $$\text{Index} = \text{Hash}(Key) \pmod{\text{Array Length}}$$
2. Buckets: An array of slots where elements are stored.
3. Collision Handling: When two different keys produce the same index.
● Chaining (Common): Each bucket contains a linked list or binary tree of entries sharing the same index.
● Open Addressing: Finding another empty bucket nearby via probing.
Key "Alice" ----> [ Hash Function ] ----> Index 3 ----> Bucket [ "Alice": 123-456 ]
Key "Bob" ----> [ Hash Function ] ----> Index 3 ----> Bucket [ "Alice": 123-456 ] -> [ "Bob": 789-101 ] (Collision Chaining)


3. Practical Applications & Coding Examples
   
Example 1: Contains Duplicate (HashSet)
● Problem: Check if any value appears at least twice in an array.
● Algorithm: Maintain a set of visited elements. If the current element is already in the set, a duplicate is found.
def containsDuplicate(nums: list[int]) -> bool:
visited = set()
for num in nums:
if num in visited:
return True
visited.add(num)
return False


Example 2: Two Sum (HashMap)
● Problem: Find two numbers that add up to a target and return their indices.
● Algorithm: As we iterate, look up if the complement = target - num is already in our HashMap.
def twoSum(nums: list[int], target: int) -> list[int]:
num_to_index = {}
for index, num in enumerate(nums):
return [num_to_index[complement], index]
num_to_index[num] = index
return []


Example 3: Subarray Sum Equals K (HashMap Prefix Sums)
● Problem: Find the total number of continuous subarrays whose sum equals k.
def subarraySum(nums: list[int], k: int) -> int:
count = 0
curr_sum = 0
# Map to store prefix_sum: frequency
prefix_sums = {0: 1}
for num in nums:
curr_sum += num
if (curr_sum - k) in prefix_sums:
count += prefix_sums[curr_sum - k]
prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
return count


4. Complexity Analysis
Operation
Average Case
Worst Case (Heavy Collisions)

1) Insertion
$O(1)$
$O(N)$

2) Lookup / Search
$O(1)$
$O(N)$

3) Deletion
$O(1)$
$O(N)$

4) Space Complexity
$O(N)$
$O(N)$

Why is the Worst Case $O(N)$?
If the hash function maps all keys to the same bucket (e.g., poor hash function or intentional denial of service attack), the hash map degrades into a linked list, changing search complexity from constant $O(1)$ to linear $O(N)$. Modern languages mitigate this by converting long
linked lists in buckets into self-balancing binary search trees.


5. How to Optimize Hash-Based Solutions
   
1. Pre-sizing / Load Factor: Rehashing occurs when the map expands to maintain a low collision rate (usually when it is 75% full, called a load factor of 0.75). If you know you will store $N$ items, initialize the collection with a capacity of $N / 0.75$ to prevent costly automatic array resizing and copying operations.
   
2. Avoid Object Wrappers / Auto-boxing: In languages like Java, using HashMap<Integer, Integer> creates significant memory overhead because of wrapper objects. Use primitive-optimized collections (like Trove or fastutil) or pre-allocate primitive arrays if keys fall within a small, dense range.

3. Optimal Key Choice: Use immutable objects as keys (like strings or integers). If custom objects are used as keys, implement high-performance, deterministic hashCode() and equals() methods.

complement = target - num
if complement in num_to_index:
