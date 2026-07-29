class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            # 1. Find the delimiter '#' that terminates the length prefix
            j = s.find('#', i)
            length = int(s[i:j])
            
            # 2. Extract exactly `length` characters after '#'
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            
            # 3. Advance pointer to the start of the next chunk
            i = end
            
        return decoded