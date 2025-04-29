def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # charToNextIndex stores the index after current character
        charToNextIndex = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1

        return ans

// time complexity: O(n)
// whenerver we see a duplicate character, we move the left pointer to the right of the last occurrence of that character
// In this way we onlu need to scan the string once, so the time complexity is O(n)
