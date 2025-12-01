'''
Question: https://leetcode.com/problems/rank-teams-by-votes/
'''

from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        """
        Approach:
            - Create a dict to count the votes for each team at each position
            - Sort the teams based on their votes counts and lexicographical (i.e., alphabetical) order as a tiebreaker
            - Finally, join the sorted team names to form the result string

        Time Complexity: O(N * S + N logN) ~ O(N logN)
            - N is the number of teams 
            - S is the length of each vote
        Space Complexity: O(N * S) ~ O(N)
            - Storing the vote counts for each team at each position
        """

        # Initialize a dictionary to hold vote counts
        vote_counts = {}

        # Build the vote counts for each team
        for vote in votes:
            # Iterate through each team in the vote string (eg. "ABC")
            for i, team in enumerate(vote):
                # If the team is not in the dictionary, initialize its vote count list
                if team not in vote_counts:
                    vote_counts[team] = [0] * len(vote) # New list for  will be the length of the vote string
                
                # Increment the vote count for the team at the current position
                vote_counts[team][i] += 1
        
        # Extract team names and pre-sort them alphabetically (for tiebreakers)
        # Note: Python's sort is stable, so when final sorting uses `vote_counts` as the key, any ties on identical count vectors will
        # keep this alphabetical order (e.g., for {'A': [5, 0, 0], 'B': [0, 2, 3], 'C': [0, 3, 2]})
        voted_names = sorted(vote_counts.keys())

        # Sort the team names based on their vote counts in descending order and return the result as a string
        final_rank = sorted(
            voted_names,
            key = lambda x: vote_counts[x], # Sort by vote counts for each team
            reverse=True
        )

        # Return the final ranked result as a string
        return "".join(final_rank)
