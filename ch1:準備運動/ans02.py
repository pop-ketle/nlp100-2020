# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

s1,s2 = 'パトカー','タクシー'
ans = ''
for t1,t2 in zip(s1,s2):
    ans+=t1
    ans+=t2
print(ans)