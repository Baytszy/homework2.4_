# for i in 1,2,3,4:
#     print(i)
#
# list_ = ['one', 'two', 'three']
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
# print(list_)

# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):
#     print(list_[i])

# list_2 = [2,3,4,5,1]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
# print(sum_)


# for i in range(1, 11): #start, stop, step i = 1, 2, 3 ...
#      for j in range(1,11): #j = 1
#         print(f'{i} x {j} = {i * j}')
# print(i)

# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i, k in dict_.items():
#     print(i, k)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# for i in numbers:
#     if i % 2 == 0:
#         primes.append(i)
#     else:
#         not_primes.append(i)
# print('Primes: ', primes)
# print('Not Primes; ', not_primes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    count = 0
    if i == 1:
         continue
    for k in range(1, i+1):
        if i % k == 0:
            count += 1
            if count == 3:
                not_primes.append(i)
                break
    if count != 3:
        primes.append(i)

print(f"Составные числа: {not_primes}")
print(f"Не составные числа: {primes}")














