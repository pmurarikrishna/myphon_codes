import random

def VIT(string):
    if string.isdigit():
        print("The input is an integer")
    else:
        print("The input is a string")

def CSE(n):
    for i in range(n):
        print(random.randint(0,100))

def Python(x):
    i=1
    while i<=x:
        print(i*i+1)
        i+=1

def Language():
    while True:
        string=input("Enter a character: ")
        if string in "aeiou":
            print("The input is a vowel")
        else:
            print("The input is a consonant")
        if string=="exit":
            break  