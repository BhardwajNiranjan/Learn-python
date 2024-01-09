print("----------------- Sequence -------------------------")
print("-------------- Type of Sequence - String, List and Touple --------------")

print("*****************************************************************************")

print("----------> Third is Touple <----------")
print("a tuple is like a list. Tuples, like lists, also contain a collection of items from various data types. A parenthetical space () separates the tuple's components from one another.")

tup  = ( "hello", "niranjan", "vijay", "vikrant", 10.34,  2) 
print(tup , type(tup)) 
print(tup)
# Tuple slicing  
print (tup[1:4])    
print (tup[2:5]) 
# Tuple concatenation using + operator  
print (tup + tup)   
# Tuple repatation using * operator   
print (tup * 3)     
# Adding value to tup. It will throw an error.  
tup[2] = "hi"  