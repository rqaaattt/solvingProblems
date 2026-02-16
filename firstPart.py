import random
import math
n = int(input())
array = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]

#task19
# for i in range(n):
#     print(min(array[i]), max(array[i]))

#task20
# for i in range(n):
#     for j in range(n):
#         if i%2==0:
#             array[j][i] = 0
#         else:
#             array[j][i] = 1

for row in array:
    print(row)
    









# array = [
#     [1, 1, 0, 1, 0], #4
#     [1, 0, 1, 0, 1], #3
#     [0, 1, 0, 1, 0], #2
#     [1, 0, 1, 0, 1], #3
#     [0, 1, 0, 1, 0]  #4
# ] #0, 4
# n = 5

#task16
# strikeArray = []
# curStrike = 0
# maxStrike = 0
# for i in range(n):
#     curStrike = 0
#     for j in range(n-1):
#         if array[i][j] == array[i][j+1]:
#             curStrike+=1
#         else:
#             if curStrike>maxStrike:
#                 maxStrike = curStrike
#                 strikeArray = []
#                 strikeArray.append(i)
#             elif curStrike==maxStrike:
#                 strikeArray.append(i)
#             curStrike = 0
#     if curStrike>maxStrike:
#         maxStrike = curStrike
#         strikeArray = []
#         strikeArray.append(i)
#     elif curStrike==maxStrike:
#         strikeArray.append(i)
# if maxStrike == 0:
#     print("нет стрика больше 1 раза")
# else:
#     for i in range(len(strikeArray)):
#         strikeArray[i] = strikeArray[i]+1
#     print(f"стрик в следующих номеров строчек: {strikeArray}")









#task super
# n = int(input())
# result = [[0, 0, 0] for i in range(math.ceil(n/3))]
# cur, next = 1, 1
# for i in range(len(result)):
#     count = 0
#     while count < 3 and n!=0:
#         result[i][count] = cur
#         cur, next = next, cur+next
#         count+=1
#         n-=1
# isOdd = True
# for i in range(len(result)):
#     if isOdd == True:
#         count = 0      
#         while count < 3 and n!=0:
#             result[i][count] = cur
#             cur, next = next, cur+next
#             count+=1
#             n-=1
#         isOdd = False
#     else:
#         count = 2
#         while count >=0 and n!=0:
#             result[i][count] = cur
#             cur, next = next, cur+next
#             count -=1
#             n-=1
#         isOdd = True




# n = len(array)

# task1
# for row in array:
#     print(row)
# count = 0
# for i in range(n):
#     for j in range(c):
#         if j>i and array[i][j]>0:
#             count+=1
# print(count)

# task2
# for i in range(n):
#     for j in range(c):
#         if array[i][j] < 0:
#             array[i][j] = abs(array[i][j])

# task3
# for i in range(n):
#     avg = 0
#     for j in range(c):
#         avg += array[i][j]
#     print(f"среднее значение {i+1}-строки: {avg/c}")

# task4
# maxSum, curSum, result = 0, 0, 0
# for i in range(n):
#     curSum = 0
#     for j in range(c):
#         curSum += array[i][j]
#     if curSum>maxSum:
#         maxSum = curSum
#         result = i+1
# print(result)

# task6
# result = True
# for i in range(n):
#     for j in range(c):
#         if array[i][j] != array[j][i]:
#             result = False
#     if result == False:
#         print("no")
#         break
# if result == True:
#     print("yes")

# task7
# for i in range(n):
#     array[i].sort()

# task8
# minSum, curSum, row = 9999999999999, 0, 0
# for i in range(n):
#     curSum = 0
#     for j in range(с):
#         curSum += array[i][j]
#     if curSum < minSum:
#         minSum = curSum
#         result = i
# del array[result]

# task9
# for i in range(n):
#     maxElsArray = []
#     maxEl = max(array[i])
#     for f in range(c):
#         if maxEl == array[i][f]:
#             maxElsArray.append(f)
#     for k in range(len(maxElsArray)):
#         array[i][maxElsArray[k]] = 0
    
# print()
# for row in array:
#     print(row)

# task10
# avgSum, count = 0, 0
# for i in range(n):
#     for j in range(c):
#         avgSum += array[i][j]
# avgSum = avgSum/(n*c)
# for i in range(n):
#     for j in range(c):
#         if array[i][j] > avgSum:
#             count+=1
# print(avgSum, count)
# 


#task11
# for i in range(n):
#     for j in range(c):
#         if (i+j)%2!=0:
#             array[i][j] = 1

#task12
# for i in range(n):
#     for j in range(c):
#         if (i==j) or (i+j == n-1):
#             array[i][j] = 1
#         else:
#             array[i][j] = 0

#task13
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             array[i][j] = 1

#task14
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if array[j][i] % 2 == 0:
#             count+=1
#     print(f"1-столбец {count}")
    
#task15
# for i in range(n):
#     for j in range(n):
#         if array[i][j] < -50:
#             array[i][j] = 0




