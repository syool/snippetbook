import os, sys
os.chdir('/home/user/Downloads')

writing_wo_breaks = []
    
with open('Blood.txt', 'rt', encoding='cp949') as input:
    for line in input:
        line = line.lstrip().rstrip() # remove line spaces from head and tail of a sentence
        writing_wo_breaks.append(line) # contain all sentences in a list
            
    for i in range(len(writing_wo_breaks)):
        if writing_wo_breaks[i] == '': # detect all '' in the list
            writing_wo_breaks[i] = '\n\n' # replace '' into double line breaks

result = ''.join(writing_wo_breaks) # convert the list into a string
# print(result)

input.close()

with open('Tear_new.txt', 'w', encoding='cp949') as output:
    output.write(result) # save the result
    
output.close()
