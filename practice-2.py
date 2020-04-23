
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

from statistics import mean


condition = [x for x in range(1500, 2701) if x % 7 == 0 and x % 5 == 0 ]
print(condition)



#Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius


#Write a Python program to guess a number between 1 to 9

n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


for i in range(4):
    for j in range(i+1):
        print('* ',end="")
    print("")
for i in range(5):
    for j in range(5-i):
        print("* ",end="")
    print("")

n=range(10)
print(mean(n))


p=range(10)
def cal_avg(num):
    sum_num=0
    for t in num:
        sum_num=sum_num+t

    avg=sum_num/(len(num)+1)
    return avg

print("average is ",cal_avg(p))


p=range(10)
def cal_avg(num):
    sum_num=0
    i=0
    for t in num:
        sum_num=sum_num+t
        i=i+1
    avg=sum_num/i
    return avg

print("average is ",cal_avg(p))




for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

#Print multiplication table of 24, 50 and 29 using loop.
n=[24,50,29]
r=[29,45,55,66]
l=[1,2,3,4,5]


def random_table(p):
    result=[]
    i = range(1, 11)
    for x in p:
        for j in i:
            y=x*j
            j=j+1
            result.append(y)
    return result

print(random_table(n))
print(random_table(r))



# Python program to find H.C.F of two numbers

# define a function


#Write a program to calculate factorial of a number.

n=range(20)
k=range(35)



def factor(num):
    s=1
    for i in range(num):
        s=s*(i+1)
        #print("i=",i)
    return s
for a in k:
    print(factor(a))



def HCF(x,y):
    if x<y:
        smaller=y
    else:
       smaller=x

    for i in range(1,smaller+1):
        if ((x%i==0) and (y%i==0)):
            hcf=i
    return hcf

num1=80
num2=28

print("hcf is", HCF(num1,num2))



#Take integer inputs from user until he/she presses q ( Ask to press q to quit after integer input ). Print average and product of all numbers.























