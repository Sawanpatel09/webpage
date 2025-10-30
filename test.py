# list1 = [-10,-12,-1,0,1,2,2,2,-1,-12]
# k = 3
# max1_list = []
# max1 = list1[0]
# min1_list = []
# min1 = list1[0]
# for i in range(k):
#     max1_flag = False
#     min1_flag = False
#     for j in range(len(list1)):
#         if max1_list == []:
#             if list1[j] > max1:
#                 max1 = list1[j]
#         if max1_list != [] and max1_flag == False:
#             if list1[j] < max1_list[-1]:
#                     max1_list.append(list1[j])
#                     max1_flag = True
#         elif max1_flag == True:
#              if max1_list[-2] > list1[j] > max1_list[-1]:
#                   max1_list[-1] = list1[j]
#         if min1_list == []:
#              if list1[j] < min1:
#                   min1 = list1[j]
#         if min1_list != [] and min1_flag == False:
#              if list1[j] > min1_list[-1]:
#                   min1_list.append(list1[j])
#                   min1_flag = True
#         elif min1_flag == True:
#              if min1_list[-2] < list1[j] < min1_list[-1]:
#                   min1_list[-1] = list1[j]
             
#     if max1_list == []:
#         max1_list.append(max1)
#     if min1_list == []:
#          min1_list.append(min1)


# dict1 = {}
# for i in list1:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#          dict1[i] += 1

# man_max1 = []
# man_min1 = []
# for item in min1_list:
#      for j in range(dict1[item]):
#           man_min1.append(item)
# for item in max1_list:
#      for j in range(dict1[item]):
#           man_max1.append(item)

# print(man_max1[k],man_min1[k])
          

    
    







'''list1 = [1,2,3,4,5,6,7,8]
k = 3
k1 = k
i = 0
j = len(list1) - 1
if k > len(list1)//2:
    k = len(list1)//2
while i < k:
    list1[i], list1[j] = list1[j],list1[i]
    i = i + 1
    j = j - 1
k = k1
print(list1)
for i in range(k):
    for j in range(0,len(list1)-k - i - 1):
        list1[j+1],list1[j] = list1[j],list1[j+1]
i = len(list1) - k
j = len(list1) - 1

while i < j:
    list1[i],list1[j] = list1[j],list1[i]
    i= i + 1
    j = j - 1
print(list1)'''







'''# list1 = [1,2,3,4,5,6,7,8,9,10,12,34,87,56]
list1 = [10,9,8,7,6,5,4,3,2,1]
var = list1[-1]
half = len(list1)//2

list1[0:half],list1[half:len(list1)] = list1[half:len(list1)],list1[0:half]
# print(list1)
i = 0
for j in range(half,len(list1)):
    list1.insert(i , list1[j])
    list1.pop(j)
    i= i + 2
list1[-1] = var
print(list1)'''

print("Main branch updated")
