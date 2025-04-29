
def lengthOfLongestSubstring(self, s: str) -> int:
    seen = []
    max = 0
    count = 0
    for char in str(s):
        while char in seen:
            seen.pop(0)
            count = count - 1
        seen.append(char)
        count += 1
    if count > max:
        max = count
    return max

// time complexity: O(n^2)
// when we see a duplicate character, we remove all the characters from the left until we remove the duplicate character
// In this way we need to scan the string multiple times, so the time complexity is O(n^2)