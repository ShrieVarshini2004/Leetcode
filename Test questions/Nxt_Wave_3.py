def minimum_cost_under_length_constraint(pairs, k):
    min_cost = {}

    for length, cost in pairs:
        if length <= k:
            if length not in min_cost:
                min_cost[length] = cost
            else:
                min_cost[length] = min(min_cost[length], cost)

    return sum(min_cost.values())
print(minimum_cost_under_length_constraint([[1,10],[2,5],[2,3],[3,8]], 2)) #13
print(minimum_cost_under_length_constraint([[5,5],[6,6]], 4)) #0