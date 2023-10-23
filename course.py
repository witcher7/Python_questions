# # # # save data
# # # # variables ---> storage buckets which stores data

# # # # IN YOUR KITCHEN ---> you use containers to store things
# # # #sugar,salt,biscuts,tea,coffee,maggie,macroni
# # # # IF I WANT TO STORE MY DATA
# # # # VARIABLES

# # # sugar = "SWEET" 
# # # # string data --> ?chrachters, words,alphabets
# # # print(sugar)

# # # munna_bhai = 100
# # # # another way to write variables
# # # # UNDERSCORE_
# # # print(munna_bhai)

# # # # numbers should come after the alphabet
# # # m3unna =120
# # # print(m3unna)

# # # circuit = 200
# # # I am storing 200 in circuit
# # # But I want anyone can give the input

# # # used to write for yourself or people who dont know how to code/program
# # circuit  =float(input("Enter your number : "))
# # # by default --> python takes input as string
# # # typecasting --> forcfully converting data type --> my data type
# # # this is how we take input
# # print(type(circuit))


# # ARITHMETIC OPERATIONS

# # a = int(input("Enter your number : "))
# # b = int(input("Enter your number : "))

# # + --> addition
# # - --> subtraction
# # * --> multiplication
# # / --> division

# # % --> module --> to find remainder

# # # 5%2 --> 1 output
# # # computer is dumb machine
# # a = 5
# # b = 50
# # print(b%a)
# #  # 50 % 5 --> 0 output
# # # 



# # # ** --> power ---> 2**2 --> 2*2 = 4
# # print(ans)

# # IF ELSE --> is a way to make conditions

# # krutika = "ICE CREAM"
# # if krutika == "ICE CREAM":
# #   print("SHE WILL EAT ICE CREAM")
# # else:
# #   print("SHE WILL CRY")

# # # = -> is used to assign a value
# # name = 10
# # chacha = 20
# # # == --> it is used to check that whether the variable has that value or not
# # chacha == 20 # it is asking that hey chacha has 20 or not
# # # if it has 20 then it will print true
# # # if it does not have 20 then it will print false

# # # > --> greater than ?
# # # < --> less than ?
# # # >= --> greater than or equal to ?
# # # <= --> less than or equal to ?
# # # != --> not equal to ?
# ##  == --> is equal to ? 

# # n = 10
# # if n < 5:# false
# #   print("n is greater than 5") # this statement will work
# # else: #this statement will work
# #   print("n is smaller than 5")
# # CALCULATOR
# # num1 = int(input("Enter your number1 : "))
# # num2 = int(input("Enter your number2 : "))
# # operator = str(input("Enter your operator + / * - % : "))
# # # I WANT MORE CONDITIONS

# # if operator == "+": # first condition
# #  print(num1+num2) # this line belongs to 93 line
# # elif operator== "-": # 
# #  print(num2 - num1)
# # elif operator == "/":
# #  print(num1/num2)
# # elif operator == "*":
# #  print(num1*num2)
# # else: # this else will work if nothing will be true be above
# #   print(num1%num2)

# # Write a program to check whether a number is divisible by 7 or not.

# # n = int(input("Enter your number"))
# # if n%7 ==0:
# #   print("It is divisible by 7")
# # else:
# #   print("It is not divisible by 7 ")

# # Write a program to display "Hello" if a number entered by user is a multiple of five , 
# # otherwise print "Bye".
# # n = int(input("Enter your number: "))
# # if n%5==0:
# #   print("Hello")
# # else:
# #   print("Bye")

# # Q8. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
# #              Unit                                                     Price  
# # First 100 units                                               no charge
# # Next 100 units                                              Rs 5 per unit
# # After 200 units                                             Rs 10 per unit

# # list --> data structure which helps to store data at one address or one point of time

# # var = "Rish"
# # print(var)

# # list = ["Rish","Gul","Mahajan","Selmon","Vivek","Shah rukh khan"]
# # INDEX   0     1       2         3      4          5 
# # we are storing multiple elements under a single addresss

# # # print(list[2])
# # # INSERT AN ELEMENT 
# # print(list)
# # list.append("WATERMELON")
# # # nameoflist.append("THE ELEMENT")
# # print(list)


# # LOOPS --> ? 
# # these are nothing just to repeat the code

# # 1.FOR LOOP

# # for i in range(10,20): # python , If you want to include 20 as well then guys you have n+1
# #               #starting ,ending point
# #   print(i)


