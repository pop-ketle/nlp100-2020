# 06. 集合
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

inputx,inputy = 'paraparaparadise','paragraph'
x,y = set(inputx),set(inputy)

union        = x | y # 和集合
intersection = x & y # 積集合
difference   = x - y # 差集合
print(*[union,intersection,difference],sep='\n')
print('se' in inputx)
print('se' in inputy)
