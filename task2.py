# 1. print 1 to 50
for i in range(1, 51):
    print(i)

# 2. even numbers 1-100
for i in range (2,101,2):
    print(i)
# 3. odd numbers 1-100
for i in range (1,101,2):
    print(i)

# 4. table of 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# 5. sum 1-100
total = 0
for i in range(1, 101):
    total += i  
print("Sum;",total)

#reverse 50 to 1
for i in range(50, 0, -1):
    print(i)

# 7. count number divisible by 3 
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("count:", count)

#8.squares 1-10
for i in range(1, 11):
    print(i*i)

#9. cubes 1-10
for i in range(1,11):
    print(i**3)

# 10. input n 
n = int(input("Enter a n: "))
for i in range(1, n+1):
    print(i)

# while loop

#11. 1 to 20
i = 1
while i <= 20:
    print(i)
    i += 1
#12. factorial
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1          
print("Factorial:", fact)

# reverse number 
num = int(input("Enter a number: "))
reverse = 0 
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
    print("Reverse:", reverse)

# 14. count digits
num = int(input("Enter a number: "))
count = 0       
while num > 0:
    num //= 10
    count += 1
print("Count of digits:", count)


#15. stop input
while True:
    text = input("Enter something (type 'stop' to end): ")
    if text.lower() == 'stop':
        break

# 18. tables 1-5
for i in range(1,6):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
        print()

#20. 1-9 grid

num =1 
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

# 21. count characters
s = input("Enter a string: ")
count = 0
for i in s:
    count += 1
print(count)


#22. count vowels
vowels = 'aeiouAEIOU'
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel count:", count)

# 23. count consonants
count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1
        print("Consonant count:", count)

#24. reverse string
reverse = ""
for ch in s:
    reverse = ch  + reverse
print("Reverse string:", reverse)


#25. palindrome
if s == s[::-1]:
    print("Palindrome") 
else:    
    print("Not a palindrome")


s = input("Enter a string: ")
print(s[:5])  
print(s[-3:])
print(s[::-1])
print(s[::2])
print(s[1::-1])

# 31. sum of list
lst = [1,2,3,4,5]

print(sum(lst))
print(min(lst))
print(max(lst))


count = 0
for i in lst:
    count += i
    print(count)

x = int(input("Enter a number: "))
if x in lst:
    print("Exists")
else:
    print("Not exists")


# list operation

lst =[1,2,3]

lst.append(4)
lst.append(5)
lst.append(6)
print(lst)

lst.insert(1,10)
print(lst)


lst.remove(3)
print(lst)


rev = []
for i in lst:
    rev = [i] + rev
print(rev)

lst = [5,2,8,1]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)










