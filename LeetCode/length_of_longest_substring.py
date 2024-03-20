def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] not in seen:
            max_len = max(max_len, right - left + 1)
        else:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
        seen.add(s[right])

    return max_len
