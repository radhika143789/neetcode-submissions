class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:
    def __init__(self):
        # Initialize the root of the trie
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If the character doesn't exist, create a new node
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move to the child node
            curr = curr.children[char]
        # Mark the end of the word
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # Return True only if it's the end of a valid inserted word
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # If we successfully traversed the prefix, it exists
        return True