def sumMainDiagonal(matrix): 
    n = len(matrix) # получаем размерность матрицы
    return sum(matrix[i][i] for i in range(n)) # получаем сумму элементов по размерности матрицы

matrix = [
    [10, 2, 3],
    [4, 10, 6],
    [7, 8, 10],
] # вводим тестовую матрицу
print(sumMainDiagonal(matrix)) 