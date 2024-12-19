def max_chunks_to_sorted(arr:list[int]) -> int:
    max_so_for = 0
    chunks = 0

    for i, val in enumerate(arr):
        max_so_for = max(max_so_for, val)
        if max_so_for == i:
            chunks += 1
    return chunks



print(max_chunks_to_sorted([4,3,2,1,0]))

