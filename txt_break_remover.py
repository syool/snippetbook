import os, sys
os.chdir('/home/user/Downloads')

codec = 'cp949' # cp949, aka UHC is for korean letters. utf-8 is universal.
writing_wo_breaks = []

with open('lady.txt', 'rt', encoding=codec) as input: 
    for line in input: # read sentence by sentence
        line = line.lstrip().rstrip() # remove line spaces from head and tail of a sentence
        writing_wo_breaks.append(line) # put all sentences into a list
            
    for i in range(len(writing_wo_breaks)):
        if writing_wo_breaks[i] == '': # detect all '' in the list
            writing_wo_breaks[i] = '\n\n' # replace '' into double line breaks

# print(writing_wo_breaks)
result = ''.join(writing_wo_breaks) # convert the list into a string
# print(result)

input.close()

with open('output.txt', 'w', encoding=codec) as output:
    output.write(result) # save the result
    
output.close()
