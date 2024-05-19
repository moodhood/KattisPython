import math

#root number 1 is 1/1, where the top is p and the bottom is q
#the left child is p/(p+q) and the right child is (p+q)/q
#F(1 )= 1/1, F(2) = 1/2, F(3) = 2/1, F(4) = ...

#the sample input that kattis wants is the first line is a single integer which represents the number of data sets that is yet to come
#then the sets contain two integers the first one representing the identifing number and the second one representing n

#read the first line 
number_of_data_sets = int(input())
#loop number_of_data_sets amount of times so that we get all the data we that has been given to us
#we need to split the two strings then convert them to an integer by using map
#then store them in a touple 
first_element_of_tuple = []
second_element_of_tuple = []
for i in range(number_of_data_sets):
    data_sets = tuple(map(int, input().split()))#first input is split into a list of substrings, then all the substrings are turned into integers and lastly they are stored in tuples.
    first_element_of_tuple.append(data_sets[0]) #make a list of all the first elements of the touple 
    second_element_of_tuple.append(data_sets[1]) #make a list of all the second elements of the touple

#we are going up the tree and remembering the path we took by checking each number if it is odd or even
#if even then it is a L if odd then it is a R to indecate whether or not we go left or right. 
#each direction is appended on to the stack (mystack)
    
mystack = []

def upthetree(n):
    if((n % 2) == 0):
        mystack.append('L')
    else:
        mystack.append('R')

def fraction_function(n): #we make a function so that we can loop it later on
    #loop the function 'upthetree' until we reach n=1
    while(n != 1):
        upthetree(n)
        n = math.floor(n/2) #return the parent so that we can keep going up the tree, floor(n/2)
    #now we know the path from the beginning node (1/1) to the node we must update p and q as we go down the path
    p,q = 1,1
    while(len(mystack) != 0):
        direction = mystack.pop()
        if(direction == 'L'): #if we go left p = p and q = p + q
            p = p
            q = p + q
        else: #if we go right q = q and p = p + q
            q = q
            p = p + q
    return p,q

for i in range (0, len(second_element_of_tuple)):
    p, q = fraction_function(second_element_of_tuple[i])
    print(f"{first_element_of_tuple[i]} {p}/{q}") #last things last we print the identifing number and p / q
    



        



