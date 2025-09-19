price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {format(base,'.2f')} ₽" ,f"НДС:               {format(vat_amount,'.2f')} ₽", \
      f"Итого к оплате:    {format(total,'.2f')} ₽", sep='\n')