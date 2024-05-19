matrix = []
for lines in range(0,5):
    matrix.append(list(map(int,input().split())))  


if(matrix[4][0] == 0): #left
    for j in range (0,4):
        for i in range (0,4):
            if(j + 1 < 4 and matrix[i][j] == matrix[i][j+1]):
                if(j - 1 > -1 and matrix[i][j-1] == 0):
                    matrix[i][j-1] = 2*matrix[i][j]
                    matrix[i][j] = 0
                    matrix[i][j+1] = 0
                else:
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i][j+1] = 0
            elif(j + 2 < 4 and matrix[i][j+1] == 0 and matrix[i][j] == matrix[i][j+2]): 
                if(j - 1 > -1 and matrix[i][j-1] == 0): 
                    matrix[i][j-1] = 2*matrix[i][j] 
                    matrix[i][j] = 0 
                    matrix[i][j+2] = 0
                else: 
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i][j+2] = 0
            elif(j + 3 < 4 and matrix[i][j+1] == 0 and matrix[i][j+2] == 0 and matrix[i][j] == matrix[i][j+3]):
                if(j - 1 > -1 and matrix[i][j-1] == 0): 
                    matrix[i][j-1] = 2*matrix[i][j] 
                    matrix[i][j] = 0 
                    matrix[i][j+3] = 0
                else: 
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i][j+3] = 0

            elif(j - 3 > -1 and matrix[i][j-1] == 0 and matrix[i][j-2] == 0 and matrix[i][j-3] == 0): #no collision
                matrix[i][j-3] = matrix[i][j]
                matrix[i][j] = 0
            elif(j - 2 > -1 and matrix[i][j-1] == 0 and matrix[i][j-2] == 0):
                matrix[i][j-2] = matrix[i][j]
                matrix[i][j] = 0
            elif(j - 1 > -1 and matrix[i][j-1] == 0):
                matrix[i][j-1] = matrix[i][j]
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i][j]
                 


if(matrix[4][0] == 1): #up
    for i in range (0,4):
        for j in range (0,4):
            if(i + 1 < 4 and matrix[i][j] == matrix[i+1][j]): #collision move up and dubble
                if(i - 1 > -1 and matrix[i-1][j] == 0): #move up one
                    matrix[i-1][j] = 2*matrix[i][j] #multiply by 2
                    matrix[i][j] = 0 #replace old spot with 0
                    matrix[i+1][j] = 0
                else: #do not move up 
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i+1][j] = 0
            elif(i + 2 < 4 and matrix[i+1][j] == 0 and matrix[i][j] == matrix[i+2][j]): # [0 x 0 x] = [2x 0 0 0] if left command is given
                if(i - 1 > -1 and matrix[i-1][j] == 0): #move up one
                    matrix[i-1][j] = 2*matrix[i][j] #multiply by 2
                    matrix[i][j] = 0 #replace old spot with 0
                    matrix[i+2][j] = 0
                else: #do not move up 
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i+2][j] = 0
            elif(i + 3 < 4 and matrix[i+1][j] == 0 and matrix[i+2][j] == 0 and matrix[i][j] == matrix[i+3][j]):
                if(i - 1 > -1 and matrix[i-1][j] == 0): #move up one
                    matrix[i-1][j] = 2*matrix[i][j] #multiply by 2
                    matrix[i][j] = 0 #replace old spot with 0
                    matrix[i+3][j] = 0
                else: #do not move up 
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i+3][j] = 0
            elif(i - 3 > -1 and matrix[i-1][j] == 0 and matrix[i-2][j] == 0 and matrix[i-3][j] == 0): #no collision so move up
                matrix[i-3][j] = matrix[i][j]
                matrix[i][j] = 0
            elif(i - 2 > -1 and matrix[i-1][j] == 0 and matrix[i-2][j] == 0):
                matrix[i-2][j] = matrix[i][j]
                matrix[i][j] = 0
            elif(i - 1 > -1 and matrix[i-1][j] == 0):
                matrix[i-1][j] = matrix[i][j]
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i][j]              
                
