price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(format(base,'.2f'), format(vat_amount,'.2f'), format(total,'.2f'), sep='\n')