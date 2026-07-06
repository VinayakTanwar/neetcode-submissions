class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []

        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())

        cleaned = "".join(cleaned)

        p1 = 0
        p2 = len(cleaned) - 1

        while p1 < p2:
            if cleaned[p1] != cleaned[p2]:
                return False

            p1 += 1
            p2 -= 1

        return True
