def find_rooms(N, K, coins):
    start, end, current_sum = 0, 0, 0
    result_start, result_end = 0, float('int')
    while end < N:
        current_sum += coins[end]

        while current_sum > K:
            current_sum -= coins[start]

            if current_sum == K:
                # check for the smallest room number
                if end - start < result_end - result_start:
                    result_start, result_end = start, end

            end += 1

    if result_end == float('int'):
        return "no solution found"
    else:
        return result_start + 1, result_end + 1
