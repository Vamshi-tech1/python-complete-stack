# Break and Continue #
# for i in range(5):
#     if i==3: if condition becomes true it exits
#         break
#     print(i)



# for i in range(10):
#     if i==5: #if condition becomes true it skipped
#         continue
#     print(i)


#simple for loops
# example 1: for over range

# for i in range(5):
#     print(f"i = {i}") # i is constant and {i} this i value changes


#example 2: for over a list

# nums = [10, 20, 30]
# for n in nums:
#     print(f"n = {n}") # n is constant and {n} this n value changes


# example 3: for over a string

# s = "Hi"
# for char in s: # char takes 'H', then "i"
#     print(char)

# for with if, break,continue
# example 4: continue to skip values

# for i in range(1,6):
#     if i%2 ==0:
#         continue # skip the true value and continue
#     print(i)


#example 5: break to stop early
# for i in range(10):
#     if i==4:
#         break   # if true exit the loop
#     print(i)


#example 6:
# Alternative prime numbers average is printed
# def is_prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     else:
#         return False
#
# s=int(input())
# e=int(input())
# c=ac=0
# sum=0
# for i in range(s,e+1):
#     b=is_prime(i)
#     if b==True:
#         c+=1
#         if c%2==1:
#             sum+=i
#             ac+=1
# print(sum/ac)



