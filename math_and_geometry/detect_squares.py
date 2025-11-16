'''
Question: https://leetcode.com/problems/detect-squares/
'''

class DetectSquares:

    def __init__(self):
        # Maintain a count of all the points
        self.ptsCount = defaultdict(int)
        # Use a list to maintain the actual points since duplicate points are allowed
        self.pts = []

    def add(self, point: List[int]) -> None:
        # Add the point to the `ptsCount` dict and also to the actual list `pts`
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        # Extract the x and y coords of the query `point`
        px, py = point

        # Iterate through every stored point in `pts`
        for x, y in self.pts:

            # Check if current x & y coords are diagonal (since we are looking for a valid square formation)
            # Also ensure that current x & y are not just repeated points (since duplicates are allowed)
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                # If any true, not a valid case for making a square
                continue
            
            # If not, then valid, so count how many squares can be made
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res
