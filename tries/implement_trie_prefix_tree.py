'''
Question: https://leetcode.com/problems/implement-trie-prefix-tree/
'''

class TrieNode:
    """
    Define a class to store each node's
    i.e. character's information (children and endOfWord flag)
    """
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        # Init the root of the Trie as an empty TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start with the root of the Trie
        cur = self.root
        
        # Iterate through every character in the word to be inserted
        for c in word:
            # If the char doesn't exist in the Trie, Add it!
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            # Move 'cur' to the children of the current character
            cur = cur.children[c]

        # Finally, once you insert all characters, 
        # set the `endOfWord` flag for the last character
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        # Start the search from the root of the Trie i.e. at 'self.root'
        cur = self.root
        
        # Extract every character from the search word
        for c in word:

            # If current character not in the Trie and it's children, return False
            if c not in cur.children:
                return False
            
            # Else, keeping moving `cur` to the current character's children
            cur = cur.children[c]
        
        # Finally return True only if the word is 
        # Fully a part of the Trie i.e. along with `endOfWord` flag
        return cur.endOfWord
        
    def startsWith(self, prefix: str) -> bool:
        # Same logic as `search` function but here we don't check `endOfWord` flag.
        # Since we are only checking if the prefix exists in the Trie.
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            
            # Keep moving the current character to it's children
            cur = cur.children[c]        
        
        # Return 'True' directly w/o checking `endOfWord` flag
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)