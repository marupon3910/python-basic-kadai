class Human:
  #コンストラクタを定義する
  def __init__(self,name,age):
    self.name = name
    self.age = age

  #メソッドを定義する
  def set_name(self,name):
    self.name = name

  def printinfo(self):
    return str(self.name) + "は" + str(self.age) + "歳です。"

#インスタンス化する
human = Human("太郎",36)
print(human.printinfo())
