# Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs with value above 2000 will be taken to the new dictionary.
# dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
# dict2={}

dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={key:value for key,value in dict1.items() if value>2000 }
print(dict2)