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


print(get_final_state([2,1,3,5,6], 5, 2))
print(f'______Find score ______')
print(find_score([2,1,3,4,5,2]))
print('TEST')
print(min([, 8, 1, 4, 5, 2]))