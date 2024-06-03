# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
#ответ:
alice_in_wonderland = """\"Would you tell me, please, which way I ought to go from here?\"
\"That depends a good deal on where you want to get to,\" said the Cat.
\"I don't much care where ——\" said Alice.
\"Then it doesn't matter which way you go," said the Cat.
\"—— so long as I get somewhere," Alice added as an explanation.
\"Oh, you're sure to do that," said the Cat, "if you only walk long enough.\""""
print(alice_in_wonderland)

# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
#
#
# """
#     # Задачі 04 -10:
#     # Переведіть задачі з книги "Математика, 5 клас"
#     # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в п'ятому класі
# """
# # task 04
# """
# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?
# """
#oтвет:
print(f'Площадь Черного и Азовского морей составляет {436402 + 37800}км2')


#
# # task 05
# """
# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.
# """
#ответ:
total_count = 375291
first_and_second_warehouse_count = 250449
second_and_third_warehouse_count = 222950
third_warehouse_count = total_count - first_and_second_warehouse_count
second_warehouse_count = second_and_third_warehouse_count - third_warehouse_count
print(f'\tЕсли общее количество товара на складах равно {total_count}'
      f'\nтогда кодичество товара на третем складе будет равно разнице общего '
      f'\nи количества товаров на первом и втором складах'
      f'\n{total_count} - {first_and_second_warehouse_count} = {third_warehouse_count} товаров'
      f'\n\tЧтобы найти количество товаров на втором складе нужно'
      f'\nиз количества на 2м и 3м складах вычесть количество на 3м складе'
      f'\n{second_and_third_warehouse_count} - {third_warehouse_count} = {second_warehouse_count}')




# # task 06
# """
# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.
# """
#
#ответ
print(f'Чтобы вычислить стоимость компьютера, '
      f'\nнужно умножить сумму ежемесячного платежа на количество месяцев'
      f'\n1179 * 18 = {1179 * 18}грн')


# # task 07
# """
# Знайди остачу від діленя чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9
# """
#
#ответ
# Task 07
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f'a) Залишок від ділення 8019 на 8: {a}')
print(f'b) Залишок від ділення 9907 на 9: {b}')
print(f'c) Залишок від ділення 2789 на 5: {c}')
print(f'd) Залишок від ділення 7248 на 6: {d}')
print(f'e) Залишок від ділення 7128 на 5: {e}')
print(f'f) Залишок від ділення 19224 на 9: {f}')



# # task 08
# """
# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн
# """
#
#ответ
pizza_large_price = 274
pizza_large_qty = 4
pizza_medium_price = 218
pizza_medium_qty = 2
juice_price = 35
juice_qty = 4
cake_price = 350
cake_qty = 1
water_price = 21
water_qty = 3

total_cost = (pizza_large_price * pizza_large_qty +
              pizza_medium_price * pizza_medium_qty +
              juice_price * juice_qty +
              cake_price * cake_qty +
              water_price * water_qty)

print(f'Загальна вартість замовлення Іринки: {total_cost} грн')





# # task 09
# """
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?
# """
#
#ответ
photos = 232
photos_per_page = 8
pages_needed = (photos + photos_per_page - 1) // photos_per_page

print(f'Ігорю знадобиться {pages_needed} сторінок, щоб вклеїти всі фото')





# # task 10
# """
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?
# """
#ответ
# Task 10
distance = 1600
fuel_per_100km = 9
tank_capacity = 48

fuel_needed = (distance / 100) * fuel_per_100km
stops_needed = (fuel_needed // tank_capacity) + (fuel_needed % tank_capacity != 0)

print(f'Для подорожі знадобиться {fuel_needed:.0f} літрів бензину')
print(f'Потрібно заїхати на заправку щонайменше {stops_needed:.0f} разів')

