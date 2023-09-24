#ランダムな整数を代入するために、randomモジュールをインポート
import random

#変数varに0～15までのランダムな値を代入する
var = random.randint(0,15)

#変数varが3の倍数の場合はFizz、5の倍数の場合はBuzz、
#3と5の倍数の場合はFizzBuzz、
#それ以外の場合は変数varを出力する

if var % 15 == 0:
  print("FizzBuzz")
elif var % 3 == 0:
  print("Fizz")
elif var % 5 == 0:
  print("Buzz")
else:
  print(var)
