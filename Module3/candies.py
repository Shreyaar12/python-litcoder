import heapq

def combine_candies(target, candies):
    heapq.heapify(candies)
    steps = 0
    while len(candies) > 1 and candies[0] < target:
        least_sweet = heapq.heappop(candies)
        second_least_sweet = heapq.heappop(candies)
        combined_sweetness = least_sweet + 2 * second_least_sweet
        heapq.heappush(candies, combined_sweetness)
        steps += 1

    if candies[0] < target:
        return -1
    return steps

# User input handling
if __name__ == "__main__":
    target_sweetness = int(input("Enter the target sweetness: "))
    candies_sweetness = list(map(int, input("Enter the sweetness of each candy, separated by space: ").split()))

    result = combine_candies(target_sweetness, candies_sweetness)
    print("Number of steps required:", result)
