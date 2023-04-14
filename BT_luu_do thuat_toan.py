
# BT 1 : Kiem tra du lieu la number hay string

"""data  = 1
print ('Kieu du lieu của data :  ' + str(type(data))) """

""" user_input = input("Nhập : ")

print("\n")
try:
    val = int(user_input)
    print("Dữ liệu nhập vào là int = ", val)
except ValueError:
    try:
        val = float(user_input)
        print("Dữ liệu nhâp vào là float = ", val)
    except ValueError:
        print("Dữ liệu nhập vào không phải là number") """

# BT 2 : Tinh tong S(n) = 1 + 2 + 3 + ... +n

""" n = input("n = " )
n = int(n)
S = 0
for i in range(1,n+1) :
    S += i
print(" tong = " + str(S)) """

# Bt 3 : Tinh tong S9n0 = 1^1 + 2^2 + ... +n^n

"""n = input("n = " )
n = int(n)
S = 0
for i in range(1,n+1) :
    S += pow(i,2)
print(" tong = " + str(S)) """

# BT 4 :tinh tong S(n) = 1 + 1/2 +1/3 + ... +1 /n

"""n = input("n = " )
n = int(n)
S = 0
S = float(S)
for i in range(1,n+1) :
    S += 1/i
print(" tong = " + str(S)) """

# BT 5 : tinh tong S9n0 =  1/2 + 1/4 + ... +1/2n

"""n = input("n = " )
n = int(n)
S = 0
S = float(S)
for i in range(1,n+1) :
    if i % 2 ==0 :
        S += 1/i
print(" tong = " + str(S)) """

# BT6 tinh tong S(n) = 1/3 + 1/5 +... + 1/(2n+1)

"""n = input("n = " )
n = int(n)
S = 0
S = float(S)
for i in range(3,n+1) :
    if i % 2 == 1 :
        S += 1/i
print(" tong = " + str(S)) """

# BT 7 : Tim uoc so của so nguyen duong n

"""n = input("n = " )
n = int(n)
list = [ ]
for i in range (1,n+1) :
    if n%i == 0 :
        list.append(i)
print ('uoc cua '+str(n) +" la : ")
for i in range(0,len(list)) :
    if i != len(list)-1 :
       print(list[i], end = ',' )
    else:
        print(list[i], end= '.') """

# BT 8 : Tinh tong cac uoc so cua so nguyen duong n

"""n = input("n = " )
n = int(n)
list = [ ]
for i in range (1,n+1) :
    if n%i == 0 :
        list.append(i)
S = 0
for i in range(0,len(list)) :
    S+= list[i]
print('Tong cac uoc la: '+str(S) )"""

# tim uoc so le lon nhat cua mot so

# tu code , qua phuc tap
"""n = input("n = " )
n = int(n)
list = [ ]
for i in range (1,n+1) :
    if n%i == 0 :
        list.append(i)
list_odd = []
for i in range(0,len(list)) :
    if list[i] % 2 != 0 :
        list_odd.append(list[i])
max = list_odd[0]
for i in range(1,len(list_odd)) :
    if list_odd[i] > max :
        max = list_odd[i]
print("Uoc so le lon nhat la : "+str (max))"""

# fix: nen dung vong lap giam dan
"""n = input("n = " )
n = int(n)

for i in range (n+1, 1, -1 ) :
    if(n % i == 0 and i%2 != 0) :
        print ("Max cua uoc so le : " + str(i))
        break """

# BT 9 : Kiem tra so hoan hao

"""n = input("n = " )
n = int(n)
S = 0
for i in range(1,n):
    if(n%i == 0) :
        S+= i
if(S == n):
    print(str(n) + " la so hoan hao ")
else :
    print(str(n) + " ko la so hoan hao ") """

# BT 10 : Kiem tra so chinh phuong

""" n = input("n = " )
n = int(n)
check = 0
for i in range(1,n+1) :
    if (i**2 == n ) :
        check = 1
        break
if(check == 1) :
    print(str(n) + ' la so chinh phuong' )
else :
    print(str(n) + 'ko la so chinh phuong') """

#BT 11 : Kiem tra so nguyen to

"""n = input("n = " )
n = int(n)
check = 1
for i in range(2,n) :
    if (n%i == 0 ) :
        check = 0
        break
if(check == 1) :
    print(str(n) + ' la so nguyen to' )
else :
    print(str(n) + ' ko la so nguyen to') """

# bt 14 : Dao nguoc 1 so : VD 123 -> 321

#C1
""" n = input("n = " )
list = []
for i in range(len(n), 0, -1) :
    list.append(n[i])
for i in range(0,len(list)) :
    print(list[i], end = '') """

#C2
""" n = input("n = " )
n = int(n)
while(n != 0) :
    print(n % 10,end = '' )
    n= int(n/10) """

# BT 15 : In ra tung ki tu cua 1 so

""" n = input("n = " )
list = []
for i in range(0, len(n)) :
    list.append(n[i])
for i in range(0,len(list)) :
    if (i != len(list)-1):
        print(list[i], end = '-')
    else :
        print(list[i]) """

# BT 16 : giai pt bac 1

""" a = int(input('a = '))
b = int(input('b = '))

if (a == 0 and b == 0 ) :
    print('PT vo so nghiem ')
elif(a==0 and b!= 0) :
    print ('PT vo nghiem')
else :
    print ('P co nghiem duy nhat: '+ str(-b/a)) """

# Bt 17 : Giai pt bac 2 :

""" import math
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

delta = b**2 -4*a*c

if (delta < 0  ) :
    print('PT vo  nghiem ')
elif(delta == 0 ) :
    print ('PT co  nghiem kep : ' + str(-b/(2*a)))
else :
    print ('P co 2 nghiem : ')
    print ('x1 = ' + str((-b+math.sqrt(delta))/(2*a)))
    print ('x2 = ' + str((-b-math.sqrt(delta))/(2*a))) """

