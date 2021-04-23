# cummulative indexing over double loop

# here, index in the inner for statement is counted cummulatively
# over the outer for statement.


''' method 1 '''

index = [] # it remembers the last counting at each end of the inner for statement

for i in range(5):
    for j in range(10):
        
        if i == 0: # ingnore the first element "0" in index
            j += 1
            index.append(j)
            
        else: # start counting from 1
            j = index[-1] # fetch the last counting number from the previous inner for loop
            j += 1
            index.append(j)
        
print(j)
print(len(index))
print(index)


''' method 2 '''

index = [0]

for i in range(5):
    for j in range(10):
        j = index[-1]
        j += 1
        index.append(j)
        print(j)
        
print(index)

