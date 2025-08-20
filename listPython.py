# #create a list of 5 numbers . Print the sum, max and min using for looping

# list1=[1,2,3,4,5]
# largest=list1[0]
# minimum=list1[0]
# for i in list1:
#     if i>largest:
#         largest=i
# print(f"The largest number in the list is : {largest}")

# #minimum element:
# for i in list1:
#     if i<minimum:
#         minimum=i
# print(f"The minimum of the list is : {minimum}")

# # sum of the number in the list:
# Sum=0

# for i in list1:
#     Sum+=i
# print(f"The sum of the given number is : {Sum}")

# list1=[1,2,3,4,5,6]
# list1.append(4)
# list1.append(5)
# list1.append(8)
# list1.append(9)
# list1.append(10)
# print(f"The New list after appending some element : {list1}")

#todo Remove a specific element from a list

# list1=[1,2,3,4,5,6]
# list1.remove(3)
# print(list1)

#!Reverse a list using slicing
# list1=[1,2,3,4,5]
# print(list1[::-1])


#?ifnd the index of an element in alist
# list1=[1,2,3,4,5,6]
# print(list1.index(3))


#count how many times a specific element appears in a lsit
# list1=[1,2,3,2,3,2,4,52,3,2,4,2,6]
# print(f"the total number appears in lsit : {list1.count(2)}")

# list1=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(list1)):
#     if list1[i]%2==0:
#         list1[i]=0
# print(list1)
        

#!merge two lsits withour using concatenate
# l1=[1,2,3,4,5,6]
# l2=[4,5,6,7,8]
# l1.extend(l2)
# print(f"After merging the Lists are : {l1}")


#check given list is merged or not

# list1=[1,2,2,3,5]
# is_sorted=True
# for i in range(len(list1)-1):
#     if list1[i]>list1[i+1]:
#         is_sorted=False
#         break
# if is_sorted==True:
#     print(f"The given list are sorted : {list1}")
# else:
#     print(f"The given lists are not sorted : {list1}")

# for pattern programming

# for i in range(6,-1,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")

# for i in range (0,6):
#     for j in range(0,6):
#         if(i==0 or i==5 or j==0 or j==5):
#             print(j,end=" ")
#         else:
#             print(" " , end=" ")
#     print("")    

        
        
# tuple1=(1,2,3,4,5,6,"hello")
# if "hello" in tuple1: 
#     print("yes")
# else:
#     print("No")
set1={1,2,3,4,1,2,6,7}
print(set1)  # it can be ignore the multiple duplicates value in sets data structure 
