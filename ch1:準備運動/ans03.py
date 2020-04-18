# 03. 円周率
# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
splited = s.split(' ')
ans = ['']*len(splited)
for i,t in enumerate(splited):
    cnt = len(t)
    if t[-1]==',' or t[-1]=='.':
        cnt-=1
    ans[i] = cnt
print(ans)