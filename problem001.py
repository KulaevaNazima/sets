farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_3 = farm_1.union (farm_2)
print (farm_3)
farm_4 = farm_1.difference (farm_2)
print (farm_4)
farm_5 = farm_2.difference (farm_1)
print (farm_5)