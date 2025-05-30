# Tạo 1 chức năng tính toán các hình
# - yêu cầu tạo class tên là Geometry => tam giac, vuong, chu nhạt 
# + thuộc tính Pi => instance
# + thuộc tính cạnh của các hình
# + chưc năng tính dien tích các hình

# Tạo 1 hàm runner() để thực thi chức năng tính toán
# Cho phép ngừoi dùng nhập kiểu hình để tinh toán 

class Geometry:
    def __init__(self):
        self.pi = 3.14

        self.triangle_base = None
        self.triangle_height = None
        self.square_side = None
        self.rectangle_length = None
        self.rectangle_width = None
        self.triangle_area = None
        self.square_area = None
        self.rectangle_area = None

    def calculate_triangle_area(self):
        if self.triangle_base is not None and self.triangle_height is not None:
            self.triangle_area = 0.5 * self.triangle_base * self.triangle_height
            return self.triangle_area
        else:
            return "Chưa có đủ thông tin để tính diện tích tam giác."

    def calculate_square_area(self):
        if self.square_side is not None:
            self.square_area = self.square_side**2
            return self.square_area
        else:
            return "Chưa có đủ thông tin để tính diện tích hình vuông."

    def calculate_rectangle_area(self):
        if self.rectangle_length is not None and self.rectangle_width is not None:
            self.rectangle_area = self.rectangle_length * self.rectangle_width
            return self.rectangle_area
        else:
            return "Chưa có đủ thông tin để tính diện tích hình chữ nhật."

    def runner(self):
        choose_shape = input("Chọn hình để tính diện tích (tam giác, vuông, chữ nhật): ").lower()

        if choose_shape == "tam giác":
            self.triangle_base = float(input("Nhập chiều dài đáy tam giác: "))
            self.triangle_height = float(input("Nhập chiều cao tam giác: "))
            area = self.calculate_triangle_area()
            print(f"Diện tích tam giác là: {area}")

        elif choose_shape == "vuông":
            self.square_side = float(input("Nhập chiều dài cạnh hình vuông: "))
            area = self.calculate_square_area()
            print(f"Diện tích hình vuông là: {area}")

        elif choose_shape == "chữ nhật":
            self.rectangle_length = float(input("Nhập chiều dài hình chữ nhật: "))
            self.rectangle_width = float(input("Nhập chiều rộng hình chữ nhật: "))
            area = self.calculate_rectangle_area()
            print(f"Diện tích hình chữ nhật là: {area}")

        else:
            print("Không thể tính toán cho hình này.")

geometry_calculator = Geometry()
geometry_calculator.runner()