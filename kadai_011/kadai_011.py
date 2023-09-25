list = ["水","金","地","火","木","土","天","海","冥"]

#for文でplanetに代入して、出力
for planet in list:
  print(planet)

#一度、for文を作り、while文で判定して出力
for i in range(9):
  while(list[i] != ""):
    print(list[i])
    break
