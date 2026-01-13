class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # The optimal target is the weighted median
        # Cost function is convex, can use ternary search or just try all values
        
        # Sort by nums value
        pairs = sorted(zip(nums, cost))
        n = len(pairs)
        
        # Find weighted median: the value where cumulative weight >= half total weight
        total_cost = sum(cost)
        
        # Calculate cost for a given target
        def calc_cost(target):
            return sum(abs(nums[i] - target) * cost[i] for i in range(n))
        
        # Find the weighted median
        cumsum = 0
        median_val = pairs[0][0]
        for num, c in pairs:
            cumsum += c
            if cumsum >= (total_cost + 1) // 2:
                median_val = num
                break
        
        # The answer is either at median_val or nearby
        # Since cost function is convex, we can check median and neighbors
        result = calc_cost(median_val)
        
        # Check a few values around median to be safe
        for delta in range(-1, 2):
            result = min(result, calc_cost(median_val + delta))
        
        return result