s = "aaabb"
k = 3

def longestSubstring( s: str, k: int) -> int:
    if not s: return 0
    for c in set(s):
        if s.count(c) < k:
            max_len = 0
            for t in s.split(c):
                print(s.split(c))
                curr_len = longestSubstring(t, k)
                if curr_len > max_len:
                    max_len = curr_len
            return max_len
    return len(s)

print(longestSubstring(s, k))

