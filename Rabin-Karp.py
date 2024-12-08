def rabin_karp(pattern, text, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    h = pow(d, m - 1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            t = t + q if t < 0 else t

    return -1

# Example usage
text = "GEEKS FOR GEEKS"
pattern = "FOR"
print("Pattern found at index:", rabin_karp(pattern, text))