# # 10 -> 100
# # -10 to 11
# # -13 to -4
# # 0 to 35
# # 85 to -5           # how many steps you want to take decrease or increase the value of i by 1
# # for i in range(85,-6,-5):
# #   print(i)
# # IN WHILE LOOP , IT IS MOST PATHETIC LOOP
# # THIS LOOP DOES NOT HAVE A RANGE
# # n = 10
# # while n>5:# condition  10
# #   print("Hello") # n = 10 -1 -=> 9 8 7 6 5
# #   n = n -1


# # n = int(input())
# # while n >10:
# #   if n ==15:
# #     print("N is 5")
# #   else:
# #     print("N is a different number")

# # Q2. Write a program to print first 10 natural number.
# # Show Answer

# # Q3. Write a program to print first 10 even numbers.
# # Show Answer

# # Q4. Write a program to print first 10 odd numbers.
# # Show Answer

# # Q5. Write a program to print first 10 even numbers in reverse order.
# # Show Answer

# # Q6. Write a program to print table of a number accepted from user.
# # Show Answer

# # n = int(input("Enter your number: "))
# # for i in range(1,11):
# #   # print(n*i)
# #   print( str(n) + "*"+ str(i) + "="+ str(n*i))


# # Q7. Write a program to display product of the digits of a number accepted from the user.
# # Show Answer

# # 4561 --> number that I gave
# # n = int(input("Enter your number: "))
# # ans = 1
# # while n > 0:
# #   last_digit= int(n%10) # get last digit
# #   ans =ans*last_digit # product of numbers
# #   n =int(n/10) # removes last digit

# # print(ans)



# # Q8. Write a program to find the factorial of a number.
# # Show Answer

# # n = int(input("Enter your number: "))
# # ans = 1
# # n = 5
# # # 1,2,3,4,5
# # for i in range(n,0,-1):
# #   ans = ans*i
# #     # ans = 1*5 = 5
# #     # ans = 5* 4 = 20
# #    # ans = 20 * 3 = 60
# #    # ans = 60 *2 = 120
# #    # ans = 120 * 1 = 120
# # print(ans)
# # # 5! == 5 * 4 * 3 * 2 * 1
# # # 10! = 10 * 9 * 8 *7 *6 *5 * 4 *3 *2 * 1


# # Q9. Write a program to find the sum of the digits of a number accepted from user
# # Show Answer

# # # 54321 
# n = int(input("Enter your number : "))
# sum = 0
# while n >0:
#   last_digit = int(n%10)
#   sum = sum +last_digit
#   n = int(n/10)



# # # 54321 --> 
# #    1 
# # # sum = 0 + 1
# #   sum = 1 + 2 = 3
# #   sum  = 3 + 3 = 6
# #   sum = 6+ 4 = 10
# #   sum = 10 + 5 = 15
# # n = int(input())
# # sum = 0
# # for i in range(n,0,-1):
# #   sum = sum + i

# # print(sum)

# # REVISE 5 times --> HOMEWORK

# NOT IT --> whatever I am doing just revise it 5 times

# n = int(input("Enter the length of the list: "))
# list = []
# for i in range(n):
#   take = int(input("Enter your element : "))
#   list.append(take)

# print(list)

# if a user a list --> find maximum element inside the list 

# INPUT --> [10,-3,4,54,100,-35,200]


    
# # OUTPUT --> 200
# n = int(input("Enter the length of the list: "))
# list = []
# for i in range(n):
#   take = int(input("Enter your element : "))
#   list.append(take)

# print(list)
# max = list[0] # assumption

# for i in range(n):
#   if max <list[i]:
#     max = list[i]

# # print("Maximum element is : ",max)

# # minimum element inside the list !!! 
# n = int(input('Enter number: '))
# list =[]
# for i in range(n):
#    take= int(input('enter element: '))
#    list.append(take)

# min = list[0]; # assumption

# for i in range(n):
#     if(min>list[i]): # if min > element[list]
#         min = list[i]   
# print(min)

# # YOU HAVE TO FIND HOW MANY TIMES K is there inside the list
# INPUT --> [1,2,2,3,2,100,2]
#        k = 2 # how many times element is coming

# OUTPUT --> 4

# n = int(input('Enter number: '))
# list =[]
# for i in range(n):
#    take= int(input('enter element: '))
#    list.append(take)

# k = int(input("Enter your K element: "))
# counter = 0
# for i in range(n):
#   if list[i]==k:
    counter = counter +1

# print(counter)

#
list = [10,-3,4,54,100,-35,200]
k = 58
n = len(list)
# n = int(input('Enter number: '))
# list =[]
# for i in range(n):
#    take= int(input('enter element: '))
#    list.append(take)

# k = int(input("Enter your K element: "))
ans = -1
j 
i 
for i in range(n-1):
  # for j in range(i+1,n):
    if list[i]+list[j]==k:
      ans = [list[i],list[j]]
    j =j +1
print(ans)
