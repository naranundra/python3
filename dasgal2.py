# хүний нас өгөгдсөн бол насанд хүрсэн эсэхийг ол
n = int(input())
if n >=0:
    if n <=18:
        print("насанд хүрсэн хүн")
    else:
        print("хүүхэд")
else: 
    print("эерэг тоо оруулна уу")
    
# хялбар
n = int(input())
if n < 0:
    print("хүүхэд")
elif n<18: 
    print("хүүхэд")
else:
    print("насанд хүрсэн")