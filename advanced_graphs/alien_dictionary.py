'''
Question (Leetcode Premium): https://leetcode.com/problems/alien-dictionary/
Neetcode Version: https://neetcode.io/problems/foreign-dictionary
'''

from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        Approach: Perform Topological Sort by traversing through the words and characters in Post-order DFS.
        What is Topological Sort?
            A topological sort is a linear ordering of vertices in a directed acyclic graph (DAG) such that,
            for every directed edge `U -> V` from vertex `U` to vertex `V`, `U` comes before `V` in the ordering (which is what we want for the given alien dictionary)

        How to achieve it? 
            - Perform DFS of each of character of the words and recursively on its neighbors (using the adjaceny list). 
            - Maintain the post-order DFS path in `res` as you traverse the adjacency list, which will be the sort order of the characters in the alien dictionary!
        
        Why Post-order DFS?
            - Post-order traversal means we visit the leaf nodes first and then their parent nodes, i.e., Leaf -> Node -> Parent
            - So ensures that we visit all the neighbors of a character before we visit the character itself

        -> Base case for the DFS will be:
            - If the current char (which could be a neighbor from a recursive call) is already visited, just return and move to the next recursive DFS call
            - But IF already visited AND also a part of the current path, then it's a loop so we have detected an invalid input case (input alien dictionary has no valid solution) 

        *Algorithm Implementation:*

        PART I:
            Iterate through the `words` in pairs and find the first differing character.
            Populate an adjacency list with the differing character from word 1 as the key and the differing char from word 2 as it's neighbors
            (implying that char from w1 comes before char from w2).
            > This will help establish the sort order of the characters (similar to when we do a lexical sort of words in English language)

        PART II:
            Perform DFS of each of character of the words and recursively on its neighbors (using the adjaceny list). 
            Maintain the post-order DFS path in `res` as you traverse the adjacency list, which will be the sort order of the characters in the alien dictionary!
            
            > Base cases during the DFS will be ->
                - If the current char (which could be a neighbor from a recursive call) is already visited, just return and move to the next recursive DFS call
                - But IF already visited AND also a part of the current path, then it's a loop so we have detected an invalid input case (input alien dictionary has no valid solution) 
        
        Note: The result path will be in reverse order since we are performing "post-order" DFS, i.e., Leaf -> Node -> Parent
        So when returning the result, we reverse the order of `res`


        Time Complexity: O(N + V + E) -> to iterate through the entire graph where,
            - `V` = unique characters (vertices) in the dictionary
            - `E` = edges (neighbors)
            - `N` = sum of lengths of all strings in `words` 
        
        Space Complexity O(V + E) -> Space needs to store the graph
        """

        # Maintain an adjacency dictionary where key is each char and value are a set of all its neighbors from different words
        adj = {c:set() for w in words for c in w}

        ''' Part I: Loop to populate the adjacency list '''
        # First iterate through all input `words` in pairs, and find the first differing character between them
        for i in range(len(words) - 1):
            # Extract the words in pairs from the input list
            w1, w2 = words[i], words[i+1]
            # Calculate the minimum length between the two words
            minLen = min(len(w1), len(w2))

            # Check for INVALID case (as mentioned as in the question directly), 
            # where word 1 is larger than word two AND but their first `minLen` characters are the same
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Loop for finding the first differing characters between the two words, 
            # which will help determine the sort order of the characters
            # Eg. w1 = ape & w2 = apple
            # First differing characters are at position 3 -> "e" and "p", so we know that "e" comes before "p" in the alien dictionary
            for j in range(minLen):

                # Iterate until we find the first different characters between the two words    
                if w1[j] != w2[j]:
                    # Add w2 character from w2 to neighbors list of w1's character (w1[j])
                    adj[w1[j]].add(w2[j])
                    # Immediately break since the rest will be different either way so won't help in determining the sort order
                    break

        ''' PART II: Perform Post-Order DFS each character in `adj` and it's neighbors '''

        # Create a visited dict with bool values only, where for each character:
        # False = visited, but not in current path `res`
        # True = visited AND also already in current path, i.e., loop detected so INVALID input
        visited = {}

        # Maintains the post-order DFS traversal path and records the character sort order of the alien dictionary
        res = []

        def dfs(char):
            # Base case: If `char` already in visited, return the stored boolean value
            if char in visited:
                return visited[char]

            # If not visited, mark the character as visited and also now a part of the current path
            visited[char] = True

            # Perform recursive DFS on all neighbors of `char` in `adj`
            for neighbor in adj[char]:
                # If any of the DFS calls on the `neighbor` returns `True` (from base case), then True to indicate a loop in the graph (INVALID case)
                if dfs(neighbor):
                    return True
            
            # Once recursive DFS on all neighbors of `char` successfully complete (no loops), 
            # mark the char as `False` in `visit`, which means visited but not in current path
            visited[char] = False
            
            # Finally, add `char` to current path
            res.append(char)

        ''' Actual DFS calls for all unique chars from `words` stored in `adj` '''
        for c in adj:
            # If any of the chars returns True, loop detected. Immediately return empty string (INVALID case)
            if dfs(c):
                return ""
        
        # After successful DFS on all chars in `adj`, the order will be populated in `res`
        # but in reverse order since we did a post-order DFS traversal
        # So, return correct order by reversing the `res` list
        return "".join(res[::-1])                
