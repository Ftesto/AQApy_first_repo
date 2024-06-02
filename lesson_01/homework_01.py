# # task 01 == Виправте синтаксичні помилки
# print("Hello", end = " ")
#     print("world!")
#ответ:
print("Hello", end=" ")
print("world!")


# task 02 == Виправте синтаксичні помилки
# hello = "Hello"
# world = "world"
# if True:
# print(f"{hello} {world}!")
#ответ:
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")


# # task 03  == Вcтавте пропущену змінну у ф-цію print
# for letter in "Hello world!":
#     print()
#ответ:
for letter in "Hello world!":
    print(letter)


# # task 04 == Зробіть так, щоб кількість бананів була
# # завжди в чотири рази більша, ніж яблук
# apples = 2
# banana = x
#ответ:
apples = 22
banana = apples * 4
print(banana)


# # task 05 == виправте назви змінних
# 1_storona = 1
# ?torona_2 = 2
# сторона_3 = 3
# $torona_4 = 4
#ответ:
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4


# # task 06 == Порахуйте периметр фігури з task 05
# # та виведіть його для користувача
# perimetery = ? + ? + ? + ?
# print()
#ответ:
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


# """
#     # Задачі 07 -10:
#     # Переведіть задачі з книги "Математика, 2 клас"
#     # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в другому класі
# """
# # task 07
# """
# У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?
#ответ:
apple_trees = 4
peer_trees = apple_trees + 5
plum_trees = apple_trees - 2
count_fruit_trees = apple_trees + peer_trees + plum_trees
print(f"Всего посадили {count_fruit_trees} фруктовых деревьев.")


# """
#
# # task 08
# """
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?
#ответ:
morning_temp = 5
afternoon_temp = morning_temp - 10
evening_temp = afternoon_temp + 4
print(f"Температура вечером составляет {evening_temp} градуса")


# """
#
# # task 09
# """
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?
#ответ:
boys = 24
girls = boys / 2
boys_absent = 1
girls_absent = 2
boys_present = boys - boys_absent
girls_present = girls - girls_absent
total_kids_count = boys_present + girls_present
total_kids_count = int(total_kids_count)
print(f"Cегодня присутсвует {total_kids_count:,} ребенка.")


# """
#
# # task 10
# """
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
#ответ:
first_book_price = 5.7
second_book_price = first_book_price + 2
third_book_price = (second_book_price + first_book_price) / 2
buy_each_book = first_book_price + second_book_price + third_book_price
print(f'Стоимость покупки будет {buy_each_book} грн, если покупать все книги по одной.')


# """
