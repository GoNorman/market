def find_max_lenght(nums : list[int]) -> int:
    prefix_sum = 0
    seen_sum = {0:-1}
    max_lenght = 0

    for i, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1

        if prefix_sum in seen_sum:
            max_lenght = max(max_lenght, i - seen_sum[prefix_sum])
        else:
            seen_sum[prefix_sum] = i
    return max_lenght

print(find_max_lenght([0,1,0,1]))

