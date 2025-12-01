'''
Question: https://leetcode.com/problems/stock-price-fluctuation/
'''

from sortedcontainers import SortedList
from heapq import heappush, heappop


class StockPrice:
    """
    Approach: Use two heaps (min-heap and max-heap) along with a dictionary to track the latest prices
        - Maintain a dict to track the "timestamp -> price" for each `update` operation
        - Maintain a min-heap to track the minimum prices
        - Maintain a max-heap to track the maximum prices
        - Maintain a `latest_timestamp` to track the lastest timestamp (since the records don't come in with sequential timestamps)
        
    Lazy deletion: for `update()`, we just add the new price to the heap
        The old price remains in the heap. The deletion is handled during calls to `maximum()` and `minimum()` 
            - Pop from top of the max or min heap
            - Check if the latest value in the `ts_to_price` matches the popped value from the heap
            - If it matches, return it as the valid max or min price
            - If it doesn't match, it means it's an outdated price, so we pop it and continue checking the next top of the heap

    Time Complexity: O(log N) for `update()` due to insertion in heaps
    Space Complexity: O(N) for storing the dict and heaps
    """

    def __init__(self):
        self.ts_to_price = {} # Dict to map timestamp to price
        self.min_heap = [] # Min-heap to maintain min prices
        self.max_heap = [] # Max-heap to maintain max prices (store negative prices)
        self.latest_ts = 0 # Variable to track latest timestamp

    def update(self, timestamp: int, price: int) -> None:
        
        # Update the dict with new price
        self.ts_to_price[timestamp] = price 
        self.latest_ts = max(self.latest_ts, timestamp) # Update latest timestamp

        # Push new price to min-heap and max-heap
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp)) # Use negation for simulating max-heap from min-heap

    def current(self) -> int:
        # Return price at latest timestamp
        return self.ts_to_price[self.latest_ts]
    
    def maximum(self) -> int:
        # Pop from max-heap until we find a valid price (matches the current price in dict)
        while True:
            price, timestamp = self.max_heap[0]
            
            # Check if the negated price matches the current price for that timestamp
            if -price == self.ts_to_price[timestamp]:
                return -price

            # If not, then the price is outdated, pop it from heap
            heappop(self.max_heap)
    
    def minimum(self) -> int:
        # Pop from min-heap until we find a valid price (matches the current price in dict)
        while True:
            price, timestamp = self.min_heap[0]
            # Check if the price matches the current price for that timestamp
            if price == self.ts_to_price[timestamp]:
                # If it matches, return the price which will be the minimum value in the heap (since popped from top of min-heap)
                return price
            # If not, then the price is outdated, pop it from heap
            heappop(self.min_heap)

    """
    Approach: Use SortedList to maintain sorted prices instead of heaps
        - Maintain a dict to track the "timestamp -> price" for each `update` operation
        - Maintain a sorted list which tracks the max and min values (at 0 and -1 positions)
        - Maintain a `latest_timestamp` to track the lastest timestamp (since the records don't come in with sequential timestamps)

    Time Complexity: O(log N) for `update()` due to insertion and deletion in sorted list
    Space Complexity: O(N) for storing the dict and sorted list
    """

    # def __init__(self):
    #     self.ts_to_price = {} # Dict to map timestamp to price
    #     self.sorted_list = SortedList() # Sorted list to maintain sorted prices (can use heapq as well)
    #     self.latest_ts = 0 # Variable to track latest timestamp

    # def update(self, timestamp: int, price: int) -> None:

    #     # If timestamp already exists, remove the old price from sorted list (to update with new price)
    #     if timestamp in self.ts_to_price:
    #         old_price = self.ts_to_price[timestamp]
    #         self.sorted_list.remove(old_price)
        
    #     self.ts_to_price[timestamp] = price # Update the dict and sorted list with new price 
    #     self.sorted_list.add(price) # Add new price to sorted list
    #     self.latest_ts = max(self.latest_ts, timestamp) # Update latest timestamp
        
    # def current(self) -> int:
    #     # Return price at latest timestamp
    #     return self.ts_to_price[self.latest_ts]

    # def maximum(self) -> int:
    #     # Return max price (last element in sorted list)
    #     return self.sorted_list[-1]

    # def minimum(self) -> int:
    #     # Return min price (first element in sorted list)
    #     return self.sorted_list[0]