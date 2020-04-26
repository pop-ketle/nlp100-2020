# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

import re
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]

# 基礎情報テンプレートの抽出条件のコンパイル
p = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE+re.VERBOSE+re.DOTALL)
contents = p.findall(ukText)

p = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)| (?=\n$))', re.MULTILINE+re.VERBOSE+re.DOTALL)
fields = p.findall(contents[0])

ans = {field[0]: field[1] for field in fields}
p = re.compile("'+")
ans = {k: p.sub('', v) for k,v in ans.items()}
print(ans)