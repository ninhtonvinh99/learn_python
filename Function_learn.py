# Function cu phap lam quen


"""def greet(name):
    # ham nay se hien thi cau chao
    print("Hello, chao "+ name +". Rat vui khi gap bạn ! ")
greet('Ninh') """

# Ham return

""" def absolute(n): # tinh gai tri tuyet doi cua 1 so
    if (n>=0 ) :
        return n
    else :
        return -n
print(absolute(2))
print(absolute(-4)) """

# Pham vi cua bien

""" def phamvi():
    n=10
    print(n)
phamvi() # gttri ben trong funciton 
n = 20
print(n) # gatri ben ngoai function  """

# Thuc hanh ham

# vd1 : in ra các so chia het cho 5 tu 1 den 100

""" def chia_het_cho_5(n) :
    if (n%5 == 0 ):
        return True
    else:
        return False
for i in range (1, 101) :
    if chia_het_cho_5(i) :
        print(i, end = ' ') """

# vd 2 : Dem tong va in ra cac so nguyen to tu 1 - 100

""" def check_snt(n) :
    if(n == 2) :
        return True
    elif(n==1) :
        return False
    else :
        for  i in range (2, n):
            if (n % i == 0) :
                return False
                break
    return True 
cout = 0
for i in range(1 ,101):
    if check_snt(i) :
        print(i, end = ' ')
        cout += 1
print(".")
print('So các snt la '+ str(cout)) """

# Gtri mac dinh cua tham so

""" def greet(name = 'Ninh'):
    print("Xin chao ", name)
greet()
greet('Ha') """

# Tham so o gioi han :
def greet(*names):
    for name in names:
        print("Hello", name )

greet("Ninh" , "Ha")

