# Net Amount

price = int(input("Enter price :"))
qty = int(input("Enter qty :"))
amount = price * qty

if qty > 2:
    discount = amount * 20 // 100
else:
    discount = amount * 10 // 100

after_discount = amount - discount

if after_discount > 10000:
    after_discount = after_discount * 95 / 100  # 5% additional discount

print(after_discount)

after_discount_price = price - discount
tax = after_discount_price * 8 // 100
net_price = after_discount_price + tax
print('Net Price = ', net_price)
