def reshenie(x,y,b):
    if y==len(matrix):
         return x,b
    else:
        for i in matrix[y] :
            x+=i ; b*=i   
        return reshenie(x ,y+1,b)     
     
matrix=[[3,3,3],[1,2,1],[4,4,4,]]
print('сумма матрицы=%d\nпроизведение матрицы=%d' %(reshenie(0,0,1)))
