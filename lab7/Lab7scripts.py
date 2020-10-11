import numpy as np 
length = input("How many integers will you enter: ")
n = 0
evn = 0
a = np.zeros(int(length), dtype=np.int64)
while n < int(length):
    ui = input("Enter number " + str(n+1) + " : ")
    a[n] = ui
    if int(ui) % 2 == 0:
        evn += 1
    n += 1
print(a)
np.sort(a)
odd = 0
odd = int(length) - evn
print("Your array in order is ", a, ".")
print("Your array has ", evn," even numbers and ",odd, " odd numbers.")
t = 0
for x in a:
    t = t + x
print("The total value of the array is ", t, ".")
avg = t/int(length)
print("The mean value of the array is ", avg, ".")
