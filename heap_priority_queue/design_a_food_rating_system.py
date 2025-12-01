'''
Question: https://leetcode.com/problems/design-a-food-rating-system/
'''

from typing import List
import heapq


class FoodRatings:
    """
    Approach: Use a combination of hash maps and max heaps to efficiently manage food ratings by cuisine
        
        Intuition:
            Maintain fast updates of a food's rating and fast queries for highest-rated food per cuisine.
            Use:
            - food_info: direct mapping food -> (cuisine, rating) for O(1) updates/lookups.
            - cuisine_heaps: per-cuisine max-heap (simulated via min-heap with negated rating) of (-rating, food).
            Lazy deletion: On rating change, old heap entries remain; we validate the top against food_info when queried.

        Functions:
        - __init__: build mappings; push all foods into their cuisine heap.
        - changeRating: update food_info; push new (-rating, food) entry (old one becomes stale).
        - highestRated: pop stale heap entries until top matches current rating; return its food name.

    Time Complexity:
        - __init__: O(N log N) heap pushes (since the heapq maintains the heap property by sorting on each push for N foods)
        - changeRating: O(log N), for pushing new entry onto the heap
        - highestRated: Amortized O(log n) (each stale entry popped once)
    
    Space Complexity: O(N) for mappings + heap entries (including stale ones, bounded by number of updates)
    """

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}          # food -> (cuisine, current_rating)
        self.cuisine_heaps = {}      # cuisine -> list[(-rating, food)] (max-heap via negation on rating)

        # Populate initial data structures
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)

            if cuisine not in self.cuisine_heaps:
                self.cuisine_heaps[cuisine] = []
            # Push as (-rating, food) to get highest rating; tie-break by lexicographically smallest food
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        # Retrieve current cuisine of the food
        cuisine, _ = self.food_info[food]

        # Update current authoritative rating.
        self.food_info[food] = (cuisine, newRating)

        # Push new entry; old entries become stale. lazy deletion so old rating is not deleted and instead handled in `highestRated`
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Access the heap for the queried cuisine
        heap = self.cuisine_heaps[cuisine]

        # Iterate through the cusine heap and pop until top entry matches the latest rating stored in food_info (and not in the heap since we do lazy deletion)
        while heap:
            # Peek at the top entry
            rating_neg, food = heap[0]

            # Check if it matches the current rating
            if self.food_info[food][1] == -rating_neg:
                # If yes, we have the latest rating already stored for the top-rated food
                return food
            # Otherwise, it's stale; pop it / discard stale entry and continue
            heapq.heappop(heap)

        # If no valid entries found (should not happen in valid usage), return empty string
        return ""


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)