class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i]={}
            cur=cur[i]
        cur["."]="."

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur:
                return False
            cur=cur[i]
        return "." in cur
        

    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root
        for i in prefix:
            if i not in cur:
                return False
            cur=cur[i]
        return True
