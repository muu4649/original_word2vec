import MeCab
import numpy as np
mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = '柔軟なシート状をした表示部を備え、当該表示部から、難聴者が補聴器をつけることなく健聴者と共に聞き取ることができる音声を発生させる表示装置を提供する。表示装置１０は、入力された第一の電気信号に応じて画像を表示することが可能な柔軟なシート状をした表示部１を備える。また、表示装置は、入力された第二の電気信号に応じて駆動するドライバユニット２を備える。表示部は、湾曲する曲面領域を有し、ドライバユニットは、この表示部において湾曲する方向の一端側１ａ端面に当接して取り付けられる。そして、駆動するドライバユニットの振動を端面から表示部へ伝達することで、表示部から音声を発生させることが出来る。'
mecab.parse('')#文字列がGCされるのを防ぐ
node = mecab.parseToNode(text)
while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[1]
    #print('{0} , {1}'.format(word, pos))
    print(word,np.array(pos))

    #次の単語に進める
    node = node.next
