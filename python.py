# # def PrimeNumber(num):
# #     count=0
# #     for i in range(1,num+1):
# #         if(num%i==0):
# #             count+=1
# #     if(count==2):
# #         print(num)

# # for i in range(1,15):
# #     PrimeNumber(i)
    
    
# while True:
#     print("Enter a number to check if it is prime or not (or type 'exit' to quit):")
#     print("1. Check Prime Number")
#     print("2. Exit")
#     choice = input("Enter your choice: ")
#     if choice == '1':
#         num = int(input("Enter a number: "))
#         count = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         if count == 2:
#             print(f"{num} is a prime number.")
#         else:
#             print(f"{num} is not a prime number.")
#     elif choice == '2':
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# print(dir(list))

# l1=[1,2,3,4]
# l2=[1,2,3,4,5,6,7,8,9,10]
# # extended
# l1.extend(l2)

# l1.remove(2) 
# print(l1)
# l1.insert(2,98)
# print(l1)


# # help(dict)
# # dict={"name":"sachin","age":22,"city":"pune"}

# # print(dict.pop("age"))  
# # # Removes the key 'age' and returns its value
# # print(dict)

# # dict.popitem()  #remove last item of key-values pairs
# # print(dict)

# # dict.update({"country":"India"})  #add new key-value pair
# # print(dict)1
# # dict.values()
# # # dict.keys()  #returns all keys in the dictionary      
# # # dict.items()  #returns all key-value pairs in the dictionary
# # # dict.get("name")  #returns the value for the specified key'1


# dic={ 1: "one", 2: "two", 3: "three" }
# # while True:
# #     key=input("Enter key (or type 'exit' to quit): ")
# #     if key.lower() == 'exit':
# #         break   
# #     value=input("Enter value: ")
# #     dic[key] = value
# # print("Dictionary contents:" ,dic, end=" ")
# dic1={"name":"sachin","age":22,"city":"pune"}

# dic.update(dic1)  # Merging two dictionaries
# print("Updated Dictionary:", dic)

# students = {"Akhil": 85, "Shivanshu": 90, "Ram": 78}

# for i,j in students.items():
#     if j > 80:
#         print(f"{i} has scored more than 80 marks.")  
# students["Akhil"] = 95  
# print("Updated Students Dictionary:", students)  

# t1=(1,2,3,4,5)
# t2=(1,2,3,4)
# t1=t1+t2  # Concatenating two tuples
# # print("Concatenated Tuple:", t1)
# print(len(t1)) # we can concatenate the tuples but we cannot change the value of the tuple

 
# list1=[1,2,3,4,5]
# MySet = set(list1)
# print(MySet)
# # convert list to set
# MySet.add(6)  
# # MySet.remove(1)
# MySet.discard(2)  
# MySet.clear()  
# dic={}

# while True:
#     key=input("Enter the (for stoping the program to enter exit)")
#     if key.lower() == 'exit':
#         break
#     user=input("Enter the value:")
#     dic[key] = user
#     print("Dictionary contents:", dic, end=" ")

dic={"name":"sachin","age":22,"city":"pune"}
# access using for loop
for i in dic.values():
    print(f"{i}")  # Print key and value pairs


# dic.reduce("age") 
# dic.discard("city")
dic.pop("name")
dic.popitem()  
print(dic)