# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

if [ $# -ne 1 ]; then
    echo 'Need n, exp:"ans14.sh 3"'
    exit 1
fi

tail -n $1 './popular-names.txt'