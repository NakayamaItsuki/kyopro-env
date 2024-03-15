# 個人的に重要だと思ったところ（c++編）

# section 1

- (1 << x)は2のx乗を表す

- ビット演算に慣れる必要あり．ビット全探索で2^nのパターンが実現できる

# section 2

- 累積和，前もって計算しておく

- 二次元累積和，長方形領域の和を計算する

- c++において，入力で受け取った引数で配列のサイズを決めることができない．

- 累積max

# section 3

- 二分探索，[lower_boundとupper_boundの使い方](https://qiita.com/ganyariya/items/33f1326154b85db465c3)，c++のlower_boundとpythonのbisect_leftは挿入するインデックスを返す．

- 答えで二分探索

- 二分探索

    2パターンありそう

    パターン1，普通はこちら
    - if X < A[mid]: right = mid - 1
    - else if X == A[mid]: return mid
    - else A[mid] < X: left = mid + 1
    - 見つからなかったらreturn -1

    パターン2
    - if X <= A[mid]: left = mid + 1
    - else : right = mid

- しゃくとり法...途中まで足したやつを再利用する

- 半分全列挙...

- 集合の演算はpythonの方が圧倒的に書きやすい，pythonのsetに慣れているというのも大きいが．

- chatGPTに「このコードを高速化して」というと高速にしてくれる...


