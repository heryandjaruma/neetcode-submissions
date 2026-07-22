class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create hashmap for each string
        outer = {} # key -> val     "charMap" -> ["word"]
        for word in strs:
            inner = {} # key -> val    "char" -> freq
            for char in word:
                if char not in inner:
                    inner[char] = 1
                else:
                    inner[char] += 1
            
            # build key by char and its count by sorted key
            sortedInner = dict(sorted(inner.items()))
            hashKey = ""
            for key, val in sortedInner.items():
                hashKey += f"{key}{val}"

            if hashKey not in outer:
                outer[hashKey] = [word]
            else:
                outer[hashKey].append(word)
        
        # convert into expected array response type
        returnVal = []
        for key, words in outer.items():
            arrWords = []
            for word in words:
                arrWords.append(word)
            returnVal.append(arrWords)
        
        return returnVal

# Time Complexity
# Build outer dict -> O(n)
# Build inner dict to count char frequency -> O(m)
# Build the key -> O(n)
# Convert into expected array response O(m+n)
# = O(m * n)

# Space Complexity
# = O(m) where m is the array of words itself