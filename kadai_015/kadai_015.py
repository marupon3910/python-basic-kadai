class Human:
  #コンストラクタを定義する
  def __init__(self,name,age):
    self.name = name
    self.age = age
  
  #メソッドを定義する
  def set_name(self,name):
    self.name = name

  def printinfo(self):
    print(self.name)

#インスタンス化する
human = Human("太郎",36)

#属性にアクセスし、値を出力する
print(human.name)
print(human.age)
