# 階乗計算の速度比較
## 概要
とあることから階乗計算の速度比較をした記録（雑）

そのうえでいくつかのサイトを参考にした
- [Pythonで階乗 math.factorial のアルゴリズム](https://qiita.com/AkariLuminous/items/1b2e964ebabde9419224)
- etc..

検証した関数
- simple_fractal
    - 1からnまでfor文で掛け算を回す関数
- used_library_fractal
    - mathライブラリの階乗計算関数
- copy_and_paste_fractal
    - 参考サイトのコード（いいのかな、）
- nezumi_fractal
    - 参考サイトをもとに簡易実装（テキトウに作り過ぎたためか結果が合わない場合がまれにある。致命的）
        - 出来るだけbit shiftで計算しようというアルゴリズム
- old_nezumi_fractal
    - 私が以前作成した階乗計算関数 (うろ覚え)
        - 素因数分解をし、高速かを図るアルゴリズム。
        - マルチプロセスも使用しているためオーバーヘッドが大きい

## 環境
- intel core i5 12400f
- RAM 32G DDR4
- python 3.11.2

## 使い方
main.ipynbファイルをjupyter notebook上で動かせる

## 計測結果
以下のようになった

![output](https://github.com/Tester-ringo/fractal/blob/master/output.png?raw=true)

#### 見方
横軸は2を底とした対数表記
縦軸は10を底とした対数表記

#### 順位
およそ5秒前後の計算負荷での順位
1. 参考サイトのコード & mathライブラリの関数 (copy_and_paste_fractal, used_library_fractal)
2. 以前作成した関数 (old_nezumi_fractal)
3. 参考サイトを参考に今回実装した関数 (nezumi_fractal)
4. forによる簡易実装 (simple_fractal)

## 雑考察
n!の値の大きさの増える速度に比べ、計算時間の増え方は基本的に同じである。
しかし、以前作成した関数(old_nezumi_fractal)は他の関数に比べて計算時間の増え方が緩やかである。
そのため、今回はn=500,000程度だが、さらに大きい1,000,000を越えてくると順位が変動するかもしれない。
考えられる理由としては、マルチプロセスによるオーバーヘッドがボトルネックとなっていると思われる。
（早い理由は考えていない）

