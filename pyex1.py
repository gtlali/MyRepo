intList = [1,2,3,4,5,6,7,8,9] 
squareList = [] 

def square_me( x ):   
    return x * x

#----- for loop---- iterating to method call to square.
for i in intList:
    print( square_me (i)); 
    
#-------------using method called pow----------
for x in intList:
 squareList.append( pow( x, 2 ) ) 
   
print("printing the with pow method",list(squareList))

#------------Same using Map method---------------
squareList = map(square_me, intList);
print("Print by Map:",list(squareList))
