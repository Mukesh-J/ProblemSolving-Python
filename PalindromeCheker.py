def is_palindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    test_str = "A man, a plan, a canal: Panama"
    print(f"Is the string '{test_str}' a palindrome? {is_palindrome(test_str)}")
