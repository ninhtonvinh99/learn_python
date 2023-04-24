# Hàm tính điểm trung bình học sinh

# Nhập tên học sinh , điểm

"""toan = 0
ly = 0
hoa = 0
def nhap_du_lieu() :
    global toan, ly , hoa
    toan = float(input("Diem toan la : "))
    ly = float(input("Diem ly la : "))
    hoa = float(input("Diem hoa la : "))
    # tinh diem trung binh
    avr = round((toan + ly + hoa) / 3,2)
    return avr
def hien_thi(tb) :
    print ("Diem trung binh la : " + str(tb))
    if(tb < 5 ):
        print("Hoc luc kem ")
    elif (tb >= 5 and tb < 7):
        print("Hoc luc tb ")
    elif(tb >= 7 and tb < 8.5):
        print("Hoc luc kha")
    else:
        print("Hoc luc gioi")
tb = nhap_du_lieu()
hien_thi(tb) """

# Hàm tính tổng các số nguyên tố từ 0 -> 100

"""my_list = []

def check_snt(n):
    check = 1
    if ( n == 0 or n == 1 ) :
        check = 0
    elif( n ==2  ):
        check =1
    else :
        for i in range(2,n):
            if (n%i==0):
                check = 0
                break
    if (check==1):
        return n
def list_snt(x1, x2):
    for i in range(x1,x2+1):
        my_list.append(check_snt(i))
def sum (my_list) :
    s = 0
    for i in range (0,len(my_list)):
        s += my_list[i]
    return s
list_snt(0,1000)
my_list = list(filter(lambda x : x is not None, my_list))
print(my_list)
print(sum(my_list))"""

"""print("Bài tập Python dùng hàm tính tổng các SNT từ 0 - 1000")

def check_snt(n) :
    check = 1
    if (n< 2 ) :
        check = 0
    elif(n == 2) :
        check = 1
    elif(n%2 == 0 ):
        check = 0
    else :
        for i in range (3, n, 2) :
            if(n% i == 0):
                check = 0
                break
            else:
                check =1
    return check
s = 0
for i in range (0,1001 ) :
    if(check_snt(i)):
        print(i)
        s += i
print(s)"""

# Tìm giá trị lớn nhất trong 3 số

"""def find_max(list):
    max = list[0]
    for i in range (0, len(list)):
        if (list[i] > max ):
            max = list[i]
    return max
list = []
n = int(input("So cac so :"))
for i in range (0, n) :
    list.append(int(input(" nhap so thu "+str(i+1) + " : ")))
print("So lon nhat la : " )
print(find_max(list))"""

# In ra thong tin Sinh vien : thực hành hàm lambda

"""def create_student(name):
    return lambda infor : name + " " + infor # hàm tạo đối tương student
name = input("Nhap ho va ten : ")
student = create_student(name)
print(" Nhap tuoi : ")
print(student(input()))
print("Nhap gioi tinh : ")
print(student(input()))
print("Nhap quoc tich : ")
print(student(input()))
# với cùng tên , có thể dùng hàm nhiều lần , ý nghĩa lambda"""

# Hàm đệ quy tính tổng S = 1 + 2 + 3+ 4 + .. +n

"""def sum(n) :
   if(n==1):
       return 1
   return n + sum(n-1)
n = int (input(" Nhap n = "))
tong = sum(n)
print(tong)"""







