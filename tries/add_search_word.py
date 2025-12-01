"""
Question: https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""

# Define a TrieNode to store information about each node in the Trie
class TrieNode:
    """
    Define a class to store each node
    i.e. character's information (`children` and `endOfWord` flag)
    """
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        # Init root of the WordDictionary Trie as an empty TrieNode
        self.root = TrieNode()
        # Add word length so that we don't search for words longer than the current longest word
        self.max_word_len = 0
        
    def addWord(self, word: str) -> None:
        # Similar to adding word in https://leetcode.com/problems/implement-trie-prefix-tree/
        cur = self.root
        
        for c in word:
            # If the character not a part of the Trie, add it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        # After adding all character, set the flag for end of word on the last character/node of the word
        cur.endOfWord = True
        
        # Also, update the length of the longest word in the WordDictionary
        self.max_word_len = max(self.max_word_len, len(word))
        

    def search(self, word: str) -> bool:
        # Perform normal search as in https://leetcode.com/problems/implement-trie-prefix-tree/ 
        # but for '.' we use DFS to search all the possible values.
        
        # If we are searching for a word longer than what exists in the Trie, return False
        if len(word) > self.max_word_len:
            return False
        
        # DFS search for the word
        def dfs(start_idx, root):
            cur = root
            
            # We start searching from index `start_idx` in the word
            for i in range(start_idx, len(word)):
                c = word[i]
                
                # Recursive search for when "." is present in the search string
                if c == ".":
                    # Search all children of the current char in the Trie
                    for child in cur.children.values():
                       
                       # Since "." can be any character, perform a recursive DFS for the remaining characters
                        if dfs(i + 1, child):
                             # If the rest of the characters are in the children, then we have a match
                             # Since last recursive call with return True and enter this `if` condition
                            return True
                    
                    # If the rest of the children don't have a match, return False
                    return False
                
                # If no "." encountered, the Usual search in the Trie for the current character
                else:
                    if c not in cur.children:
                        return False
                    
                    # If `c` is in the Trie, move to the next character (by searching in the children)
                    cur = cur.children[c]
            
            # Finally, when you're here, all the characters in the word have been found in the Trie, BUT...
            # Return True ONLY IF the word is a complete word in the Trie i.e. has `endOfWord` flag set!
            return cur.endOfWord
        
        ## Call the recursive DFS on the Trie, starting with index 0
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)