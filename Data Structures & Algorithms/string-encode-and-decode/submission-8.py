from collections import deque

class Solution:
    # thought process
    # apparently it's fine in encoding, but in decoding process it will
    # be very much hard to exactly decode it
    # the right approach is to specify the length and the delimiter
    def encode(self, strs: List[str]) -> str:
        encoded = []
        if not strs: # special case
            return ""
        for word in strs:
            if word == "":
                encoded.append("0")
            else:
                encoded.append(f"{len(word)}#{word}")
        return "#".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == "": # special case
            return []
        result = []
        # convert into queue
        squeue = deque(s)
        print(squeue)
        while True:
            # read char until delimiter found
            lengthStr = ""
            while True:
                print(f"curr : {squeue}")
                nextChar = squeue.popleft()
                if nextChar in '1234567890':
                    lengthStr += nextChar
                if nextChar == "#": # stop reading length
                    break
                if not squeue:
                    break
            nextword = ""
            for i in range(int(lengthStr)):
                nextword += squeue.popleft()
            print(nextword)
            result.append(nextword)
            print(f" > {squeue}")
            if not squeue:
                break
            squeue.popleft() # nextchar has to be delimiter so just pop
        return result

