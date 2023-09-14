# # Запитуємо в користувача три числа
#
# num1 = float(input("Enter the first number: "))
#
# num2 = float(input("Enter the second number: "))
#
# num3 = float(input("Enter the third number: "))
#
# # Обчислюємо середнє арифметичне значення
#
# average = (num1 + num2 + num3) / 3
#
# # Виводимо результат
#
# print("arithmetic mean:", average)
nums = list(map(int, input("Введите 3 числа через пробел: ").split()))

print(nums)

what = int(input("Максимум - 1 \n Минимум - 2 \n Среднее - 3\n"))

if what == 1:

   print(f"Максимальное: {max(nums)}")

elif what == 2:

   print(f"Минимальное: {min(nums)}")

elif what == 3:

   print(f"Среднее: {sum(nums) / len(nums)}")


for i in range(7 ): # 0, 1, 2, 3, 4
   print("good day")
    print(i, end= "t/" )


massenge = "Good morning"

print(massenge[2])

print(massenge[-2])

print(massenge[0:5])

print(massenge [0:10])

print(massenge [1:12:2])

print(massenge [0:13:2])

print(massenge[::-1])

print(massenge [:12:1])

print(len(massenge))
a = 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10
for element in a:
   if element  <= 6:
      print (element)

meters = float(input("enter meters:"))
print ("1.в милі n2.в дюйми n3.в ярди")
choice = int(input("вибір: "))
if choice == 1:
    print (meters * 0.000621371192)
elif choice == 2:
    print(meters * 39.3700787)
elif choice == 3:
    print(meters * 1.0936133)


a = int(input("Enter number:"))

if a == 1:

   print("Monday")

elif a == 2:

   print("Tuesday")

elif a == 3:

   print("Wednesday")

elif a == 4:

   print("Thursday")

elif a == 5:

   print("Friday")

elif a == 6:

   print("Saturday")

elif a == 7:

   print("Sunday")

a = int(input("a: "))

b = int(input("b: "))

if a != b and a < b:

   print(str(a) + " " + str(b))

elif a != b and a > b:

   print(str(b) + " " + str(a))

else:

   print("a = b")




