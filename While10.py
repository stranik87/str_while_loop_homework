def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x = 0
    cnt = 0

    while x < len(s):
        if int(s[x])%2 == 1:
            cnt += int( s[x])
        x += 1
    return cnt

print(main("98421"))