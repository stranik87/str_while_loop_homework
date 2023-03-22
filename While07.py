def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x = 0
    cnt = 0

    while x < len(s):
        if int( s[x])%2 == 0:
            cnt += 1
        x += 1
    return cnt

print(main("123456"))