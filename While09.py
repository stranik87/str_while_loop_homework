def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x = 0 
    cnt = 0

    while x  < len(s):
        if s[x].isdigit():
            cnt += int( s[x])

        x += 1
    return cnt

print(main("987654"))