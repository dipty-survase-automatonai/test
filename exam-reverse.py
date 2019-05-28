import io
import re
fname=input("enter filename:")
f=open(fname)
line=f.readline()
#print(line)
while line != "":
        y = line[::-1]
        print(y)
        line= f.readline()
