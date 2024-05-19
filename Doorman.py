
#Pre condition: string is given containing W's and M's, and an integer,
#integer tells what the maximum difference between M's and W's can be



MyQueue = [] 
Largest_Absolute_difference = int(input())
String = list(input())
for char in String:
    MyQueue.append(char)

#A count for the difference between the men and women and a count for both
Difference, Men_Count, Women_Count = 0, 0 ,0
#To keep count of the score:


#make a loop from the beginning to the end  
for i in range(0, len(MyQueue)):
    if(Difference == Largest_Absolute_difference):
        if(MyQueue[i] == 'M'):
            if(Men_Count < Women_Count):
                Men_Count += 1
                Difference = abs(Men_Count - Women_Count) #the absolute value of the men and women, also known as the difference
            else:
                if(MyQueue[i+1] == 'W'): #since we can look one spot ahead
                    Women_Count += 1
                    Difference = abs(Men_Count - Women_Count) 
                    MyQueue[i+1] = 'Used' #mark the used spot so we can identify and use it later on
                else:
                    print(Men_Count + Women_Count) #print the score since we can't do anything from this point and terminate the program
                    quit()
        else:
            if(Men_Count > Women_Count):
                Women_Count += 1
                Difference = abs(Men_Count - Women_Count)
            else:
                if(MyQueue[i+1] == 'M'):
                    Women_Count += 1
                    Difference = abs(Men_Count - Women_Count)
                    MyQueue[i+1] = 'Used'
                else:
                    print(Men_Count + Women_Count) 
                    quit() 

    else: #check if the threshold has been violated
        if(MyQueue[i] == 'Used'): #if it is used then we have to look back one spot because we cannot look two spots a head
            if(MyQueue[i-1] == 'M'):
                Men_Count += 1
            else:
                Women_Count += 1
        else:    
            if(MyQueue[i] == 'M'): 
                Men_Count += 1
            else:
                Women_Count += 1

        Difference = abs(Men_Count - Women_Count) 
print(Men_Count + Women_Count)
