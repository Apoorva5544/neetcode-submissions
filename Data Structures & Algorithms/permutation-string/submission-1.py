class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1>len2:
            return False

        count1 = Counter(s1)
        count2 = Counter(s2[:len1])

        if count1 == count2:
            return True

        left = 0

        for right in range(len1,len2):
            count2[s2[right]]+=1
            count2[s2[left]]-=1
            left +=1

            if count1 == count2:
                return True

        return False