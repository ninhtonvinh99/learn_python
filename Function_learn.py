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
""" def greet(*names):
    for name in names:
        print("Hello", name )

greet("Ninh" , "Ha") """

# Ham de quy

# Ham tinh day fibo cua 1 so
""" def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("Dãy fibo của ", num, "là ", calc_factorial(num)) """

# kHU DE QUY

""" num = 4
result = 1;
for i in range(1, num + 1):
    result = result * i

print("Kết quả khử đệ quy là: ", result) """

# Ham an danh

""" double = lambda x : x*2
print(double(4)) """

# dùng lambda trong 1 function khác
""" def myfunc(n):
    return lambda a : a * n

# Biến mydoubler lúc này sẽ là một lambda function
mydoubler = myfunc(2)

# Vì vậy bạn có thể gọi thoải mái và nhiều lần ở nhièu vị trí
# Và vẫn kế thừa giá trị n của hàm myfunc
print(mydoubler(11)) # Kết quả 22
print(mydoubler(10)) # Kết quả 20 """

"""def myfunc(n , a ) :
    return a*n
print(myfunc(2,2))"""

# kết hợp với hàm filter

# Hàm filter có công dụng là lọc dữ liệu theo tham số truyên vào
# tham số đầu tiên là hàm kiểm tra điều kiện lọc : True giữ lại, False lọc
# tham số thứ hai là dữ liệu cần lọc.
# hàm filter trả ra 1  iterator chưá các ptu được lọc, cần dùng list() or tuple() để sử dụng

# VD lọc số chẵn trong 1 list

"""my_list = [1, 3, 4,6,8, 10 ]
list1 = list(filter(lambda x : (x%2==0), my_list))
print(list1)"""

# Kết hợp vói hàm map ()

# Hàm map có công dụng là lặp qua từng phần tử và thay đổi giá trị của nó dựa vào hai tham số
# tham số đầu tiên là một hàm dùng để xử lý dữ liệu và trả kết quả về
# tham số thứ hai là dữ liệu cần lặp.

# VD dùng nhân đôi các giá trị cả các ptu trong list

""" my_list = [ 1, 2, 3,4]
list1 = list(map(lambda x : x*2,my_list))
print(list1) """

# biến toàn cục và biến cục bộ

# Global Variable

""" x = "Học Python tại Freetuts.net"
def foo():
    print("Trong hàm:", x)
foo()
print("Ngoài hàm:", x) """

# Local variable
""" def foo():
    y = "local"

foo()

# Lệnh này sai vì biến y không tồn tại
print(y) """

# từ khóa global

x = "global"

""" def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()
foo() # Khi chúng ta thay đổi giá trị cho biến global tong hàm 
      # thì gá trị của biến đó thay đổi theo """



