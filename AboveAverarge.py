C = int(input())
for data in range (0,C):
    data = input()
    numbers_list = [int(num) for num in data.split()]
    numberofstudents = numbers_list[0]
    count = 0
    for i in range(1,numberofstudents+1):
        count += numbers_list[i]
    average = count / numberofstudents
 
    highercount = 0
    for i in range(1,numberofstudents+1):
        if(numbers_list[i] > average):
            highercount += 1

    solution = (highercount/numberofstudents) * 100

    rounded = round(solution, 3)  # Round to three decimal places
    formatted = "{:.3f}".format(rounded)  # Ensure at least three decimal places
    print(f'{formatted}%')



