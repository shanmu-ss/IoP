# for i in range(2):
#     for j in range(3):
#         print(f"i={i}, j={j}")
#
# numbers = [1,2,3,4,5,6]
# # even_numbers = [x * 3 for x in numbers if x % 2 ==0]
# # print(even_numbers)
# labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
# print(labels)

myList = [1,2,3,4,5,6,7,8,9,10,12,15,16,20,43,29]

print(f'even number: {[n for n in myList if n % 2 == 0]}')
print(f'odd number: {[n for n in myList if n % 2 != 0]}')
print(f'Divisible by 3 & 4 {[n for n in myList if n % 3 == 0 and n % 5==0]}')