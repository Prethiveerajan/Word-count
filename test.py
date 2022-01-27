#devolped by: prethiveerajan P
#reg no: 21500340
num_words =0
with open('help.txt','r') as file1:
    for i in file1:
        word =i.split()
        num_words += len(word)
print("Number of words={}".format(num_words))
