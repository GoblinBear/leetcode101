class TrieNode:
    def __init__(self):
        self.child_node = [ None ] * 26
        self.is_value = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            index = self._char_to_index(char)
            if not current.child_node[index]:
                current.child_node[index] = TrieNode()
            
            current = current.child_node[index]

        current.is_value = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if not current:
                return False

            current = current.child_node[self._char_to_index(char)]
        
        return current.is_value

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if not current:
                break

            current = current.child_node[self._char_to_index(char)]
        
        return current != None


# Test
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
# Output: True
print(trie.search("app"))
# Output: False
print(trie.starts_with("app"))
# Output: True
trie.insert("app")
print(trie.search("app"))
# Output: True
