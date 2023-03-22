def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x = 0
    cnt = 0

    while x < len(s):
        if s[x].isalpha():
            cnt += 1
        x += 1
    return  cnt

print(main("coder 2022"))