def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs -1) + ways(stairs - 2)

input("ways counts every distinct path up n stairs - 1 step or 2 steps at a time. Press enter")
print(" ways(3) = ", ways(3))

n = int(input("Enter the number of stairs: "))
print("ways(" + str(n) + ") =", ways(n))