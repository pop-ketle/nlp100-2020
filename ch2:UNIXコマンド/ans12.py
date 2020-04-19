# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

import pandas as pd

df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
df[0].to_csv('./col1.txt')
df[1].to_csv('./col2.txt')
