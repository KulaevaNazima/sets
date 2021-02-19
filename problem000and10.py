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