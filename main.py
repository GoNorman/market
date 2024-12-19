def get_final_state(nums : list[int], k : int, multiplier : int) -> list[int]:
    for val in range(k):
        nums[nums.index(min(nums))] = min(nums) * multiplier
    return nums


def find_score(nums : list[int]) -> int:

    score = 0

    print(nums)

    for i in nums:
        min_val = min(nums)
        index = nums.index(min_val)

        if index == 0:
            print(f'min val {nums}')
            score += min_val
            nums[index + 1] = False
            nums[index] = False

        if index == len(nums) - 1:
            score += min_val
            nums[index - 1] = False
            nums[index] = False

        if index > 0:
            score += min_val
            nums[index - 1] = False
            nums[index + 1] = False
            nums[index] = False

    return score


def final_prices(prices: list[int]) -> list[int]:
    n = len(prices)
    answer = prices[:]

    for i in range(n):
        for j in range(i + 1, n):
            if j > i and prices[j] <= prices[i]:
                answer[i] = prices[i] - prices[j]
                break
    return answer

print(final_prices([8,4,6,2,3]))

def fill_prefix_sum(nums: list[int], n:int, presix_sum:list[int]) -> list[int]:
    prefix_sum[0] = nums[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    return prefix_sum

arr = [1,2,3,4,5,6]
n = len(arr)

prefix_sum = [0 for i in range(n)]

print(f'prefix sum {fill_prefix_sum(arr, n, prefix_sum)}')

