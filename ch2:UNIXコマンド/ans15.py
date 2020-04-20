# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

import sys
import pandas as pd

if not len(sys.argv)==2:
    print('Need n, exp:"python ans14.py 3"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
    print(df.tail(n))