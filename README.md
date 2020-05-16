# Markov Algorithm Online Testing Framework

https://mao.snuke.org/ の解をテストするのに便利なツールです。

## 要件
* Python 3.6 以上

## 機能
* テストケース定義 & 評価
* 貪欲最適化で不要なルールを除去 (optimize/bruteforce.py)

## 簡単な使い方
1. solutions/template.py をコピーします。これがそのまま Problem 6 用の例になっています。
2. judge を実装します。sが入力で、これに対する出力を返せばよいです。任意の Python 3 コードを使えます。
3. test_cases を実装します。これはテストケースを返すジェネレータです。よくわからなければ関数定義っぽくイテレータが定義できて、次の要素を返すのに yield 文を使うとだけ覚えておけばよいです。
4. （必要であれば）step_limit をオーバーライドします。Problem 42 のようにステップ数に独自の制限があるときに必要になります。
5. 準備完了です。solution をいろいろ書き換えながらスクリプトを実行してみましょう。

コマンドラインからだと、リポジトリのルートから次のコマンドで実行できます（template は適宜書き換え）。
```shell script
python -m solutions.template
```
テストに成功すれば、solutions/output.txt に最適化された解が出力されます。

## 細かい機能
* mao/interp.py はコマンドラインツールとして機能します
* solutions/utils.py の binary と pad_binary はテストケース生成に便利です。