def count_paren(n, l=0, r=0):
    if l == n and r == n:
        return 1
    total = 0
    if l > r:
        total += count_paren(n, 1, r + 1)
    if l < n:
        total += count_paren(n, l + 1, r)
    return total

def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs -1) + ways(stairs - 2)

print("ways(5) = ", ways(5), "count_paren(5) = ", count_paren(5)) 