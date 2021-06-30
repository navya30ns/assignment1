#Mississippi (program1)
str1=input("Please enter a string: ")
str2=str1.lower()   #making string case insensitive.
list1=list(str2)
new=[]
for i in list1:
    if i not in new:
        new.append(i)
        count=0
        for j in range(len(list1)):
            if i==list1[j]:
                count+=1
        print(f"{i} = {count}")