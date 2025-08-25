# def starshapeB(n):
#     if n == 0:
#         return ""
#     return starshapeB(n - 1) + ("*" * n + "\n")

# def starshapeC(n, i=0):
#     if i == n:      # base case
#         return ""
#     return " " * i + "*" * (n - i) + ("\n" + starshapeC(n, i + 1) if i + 1 < n else "")

def starshapeD(n, i=0, down=False):
    if n <= 0:       
        return ""
    if i < 0:        
        return ""

    line = " " * (abs(i)) + "*" * (n - 2 * abs(i))

    if not down and i < n // 2:
        return line + "\n" + starshapeD(n, i + 1, False)
    elif not down and i == n // 2:
        return line + ("\n" + starshapeD(n, i - 1, True) if i > 0 else "")
    else:
        return line + ("\n" + starshapeD(n, i - 1, True) if i > 0 else "")

print(starshapeD(5))