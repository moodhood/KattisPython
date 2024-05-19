import sys 

for line in sys.stdin: # it will read every line until the end of the file
    numbers_list = []
    for num in line.split():
        numbers_list.append(int(num))#int() is a function that takes in a string and converts it into a integer 
    if(numbers_list[0] > numbers_list[1]):
        print(numbers_list[0] - numbers_list[1])
    else:
        print(numbers_list[1] - numbers_list[0])