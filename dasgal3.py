# хүний нэр өгөгдсөн бол 2 оос дээш а үсэг орсон эсэхийг шалга
ner = input("нэр ээ оруулна уу:")
c = ner.count("a")
print(c)

ner = input("нэр ээ оруулна уу:")
c = ner.count("a")
if c>2:
    print("2-оос олон а үсэг орсон")