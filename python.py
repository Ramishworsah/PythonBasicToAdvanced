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

print(dir(list))

l1=[1,2,3,4]
l2=[1,2,3,4,5,6,7,8,9,10]
# extended
l1.extend(l2)

l1.remove(2) 
print(l1)
l1.insert(2,98)
print(l1)