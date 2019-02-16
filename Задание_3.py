# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x_1 = float(input("Enter x1: "))
y_1 = float(input("Enter y1: "))
x_2 = float(input("Enter x2: "))
y_2 = float(input("Enter y2: "))

k = (y_2 - y_1)/(x_2 - x_1)
b = (x_1 * y_2 - x_2 * y_1)/(x_1 - x_2)

if b == 0:
    print ("y = %rx" % (k))
elif k == 0:
    print ("y = %r" % (b))
elif b > 0:
    print ("y = %rx+%r" % (k, b))
else:
    print ("y = %rx%r" % (k, b))