if(matrix[4][0] == 2): #right
    for j in range (3,-1,-1):
        for i in range (3,-1,-1):
            if(j - 1 > -1 and matrix[i][j] == matrix[i][j-1]):
                if(j + 1 < 4 and matrix[i][j+1] == 0):
                    matrix[i][j+1] = 2*matrix[i][j]
                    matrix[i][j] = 0
                    matrix[i][j-1] = 0
                else:
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i][j-1] = 0
            elif(j - 1 > -1 and matrix[i][j-1] == 0 and matrix[i][j] == matrix[i][j-2]): 
                if(j + 1 < 4 and matrix[i][j+1] == 0): 
                    matrix[i][j+1] = 2*matrix[i][j] 
                    matrix[i][j] = 0 
                    matrix[i][j-2] = 0
                else: 
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i][j-2] = 0
            elif(j - 1 > -1 and matrix[i][j-1] == 0 and matrix[i][j-2] == 0 and matrix[i][j] == matrix[i][j-3]):
                if(j + 1 < 4 and matrix[i][j+1] == 0): 
                    matrix[i][j+1] = 2*matrix[i][j] 
                    matrix[i][j] = 0 
                    matrix[i][j-3] = 0
                else: 
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i][j-3] = 0
            elif(j + 3 < 4 and matrix[i][j+1] == 0 and matrix[i][j+2] == 0 and matrix[i][j+3] == 0): #no collision so move up
                matrix[i][j+3] = matrix[i][j]
                matrix[i][j] = 0
            elif(j + 2 < 4 and matrix[i][j+1] == 0 and matrix[i][j+2] == 0):
                matrix[i][j+2] = matrix[i][j]
                matrix[i][j] = 0
            elif(j + 1 < 4 and matrix[i][j+1] == 0):
                matrix[i][j+1] = matrix[i][j]
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i][j]


if(matrix[4][0] == 3): #down
    for i in range (3,-1,-1):
        for j in range (3,-1,-1):
            if(i - 1 > -1 and i + 1 < 4 and matrix[i][j] == matrix[i-1][j]): #collision 
                if(i + 2 < 4 and matrix[i+1][j] == 0):
                    matrix[i+1][j] = 2*matrix[i][j] #multiply by 2
                    matrix[i][j] = 0 #replace old spot with 0
                    matrix[i-1][j] = 0
                else:
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i-1][j] = 0
            elif(i - 2 > -1 and matrix[i-1][j] == 0 and matrix[i][j] == matrix[i-2][j]): # [0 x 0 x] = [2x 0 0 0] if left command is given
                if(i + 1 < 4 and matrix[i+1][j] == 0): #move up one
                    matrix[i+1][j] = 2*matrix[i][j] #multiply by 2
                    matrix[i][j] = 0 #replace old spot with 0
                    matrix[i-2][j] = 0
                else: #do not move up 
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i-2][j] = 0
            elif(i - 3 > -1 and matrix[i-1][j] == 0 and matrix[i-2][j] == 0 and matrix[i][j] == matrix[i-3][j]):
                if(i + 1 < 4 and matrix[i+1][j] == 0): #move up one
                    matrix[i+1][j] = 2*matrix[i][j] #multiply by 2
                    matrix[i][j] = 0 #replace old spot with 0
                    matrix[i-3][j] = 0
                else: #do not move up 
                    matrix[i][j] = 2*matrix[i][j]
                    matrix[i-3][j] = 0
            elif(i + 3 < 4 and matrix[i+1][j] == 0 and matrix[i+2][j] == 0 and matrix[i+3][j] == 0): #no collision so move up
                matrix[i+3][j] = matrix[i][j]
                matrix[i][j] = 0
            elif(i + 2 < 4 and matrix[i+1][j] == 0 and matrix[i+2][j] == 0):
                matrix[i+2][j] = matrix[i][j]
                matrix[i][j] = 0
            elif(i + 1 < 4 and matrix[i+1][j] == 0):
                matrix[i+1][j] = matrix[i][j]
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i][j]


for i in range (0, 4):
    print(f'{matrix[i][0]} {matrix[i][1]} {matrix[i][2]} {matrix[i][3]}')




