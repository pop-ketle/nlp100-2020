# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

cut -f 1 -d $'\t' './popular-names.txt' >> './col1.txt'
cut -f 2 -d $'\t' './popular-names.txt' >> './col2.txt'
