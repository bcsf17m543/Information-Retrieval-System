# preprocessing
import numpy as np
def convert(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j]=lst[i][j].lower()

def ignore(usr_inp,vocab):
    temp=set(usr_inp)
    temp=temp.intersection(vocab)
    temp =list(temp)
    return temp        


def Convert(string): 
    li = list(string.split(" ")) 
    return li

def MakeVector(usr_lst,dict):
    vec=np.zeros((1,len(dict)),dtype=int)
    for i in range(vec.shape[0]):
        for j in range(vec.shape[1]):
            if (d2[j] in usr_lst):
                vec[i][j] = 1
    vec = np.reshape(vec,(len(dict),1)) 
    return vec

def RetResult(mtrx,usr_matt,fileContent):
    usr_matt=np.dot(mtrx,usr_matt)
    #print(type(usr_matt))
    #print(usr_matt)
    temp=usr_matt.flatten()
    temp=list(temp)
    temp2=list(range(len(temp)))
    mytuple=[(temp2[i], temp[i]) for i in range(0, len(temp2))]
    mytuple=sorted(mytuple, key=lambda x: x[1])
    mytuple=mytuple[::-1] 
    for i in range(len(mytuple)):
        print(fileContent[mytuple[i][0]])

def IgnoreDeli(lst):
    for i in range(len(lst)):
        lst[i]=lst[i].strip(".")

files = ("f1.txt", "f2.txt", "f3.txt")
my_set = set()
lst=[]
num = 0  # number of files
for i in files:
    num = num+1
    f = open(i, "r")
    if f.mode == 'r':
        contents = list(f.read().split())
        IgnoreDeli(contents)
        lst.append(contents)
        for j in contents:
            my_set.add(j.lower())    
    f.close()
#print(my_set)
# inverted indices , 2 dictionaries
d1 = {item:val for val,item in enumerate(my_set)}
#print(d1)
d2={v:k for k,v in d1.items()}
#print(d2)
var=len(d2)
my_matt =np.zeros((num,var),dtype=int)
#print(my_matt)
#print(lst[0][0])
#print(my_matt)
convert(lst)
#print(lst)
for i in range(my_matt.shape[0]):
    for j in range(my_matt.shape[1]):
        if (d2[j] in lst[i]):
            my_matt[i][j] = 1
#print(my_matt)            
usr_inp=input("write something :")
usr_lst=Convert(usr_inp)
#print(type(usr_inp),type(usr_lst))
usr_lst=ignore(usr_lst,my_set)
usr_lst=MakeVector(usr_lst,d2)
RetResult(my_matt,usr_lst,lst)
