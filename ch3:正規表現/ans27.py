# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

import re
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]

# 基礎情報テンプレートの抽出条件のコンパイル
p = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE+re.VERBOSE+re.DOTALL)
contents = p.findall(ukText)

# 抽出結果からのフィールド名と値の抽出条件コンパイル
p = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)| (?=\n$))', re.MULTILINE+re.VERBOSE+re.DOTALL)
fields = p.findall(contents[0])

ans = {field[0]: field[1] for field in fields}
p = re.compile("'+")
ans = {k: p.sub('', v) for k,v in ans.items()}

# 内部リンクの除去
p = re.compile(r'''
    (\'{2,5})   # 2〜5個の'（マークアップの開始）
    (.*?)       # 任意の1文字以上（対象の文字列）
    (\1)        # 1番目のキャプチャと同じ（マークアップの終了）
''', re.MULTILINE + re.VERBOSE)
ans = {k: p.sub(r'\2', v) for k,v in ans.items()}

# 内部リンクの除去
p = re.compile(r'''
    \[\[       # '[[' マークアップの開始
    (?:        # キャプチャ対象外のグループ開始
        [^|]*? # '|'以外の文字が0文字以上、非貪欲
        \|     # '|'
    )??        # グループ終了、このグループが0か1以上出現、非貪欲
    ([^|]*?)   # キャプチャ対象、'|'以外が0文字以上、非貪欲(表示対象の文字列)
    \]\]       # ']]' (マークアップの終了)
''', re.MULTILINE + re.VERBOSE)
ans = {k: p.sub(r'\1', v) for k,v in ans.items()}
print(ans)