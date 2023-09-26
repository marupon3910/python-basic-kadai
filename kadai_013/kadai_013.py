#購入金額をtotal、商品の金額をprice、消費税をtaxと定義して作成
def total(price,tax):
  total = price * (1 +(tax / 100))
  return f"{total}円"
print(total(1000,10))
