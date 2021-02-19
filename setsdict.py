# problem 0


# problem1
'''
items= {numbers = {1, 2, 3}, names = {"Vlad", "Ali", "Mike"}, fruits = {"apple", "lemon", "watermelon"}}
print (items)
'''
'''
# problem 2
farm_1= {"dog", "cat", "mouse", "sheep"}
farm_2= {"cow", 'horse', "donkey", "cat", "dog"}
print (farm_2.difference (farm_1))
'''

'''
# problem 3
pets = {"dog", "cat", "mouse", "elephant", "horse"}
print (pets)
pets.add ("leon")
print (pets)
pets.pop ()
print (pets)
'''
'''
 # problem 000 and 10
menu = {"lagman": 120, "plov": 120, "borsh": 100}
print (menu.items ())
menu.update ({"besh_barmak":130})
print (menu.items ())
menu ["lagman"] = 135
print (menu.items ())
del menu ["borsh"]
print (menu.items ())
menu.update ({"drinks" : ["Coca-Cola", "Sprite", "Fanta"]})
print (menu.items ())
'''
'''
# problem 020
methods_sets= {"add", "remove", "clear", "update", "difference", "discard", "intersection", "intersection_update", "pop"}
methods_dict= {"clear", "keys", "items", "get", "values", "update"}
print (methods_sets.intersection (methods_dict))
'''
'''
# problem 31
a= {}
for i in range (3):
  keys= input ("Введите имя ")
  pas = input ("Введите пароль")
  a.update ({keys:pas})
  print (a)
 '''

'''
# problem 27
professions = {"robert dauni":"actor",
               "beyonce": "singer",
               "mike tayson": "boxer",
               "putin": "prezident",
               "guzal": "doctor"}
for name, professions in professions.items():
 print(f"Здравствуйте {name.title()} Прекрасная профессия {professions.title()}")
 '''

'''
# problem 22
a_set = set ()
for i in range (10):
  item = int (input ("Введите число "))
  a_set.add (item)
a_tup= tuple (a_set)
print (a_tup)
'''
'''
#problem 11
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
set1=set (south_american_countries)
print (set1)
print (list (set1))
'''
'''
suitcase= []
for i in range (5):
	things= input ("Положите вещь в свой чемодан: ")
	suitcase.append (things)
	print (suitcase)
suitcase.pop (2)
print (suitcase)
'''
'''
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_3 = farm_1.union (farm_2)
print (farm_3)
farm_4 = farm_1.difference (farm_2)
print (farm_4)
farm_5 = farm_2.difference (farm_1)
print (farm_5)



