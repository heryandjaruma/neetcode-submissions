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
            
            # normalize the inner w frozenset to be converted into key
            hashKey = frozenset(inner)
            if hashKey not in outer:
                outer[hashKey] = [word]
            else:
                outer[hashKey].append(word)
        
        returnVal = []
        for key, words in outer.items():
            arrWords = []
            for word in words:
                arrWords.append(word)
            returnVal.append(arrWords)
        
        return returnVal