class FourCal:
     def add():
         result = a + b
         print(result)
     def mul():
         result = a * b
         print(result)
     def sub():
         result = a - b
         print(result)
     def div():
         result = a / b
         print(result)

a,b = map(int, input().split())
n = input()

if n == "+":
    FourCal.add()
if n == "*":
   FourCal.mul()
if n == "-":
    FourCal.sub()
if n == "/":
    FourCal.div()