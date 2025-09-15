from itertools import combinations
def knapsack_bruteforce_all_subsets(weights, values, capacity):
    n = len(values)
    max_profit = 0
    best_combination = None
    print(f"\nKnapsack Capacity = {capacity}\n")
    print("All Possible Subsets:")
    # Generate all subsets (including empty set)
    for r in range(0, n+1):
        for subset in combinations(range(n), r):
            total_weight = sum(weights[i] for i in subset)
            total_value = sum(values[i] for i in subset)
            items = [i+1 for i in subset]  # 1-based item numbering
            if total_weight <= capacity:
                status = "Considered"
                if total_value > max_profit:
                    max_profit = total_value
                    best_combination = (items, total_weight, total_value)
            else:
                status = "Not Considered (Exceeds Capacity)"
            print(f"Items: {items}, Weight: {total_weight}, Value: {total_value} --> {status}")
    # Display best solution
    print("\nBest Combination Found:")
    print(f"Items: {best_combination[0]}, Weight: {best_combination[1]}, Profit: {best_combination[2]}")
    print(f"\nMaximum Profit Achievable = {max_profit} (with Capacity = {capacity})")
    return max_profit

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    weights = []
    values = []
    print("\nEnter weights and values for each item:")
    for i in range(n):
        w = int(input(f"Weight of item {i+1}: "))
        v = int(input(f"Value of item {i+1}: "))
        weights.append(w)
        values.append(v)
    capacity = int(input("\nEnter knapsack capacity: "))
    knapsack_bruteforce_all_subsets(weights, values, capacity)