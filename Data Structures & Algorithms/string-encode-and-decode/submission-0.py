class Solution:
    # thought process
    # why don't just append string and decode?
    # it's hard to decode since it has to carry information
    # about each string
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(f"{len(word)}{word}")
        return "#".join(encoded)

    def decode(self, s: str) -> List[str]:
        delimited = s.split("#")
        strs = []
        for decoded in delimited:
            charLen = decoded[0]
            word = decoded[1:]
            strs.append(word)
        return strs

