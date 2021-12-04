# def divisors(integer):
#     array = []
#     for i in range(2, integer):
#         if integer % i == 0:
#             array.append(i)
#     return f"{integer} is prime" if len(array) == 0 else array


# print(divisors(13))


def ndivisors(integer):
    return [x if integer % x == 0 else f"{integer} is prime" for x in range(2, integer)]


print(ndivisors(13))
