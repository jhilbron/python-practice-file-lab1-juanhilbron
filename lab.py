# correct: sum then divide by count 
def average(a, b, c,):
    return (a + b + c) / 3 # ✅

print(average(4, 6, 8))
#correct answer 



#1 Write a function double(x) that returns x * 2. Call it with 5 — what do you get? 

def double(x):
    return x * 2

result = double(5)
print(result)


#2 This code has a semantic bug — find it and fix it: def area(w, h): return w + h (should calculate rectangle area)
-The bug in your code is that it uses addition (+) instead of multiplication (*).

def area(w, h):
    return w * h


#3 Trace this by hand — write what happens each step:
a = 10 → b = a - 3 → print(b)

a = 10
Action: The computer creates a variable named 
Memory: It stores the integer value 10 inside that variable.
Current State: a is 10.

b = a - 3
Action: The computer looks up the value currently stored in a (10).
calculation: It performs the subtraction: 10 - 3.
Assignment: It creates a new variable named b and stores the result (7) in it
Current State: a is 10, b is 7.

print(b)
Action: The computer looks up the value of b.
Output: It sends the value 7 to the console/screen.

#4 True or False: A program with a semantic error will always crash with an error message.
False 
