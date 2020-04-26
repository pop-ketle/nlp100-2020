# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import re
import pandas as pd

df = pd.read_json('./jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]

# 基礎情報テンプレートの抽出条件のコンパイル
p = re.compile(r'''
    ^\{\{基礎情報.*?$   # '{{基礎情報'で始まる行
    (.*?)       # キャプチャ対象、任意の0文字以上、非貪欲
    ^\}\}$      # '}}'の行
    ''', re.MULTILINE+re.VERBOSE+re.DOTALL)
contents = p.findall(ukText)

# 抽出結果からのフィールド名と値の抽出条件コンパイル
p = re.compile(r'''
    ^\|         # '|'で始まる行
    (.+?)       # キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
    \s*         # 空白文字0文字以上
    =
    \s*         # 空白文字0文字以上
    (.+?)       # キャプチャ対象（値）、任意の1文字以上、非貪欲
    (?:         # キャプチャ対象外のグループ開始
        (?=\n\|)    # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)   # または、改行+終端の手前（肯定の先読み）
    )           # グループ終了
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
fields = p.findall(contents[0])

ans = {field[0]: field[1] for field in fields}
print(ans)

# template = '基礎情報'
# ls, flag = [], False
# p1 = re.compile('\{\{' + template)
# p2 = re.compile('\}\}')
# p3 = re.compile('\|')
# p4 = re.compile('<ref(\s|>).+?(</ref>|$)')
# for text in ukText.split('\n'):
#     if flag:
#         tmp = [p2.match(text), p3.match(text)]
#         if tmp[0]:
#             break
#         if tmp[1]:
#             ls.append(p4.sub('', text.strip()))

#     if p1.match(text):
#         flag = True
# print(ls)
# p = re.compile('\|(.+?)\s=\s(.+)')
# # ans = {m.group(1): m.group(2) for m in [p.match(c) for c in ls]}
# ans = [m.group() for m in [p.match(c) for c in ls]]
# # ans = {m.group(1): m.group(2) for m in [re.match(r'\|(.+?)\s=\s(.+)', c)for c in ls]}
# print(ans)
# for a in ans:
#     print(a)