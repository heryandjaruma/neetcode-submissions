class Solution:
    # thought process
    # why don't just append string and decode?
    # it's hard to decode since it has to carry information
    # about each string
    def encode(self, strs: List[str]) -> str:
        encoded = []
        if not strs: # special case
            return ""
        for word in strs:
            if word == "":
                encoded.append("0")
            else:
                encoded.append(f"{len(word)}{word}")
        return "\x00".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == "": # special case
            return []
        delimited = s.split("\x00")
        strs = []
        for decoded in delimited:
            if decoded == "0":
                strs.append("")
            else:
                charLen = decoded[0]
                word = decoded[1:]
                strs.append(word)
        return strs

