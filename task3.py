#Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это слово палиндромом. Выведите YES или NO.
#При решении этой задачи нельзя пользоваться циклами, в решениях на питоне нельзя использовать срезы с шагом, отличным от 1.

slovo = str(input("Введите слово в английской раскладке:"))
a = slovo[::-1]
if slovo == a:
  print("YES")
else:
  print("NO")