#1
# a = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)
#2
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [1, 2, 43, 322, 6, 33, 12, 98]
# c = list(set(a) & set(b))
# print(c)
#3
# my_dict = {'one': 1, 'four': 4, 'three': 3, 'five': 5, 'two': 2}
# ascending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# descending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
# print("Сортировка по значению в порядке возрастания:", ascending_sorted_dict)
# print("Сортировка по значению в порядке убывания:", descending_sorted_dict)
#4
# a = {'a': 500, 'b': 5874,  'c': 560,  'd': 400,  'e': 5874,  'f': 20}
# print(sorted(a, key=a.get)[-3:])
#5
a = " dhjshkhds gsd hdskjf"
print(a.count("a"))
#6
# a = input("введите оператичексое выражение + - * / ")
# b = int(input("введите первое число "))
# с = int(input("введите второе число "))
# if a == "+":
#     print("your answer", b + с)
# elif a == "-":
#     print("your answer", b - с)
# elif a == "*":
#     print("your answer", b * с)
# elif a == "/":
#     print("your answer", b / с)
# d = input("хотите добавить еще что-то?  yes/no")
# if d == "yes":
#     r = int(input("введите   первое число "))
#     k = int(input("введите  второе число "))
#     m = input("Доступные операции (**) ")
    
#     print("answer:", r ** k )
# elif d == "no":
#     print("Операция закончена")    
#7
# def check_even_odd():
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         print("odd number")
#     else:
#         print("even number")
#8

# import random
# b = random.randint(1, 100)
# print(b)
# a = int(input("enter number berween 1 from 100 "))
# while True:
#     if b > a :
#         print("bolshwe", b)
#         break
#     elif b < a:
#         print("menshe", b)
#     elif b == a:
#         print("ваше число", a)