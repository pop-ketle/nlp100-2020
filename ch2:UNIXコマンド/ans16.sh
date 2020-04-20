# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．
# FIXME: 本当なら小数点で切り上げすべきだけど面倒だったので飛ばした

if [ $# -ne 1 ]; then
    echo 'Need n, exp:"ans16.sh 3"'
    exit 1
fi

n=`wc -l './popular-names.txt' | awk '{print $1}'`
ln=`expr $n / $1`
split -l $ln './popular-names.txt' './ans16_'