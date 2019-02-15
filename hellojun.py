'''
for i in  range(1,10):
	for j in range(0,i):
		if (i%3==1):
			print('李',end='')
		elif(i%3==2):
			print("汉",end='')
		else:
		    print ("俊",end='')
	print('\n')
'''
#creat a list

list=[]
for i in range(1,11):
	list.append(i)

name=input("please input the num you want to find in list\n")

if(int(name) in list):
	print("the name ",name," is in the list",list)
else:
	print("the name ",name," is not in the list",list)

name2=input("please enter the name you want to delete\n")

if(int(name2) in list):
	list.remove(int(name2))
	print("the name ",name2," was delete the list",list)
	print("the len of the list is",len(list))
else:
	print("the name ",name2," is not in the list",list)

##creat a dictionary 
dict= {}
for i in range(1,11):
	index=str(i)+str(i+1)
	lt=[i,i+1]
	dict.setdefault(index,lt)   # add the key and value to the dic if the key do not in it ,it will creat it 
print(dict)

dict2=dict.fromkeys(list,0) # the second parament is the initial value
key2=dict2.keys()
print("the key of dict2 is\n",key2)

dict.update(dict2)
value=dict.values()
n=input("please input the key you want to delete: ")
value2=dict.pop(n,-1)
print("the key ",n,"was delete and his value is ",value2)
print(dict.pop(100,-1))

print(dict)
tup=dict.items()
print("the total item of dict is",tup)

print("the value of dict:\n",value)
## about the checkout 's usage 
#when you just not  add to stage,you can use checkout -- filename to return the former file remenber the there is a space between - and filename
# when you didnot commit just add to stage,then you wanto  repeal ,you must use the command "git reset HEAD filenaem",then input "git checkout -- filename"