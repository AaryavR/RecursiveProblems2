def count_paren(n, l=0, r=0):
    if l == n and r == n:
        return 1
    total = 0
    if l > r:
        total += count_paren(n, 1, r + 1)
    if l < n:
        total += count_paren(n, l + 1, r)
    return total

input("Count_paren counts ever valud {} sequence - return 1 at each valud end. Press enter")
print(" count_paren(1) =", count_paren(1))
print(" count_paren(2) =", count_paren(2))

n = int(input("Enter number of pairs (try 3 or 4): "))
guess = input("What is count_paren(" + str(n) + ")? ")
print(" count paren(" + str(n) + ") =", count_paren(n), "your guess: ", guess)
