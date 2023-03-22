def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x = 0
    cnt = 0

    while x < len(s):
        if s[x].isupper():
            cnt += 1
        x += 1
    return cnt

print(main("CodeschoolUz"))