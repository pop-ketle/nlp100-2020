# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

import sys
import pandas as pd

if not len(sys.argv)==2:
    print('Need n, exp:"python ans16.py 3"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
    
    div_cnt = -(-len(df)//n)
    for i in range(0,len(df),div_cnt):
        print(df.iloc[i:i+div_cnt])