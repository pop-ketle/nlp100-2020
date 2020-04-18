# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
# *Typoglycemiaとは、単語を構成する文字を並べ替えても、最初と最後の文字が合っていれば読めてしまう現象のことである。

import random

def typoglycemia(s):
    s = s.split(' ')
    ans = []
    for t in s:
        if len(t)<=4:
            ans.append(t)
        else:
            f,e = t[0],t[-1]
            tmp = random.sample(list(t[1:-1]),len(t[1:-1]))
            ans.append(t[0]+''.join(tmp)+t[-1])
    return ' '.join(ans)

s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

print(typoglycemia(s))
