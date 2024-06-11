year = int(input("Năm sinh của bạn là: "))
can =["Canh ","Tân ","Nhâm ","Quý ","Giáp ","Ất ","Bính ","Đinh ","Mậu ","Kỷ "]
chi =["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
s = []
x = year % 10
y = year % 12
s = can[x] + chi[y]
print(s)