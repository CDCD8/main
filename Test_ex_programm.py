#программа пишущая значение переменной в верхнем и нижнем регистрах
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#программа выводящая полное имя в правильной формулеровке
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
massege = f"Hello, {ful_name.title()}!"
print(massege)

#программа выводяшая набор слов с всевозможными смещениями
print("Languages: \n\tPython \n\tC \n\tJavaScript")

#программа исключающая пропуск из сроки
favorit_language = "python "
favorit_language = favorit_language.rstrip()
print(favorit_language)

#apostrophe.py
massege = "One of Python's strenghs is its diverse community"
print(massege)

#приветственное сообщение для пользователя
name = "Jony"
massege = "Hello,"
print (massege + name.title)

#операции с именами 
name = "Jony"
print(name.upper) 
print(name.lower)
print(name.title)

#числа 
number = (2+3)*4
print (number)

#дробные числа 
number = (0.6 + 0.6)*2
print(number)

#вещественные числа
num = 8/2
number = num + 2
print(number)

#множественное присвоение 
x,y,z = 0,0,0
print(x)
print(y)
print(z)

#константа
THIS_IS_CONSTANT = 5000
print(THIS_IS_CONSTANT)

#числа упражнение 
print(2+2+2+2)
print(9-1)
print(10+2-4)
print(8+0)

#список велосипедов
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title()) 

#работа со списком велосипедов 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#изменение элементов в списке
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#присоединение элементов в конец списка
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

#добавление в пустой список
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#вставка элементов в список
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#удаление элементов командой del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#удаление элемента командой pop
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#последний мотоцикл
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owent was a {last_owned.title()}.")

#удаление по значению
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#удаление с причиной
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me

#упражение 3
persons = ['Neo', 'Stalin', 'Rusveld']
persons_no = []
persons_no1 = 'Neo'
persons.remove(persons_no1)
persons_no.insert(0, persons_no1)
print(persons)
print(persons_no)

new_person = 'Churchill'
persons.insert(3, new_person)
new_person1 = 'Hitler'
new_person2 = 'Nicson'
new_person3 = 'Seva'
persons.insert(0, new_person1)
persons.insert(3, new_person2)
persons.insert(4, new_person3)
print(persons)

person_popped = persons.pop()
print(f"Dear {person_popped.title()}, can you meet me for lunch today?")
person_popped1 = persons.pop()
print(f"Dear {person_popped1.title()}, can you meet me for lunch today?")
person_popped2 = persons.pop()
print(f"Dear {person_popped2.title()}, can you meet me for lunch today?")
person_popped3 = persons.pop()
print(f"Dear {person_popped3.title()}, can you meet me for lunch today?")
person_popped4 = persons.pop()
print(f"Dear {person_popped4.title()}, can you meet me for lunch today?")
person_popped5 = persons.pop()
print(f"Dear {person_popped5.title()}, can you meet me for lunch today?")

print("Sorry, we haven't got then more table and chair.")
print("And I cann't meet with Seva, Nicson, Hitler and Stalin")

print("I'm sorry")

nnew_person_list = ['Churchill', 'Rusveld']
nnew_person_popped1 = nnew_person_list.pop()
print(f"Dear {nnew_person_popped1.title()}, can you meet me for lunch today?")
nnew_person_popped2 = nnew_person_list.pop()
print(f"Dear {nnew_person_popped2.title()}, can you meet me for lunch today?")
 
print(persons)
print(persons_no)
print(nnew_person_list)
print("SUCCESS")

