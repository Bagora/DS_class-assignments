def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right

# Test example 1
x = 4
result = mySqrt(x)
print("Example 1:")
print("Input:", x)
print("Output:", result)

# Test example 2
x = 8
result = mySqrt(x)
print("Example 2:")
print("Input:", x)
print("Output:", result)
