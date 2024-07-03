my_dict = {"Катя":1982,"Leo":2010}
print(my_dict)
print(my_dict["Катя"])
my_dict["Olya"] = 1950
print(my_dict)
my_dict.update({"Sacha":1986,"Vika":1950})
a= my_dict.pop("Vika")
print(a)
print(my_dict)


my_set ={12,10,1,8,10,"string",(1,2,3)}
print(my_set)
list_ = [7,8,9,10]
print(set(list_))
my_set.update({5,11})
print(my_set)
my_set.remove(8)
print(my_set)
