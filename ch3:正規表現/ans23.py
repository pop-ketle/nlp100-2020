# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

import re
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]

for section in re.findall(r'(=+)([^=]+)\1\n' ,ukText):
    print(len(section[0])-1,section[1].replace(' ', ''))