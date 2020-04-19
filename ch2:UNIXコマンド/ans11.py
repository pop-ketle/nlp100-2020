# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import pandas as pd

df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
df.to_csv('./ans11.txt', sep=' ', index=False, header=None)