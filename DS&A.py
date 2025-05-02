# ============================================
#? 🧠 1. Two Sum (Easy) - Time: O(n), Space: O(n)
# ============================================
#! Problem:
#!   Given array nums and integer target, return indices of two numbers adding to target.
#! Example:
#!   nums = [2,7,11,15], target = 9  -> [0,1]
#! Key Idea:
#!   As you scan, store each number’s index in a hash map. For current num, check if its complement (target-num)
#!   was seen before.
#! Pseudocode:
#!   M = {}
#!   for i in 0..len(nums)-1:
#!     diff = target - nums[i]
#!     if diff in M: return [M[diff], i]
#!     M[nums[i]] = i

def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        # complement that pairs with current num
        diff = target - num
        if diff in num_to_index:
            return [num_to_index[diff], i]
        # record this num's index for future complements
        num_to_index[num] = i
    return []

#* Hints:
#* As I move through the list, I check if I’ve already seen the number that would complete the target sum—if not, I save my current number for the next guy to check against.
#* 1. Scan left-to-right, storing seen numbers in a map—when you see x, check if target−x was seen.
#* 2. Think: for current index, what complement do you need to reach target?
#* 3. A hash map lookup is O(1), enabling a single-pass solution.

# ============================================
#? 🧠 2. Valid Parentheses (Easy) - Time: O(n), Space: O(n)
# ============================================
#! Problem:
#!   Given a string of brackets, determine if all opens/closes match in correct order.
#! Example:
#!   s = "()[]{}"  -> True
#! Key Idea:
#!   Use a stack to track opening brackets; on closing, check top of stack for matching type.
#! Pseudocode:
#!   mapping = {')':'(', ']':'[', '}':'{'}
#!   st = []
#!   for c in s:
#!     if c in mapping.values(): push c
#!     else if stack empty or pop()!=mapping[c]: return False
#!   return stack empty

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        else:
            # mismatch or nothing to pop
            if not stack or stack.pop() != mapping[char]:
                return False
    # all opens matched if stack is empty
    return not stack

#* Hints:
#* 1. Use a stack: push opens, and on each close pop and compare to a mapping.
#* 2. If you see a closing bracket when the stack is empty, it's invalid immediately.
#* 3. Map each closing bracket to its matching opening bracket for O(1) checks.

# ============================================
#? 🧠 3. Longest Substring Without Repeating Characters (Medium) - Time: O(n), Space: O(min(n,|charset|))
# ============================================
#! Problem:
#!   Find length of longest substring with all unique chars.
#! Example:
#!   s = "abcabcbb"  -> 3 ("abc")
#! Key Idea:
#!   Sliding window: expand right, track last seen positions, and move left past duplicates.
#! Pseudocode:
#!   M = {}  # char→last index
#!   left = 0, max_len = 0
#!   for right in 0..len(s)-1:
#!     if s[right] in M and M[s[right]]>=left:
#!       left = M[s[right]] + 1
#!     M[s[right]] = right
#!     max_len = max(max_len, right-left+1)
#!   return max_len

def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # if duplicate inside current window, shift left
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        # update last seen index
        char_index[char] = right
        # update max window size
        window_len = right - left + 1
        if window_len > max_len:
            max_len = window_len

    return max_len

#* Hints:
#* 1. Maintain a sliding window with left/right pointers so the window always has unique chars.
#* 2. When a duplicate is found within the window, jump left past its previous index.
#* 3. Store last seen positions in a map to adjust the window in O(1) time.

# ============================================
#? 🧠 217. Contains Duplicate (Easy) - Time: O(n), Space: O(n)
# ============================================
#! Problem:
#!   Given an integer array nums, return True if any value appears at least twice in the array,
#!   and return False if every element is distinct.
#! Examples:
#!   nums = [1,2,3,1]           -> True
#!   nums = [1,2,3,4]           -> False
#!   nums = [1,1,1,3,3,4,3,2,4,2] -> True
#! Key Idea:
#!   Use a hash set to track which elements you’ve seen. As you iterate, check membership:
#!     - If the current element is already in the set → you’ve found a duplicate → return True.
#!     - Otherwise, add it to the set and continue.
#! Pseudocode:
#!   seen = {}
#!   for num in nums:
#!     if num in seen:
#!       return True
#!     seen.add(num)
#!   return False

