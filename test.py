import os

strA = "hellow"
print(strA)

f = open("E:/파이썬새파일입니다..txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.write(strA)
f.close()



