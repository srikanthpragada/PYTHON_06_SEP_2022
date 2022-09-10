# Net price

price = int(input("Enter price :"))
discount = price * 15 // 100
after_discount_price = price - discount
tax = after_discount_price * 8 // 100
net_price = after_discount_price + tax
print('Net Price = ', net_price)
