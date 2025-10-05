# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n == 1:
        return "*"
    result = ""
    for i in range(n):
        result += "*"
    result += "\n"

    for j in range(n-2):
        result += "*"
        for k in range(n-2):
            result += " "
        result += "*\n"
    
    for i in range(n):
        result += "*"

    return result

    
# 1
# 12
# 123
# 1234
def number_pattern(n):
    pattern = ""
    for i in range(1, n+1):
        for j in range(1, i+1):
            pattern += str(j)
        pattern += "\n"
    
    return pattern.rstrip()

    # result = 1
    # pattern = ""
    # while result <= n:
    #     i = 1
    #     while i <= result:
    #         pattern += str(i)
    #         i += 1
    #     pattern += "\n"
    #     result += 1
    # return pattern.rstrip()


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******


def centered_star_pyramid(n):
    if n <= 0:
        return ""
    result = ""
    for i in range (n):
        for j in range(n-1-i):
            result += " "
        for k in range(i*2 + 1):
            result += "*"
        result += "\n"
    return result.rstrip()
            


# print (hollow_square(5))
# print(number_pattern(4))
# for i in range(4):
#     print(i)
# print(sum_of_natural_numbers(0))
print(centered_star_pyramid(4))