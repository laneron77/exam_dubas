import datetime
import sys

formats = {"/": "%d/%m/%Y", ".": "%d.%m.%Y"}
#конвератція дати фанкшн
def convert_date(date_str, separator):
  try:
    date_format = formats[separator]  
    date_obj = datetime.datetime.strptime(date_str, date_format)
    return date_obj.strftime("%Y-%m-%d")
  except ValueError:
    return "Невірний формат дати"
#фанкшн на валідність
def is_valid_date(date_str, separator):
  if convert_date(date_str, separator) != "Невірний формат дати":
    return True
  else:  
    return False
#фанкшн для отримання коректної дати
def get_date(separator):
  while True:
    date_str = input(f"Введіть дату ({separator}): ")  
    if is_valid_date(date_str, separator):
      return date_str
    else:
      print("Невірний формат, спробуйте ще раз.")
#вибір сепаратора 
def select_separator():
  print("Виберіть сепаратор:")
  print("1. /") 
  print("2. .")

  separator = input("Ваш вибір: ")
  return separator
  #меню
def menu():
  print("1. Конвертувати дату")  
  print("2. Вихід")

  choice = int(input("Виберіть пункт: "))
  
  if choice == 1:
    separator = select_separator()
  else:  
    separator = ""

  return choice, separator
  #функція для конвертації
def convert():
  choice, separator = menu()  

  if choice == 1:  
    date_str = get_date(separator)
    result = convert_date(date_str, separator)
    print(f"Результат: {result}")

  elif choice == 2:
    sys.exit()

  else:
    print("Помилка, спробуйте ще раз")
    
convert()