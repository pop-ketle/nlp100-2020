# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
# *n-gramとは: 任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法．

def make_n_gram(s,n):
    n_gram = []
    for i,t in enumerate(s):
        if i+n>len(s): break # 最後n文字以上取れなくなったらそこで終わりらしいので
        n_gram.append(s[i:i+n])
    return n_gram


s = 'I am an NLPer'
print(make_n_gram(s,2))
print(make_n_gram(s.split(' '), 2))

# リスト内包表記での書き方
# def n_gram(target, n):
#     return [target[idx:idx + n] for idx in range(len(target) - n + 1)]
