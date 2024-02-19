print("here we  will discuss about Dictionary in data type")

print("*****************************************************************************")

print("A dictionary is a key-value pair set arranged in any order. It stores a specific value for each key, like an associative array or a hash table.")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

print("The comma (,) and the curly braces are used to separate the items in the dictionary.")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

d = { 0:'yes', 1:'niranjan', 2:'vikrant', 3:'puru', 4:'vijay'}

print(d, type(d))

print(d)
# Accesing value using keys  
print("the first name is " +d[1])

print("the second name is " +d[2])

print("the fourth name is " +d[4])
print("the frist name is " +d[0])
#find key which is in use..
print(d.keys())    
# it will show value of keys
print(d.values())    
print (d[0])
