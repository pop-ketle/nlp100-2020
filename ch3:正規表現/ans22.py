# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]
ukTextList = ukText.split('\n')
categorys = list(filter(lambda x: 'Category:' in x, ukTextList))

ans = [s.split('|')[0].replace(']]', '').replace('Category:', '') for category in categorys for s in re.findall(r'Category:[^Category:]*', category)]
# # 二重ループになるとリスト内包表記わかりにくいですね
# ans = []
# for category in categorys:
#     for s in re.findall(r'Category:[^Category:]*', category):
#         ans.append(s.split('|')[0].replace(']]', '').replace('Category:', ''))

print(set(ans))