#購入金額をtotal、商品の金額をprice、消費税をtaxと定義して作成
def total(price,tax):
  total = price * (1 +(tax / 100))
  #変数$totalの値を出力する
  print(f"{total}円")

#関数を呼び出し、引数として購入金額と消費税を渡す
#total(1000,10)
