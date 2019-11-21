#operation performed on a string

#to accept the string from the user
string=raw_input("Enter string:")
count1=0
count2=0
for i in string:
#calculation of number of upper and lower case letters
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
print("the length of the string is:")
print(len(string)) 

#print the reverse of the string

def reverse(string): 
    if len(string) == 0: 
        return string 
    else: 
        return reverse(string[1:]) + string[0] 
  

print ("The original string  is : ",string) 
print (string) 
  
print ("The reversed string(using recursion) is : ") 
print (reverse(string)) 
