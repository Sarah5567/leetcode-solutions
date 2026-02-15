class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k_idx = nums.index(k)

        balance = 0
        balance_dict = defaultdict(int)
        balance_dict[0] = 1
        for i in range(k_idx + 1, n):
            if nums[i] > k:
                balance += 1
            else:
                balance -= 1
            balance_dict[balance] += 1

        ans = balance_dict[0] + balance_dict[1]
        balance = 0
        for i in range(k_idx - 1, -1, -1):
            if nums[i] > k:
                balance += 1
            else:
                balance -= 1
            ans += balance_dict[-balance] + balance_dict[-balance + 1]
        
        return ans
        