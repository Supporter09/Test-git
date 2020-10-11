# Lớp cha
class Car:

     # Constructor
     def __init__(self, hangxe, tenxe, mausac):
        # Lớp Car có 3 thuộc tính: tenxe, mausac, hang xe
        self.hangxe = hangxe
        self.tenxe = tenxe
        self.mausac = mausac

     # phương thức
     def chayxe(self):
        print ("{} đang chạy trên đường".format(self.tenxe))

     def dungxe(self, mucdich):
        print ("{} đang dừng xe để {}".format(self.tenxe, mucdich))

# Lớp Toyota mở rộng từ lớp Car.
class Toyota(Car):

     def __init__(self, hangxe, tenxe, mausac, nguyenlieu):
 # Gọi tới constructor của lớp cha (Car) 
        # để gán giá trị vào thuộc tính của lớp cha.
        super().__init__(hangxe, tenxe, mausac)

        self.nguyenlieu = nguyenlieu

     # Kế thừa phương thức cũ
     def chayxe(self):
        print ("{} đang chạy trên đường".format(self.tenxe))

     # Ghi đè (override) phương thức cùng tên của lớp cha.
     def dungxe(self, mucdich):
        print ("{} đang dừng xe để {}".format(self.tenxe, mucdich))
        print ("{} chạy bằng {}".format(self.tenxe, self.nguyenlieu))

 # Bổ sung thêm thành phần mới 
     def nomay(self):
        print ("{} đang nổ máy".format(self.tenxe))

toyota1 = Toyota("Toyota", "Toyota Hilux", "Đỏ", "Điện")
toyota2 = Toyota("Toyota", "Toyota Yaris", "Vàng", "Deisel")
toyota3 = Toyota("Toyota", "Toyota Vios", "Xanh", "Gas")

toyota1.dungxe("nạp điện")
toyota2.chayxe()
toyota3.nomay()
