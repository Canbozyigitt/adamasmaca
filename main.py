# tek çift olduğunu belirt 
my_list=[1,2,3,4,5]
for number in my_list:
    if number%2==0:
        print("çift    " + str(number))
    else:
        print("tek     "+str(number))    

my_list2="metalica"
new_list=[number for number in my_list2]
print(new_list)