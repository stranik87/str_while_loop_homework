def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x = 0
    cnt = 0

    while x < len(s):
        if s[x].isdigit():
            cnt += 1

        x += 1
    return cnt

print(main("python 2023"))