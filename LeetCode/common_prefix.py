def longestCommonPrefix(strs: list[str]) -> str:
    common_prefix = ""
    min_length = min([len(string) for string in strs])
    k = min_length
    while k >= 0:
        prefix = strs[0][:k]
        all_start_with = [string.startswith(prefix) for string in strs]
        if all(all_start_with):
            common_prefix = prefix
            break
        k -= 1
    return common_prefix


a = ["ab", "a"]
common_prefix = longestCommonPrefix(a)
assert common_prefix == 'a'
