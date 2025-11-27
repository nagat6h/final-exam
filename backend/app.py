# قائمة المنتجات والأسعار
products = [ ["منتج 1", 10],
             ["منتج 2", 20],
             ["منتج 3", 30],
             ["منتج 4", 40],
             ["منتج 5", 50]]

# حلقة لا نهائية حتى يدخل رقم صحيح
while True: 
# عرض قائمة المنتجات
    print("اختر رقم المنتج:")
    for n in range(len(products)):
     print(f"{n+1} - {products[n][0]}")

    productNumber = int(input("اكتب الرقم: "))
    if 1 <= productNumber <= 5:
        price = products[productNumber-1][1]
        total_price = price + (price * 0.15)
        print(f"سعر المنتج شامل الضريبة: {total_price} ريال")
        break  # نخرج من الحلقة بعد إدخال صحيح
    else:
        print("رقم المنتج غير صحيح، حاول مرةش أخرى.\n")