def contains_duplicate(nums):
    seen = set()                  # Initialize an empty set.
    for num in nums:              # Iterate through each number.
        if num in seen:           # If already seen, duplicate found.
            return True           # Early exit.
        seen.add(num)             # Otherwise, mark this number as seen.
    return False                  # No duplicates detected.

#* Hints:
#* 1. A hash set gives O(1) average‐time membership checks.
#* 2. Return as soon as you detect a duplicate to save work.
#* 3. Alternative: sort the array (O(n log n)) and check adjacent pairs for equality.
#* 4. If the value range is small, you could use a boolean array (bitmap) instead of a set.
#* 5. Think “Have I seen this before?” at each step—that’s the essence of duplicate detection.

# ============================================
#? 🧠 739.  Daily Temperatures (Medium) - Stack - Time: O(n), Space: O(n)
# ============================================
#! Problem:
#!   Given a list of daily temperatures, return a list such that for each day,
#!   it tells you how many days you'd have to wait until a warmer temperature.
#!   If no future day is warmer, put 0.
#! Example:
#!   temps = [73,74,75,71,69,72,76,73]
#!   Output = [1,1,4,2,1,1,0,0]
#! Key Idea:
#!   Use a **monotonic stack** to track indexes of temperatures in decreasing order.
#!   As you move forward, if current temp > temp at stack top → pop and calculate the difference.

def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # stores (index) of unresolved temperatures

    for i, temp in enumerate(temperatures):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    return result

#* Hints:
#* 1. Think of the stack as "waiting for a warmer day" → we resolve it when a warmer day arrives.
#* 2. Stack holds indices, not values.
#* 3. A monotonically decreasing stack means you’ll only scan each temp once → O(n).
# ============================================
#? 🧠 735. Asteroid Collision (Medium) - Stack - Time: O(n), Space: O(n)
# ============================================

#* Approach:
#? Create an empty stack  
#? Iterate through each asteroid `a` in `asteroids`:
#?   • While stack not empty AND `a < 0 < stack[-1]` (a left-moving meets a right-moving):
#?       – If `abs(a) > stack[-1]`: pop stack (the new asteroid destroys the top), then continue checking  
#?       – Else if `abs(a) == stack[-1]`: pop stack (both explode), set `a = None`, break  
#?       – Else: set `a = None`, break  (the new asteroid is destroyed)  
#?   • After resolving collisions, if `a` survived (`a is not None`), push it onto stack  
#? Return the stack of survivors

#! Problem:
#!   Given a list of integers `asteroids` where each element represents the size and direction
#!   of an asteroid (positive = moving right, negative = moving left), compute the state
#!   of the asteroids after all collisions. When two asteroids collide, the smaller one explodes;
#!   if they are the same size, both explode.
#! Examples:
#!   asteroids = [5, 10, -5]    → [5, 10]
#!   asteroids = [8, -8]        → []
#!   asteroids = [10, 2, -5]    → [10]

#! Key Idea:
#!   Use a stack to keep track of surviving asteroids.  
#!   Push right-moving asteroids immediately.  
#!   For left-moving asteroids, resolve collisions against the stack’s top until no more apply.

#! Pseudocode:
#!   stack = []
#!   for a in asteroids:
#!     while stack AND a < 0 < stack[-1]:
#!       if abs(a) > stack[-1]:
#!         pop(stack)           # a destroys stack[-1]
#!         continue              # keep checking
#!       elif abs(a) == stack[-1]:
#!         pop(stack)           # both explode
#!         a = None
#!         break
#!       else:
#!         a = None             # a is destroyed
#!         break
#!     if a is not None:
#!       push(stack, a)
#!   return stack

def asteroid_collision(asteroids):
    stack = []
    for a in asteroids:
        while stack and a < 0 < stack[-1]:
            if stack[-1] < -a:
                stack.pop()
                continue
            elif stack[-1] == -a:
                stack.pop()
            break
        else:
            stack.append(a)
    return stack

#* Hints:
#* 1. Only opposite‐direction asteroids collide (left vs. right).
#* 2. Use `abs(a)` to compare sizes, ignoring sign.
#* 3. The `while` loop handles chain reactions until the new asteroid either is destroyed or no more collisions occur.
