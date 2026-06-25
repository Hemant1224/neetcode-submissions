class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0]*26

            for ch in word:
                count[ord(ch) - ord('a')]+=1

            groups[tuple(count)].append(word) # tuple ..because once made, it can't change
        return list(groups.values())
