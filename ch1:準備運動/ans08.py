# 08. 暗号文

# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

#     英小文字ならば(219 - 文字コード)の文字に置換
#     その他の文字はそのまま出力

# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(S):
    ans = [chr(219-ord(s)) if not s.isupper() else s for s in S]
    return ''.join(ans)

text   = 'This Is A Sample Text.'
encode = cipher(text)
decode = cipher(encode)
print(encode)
print(decode)
