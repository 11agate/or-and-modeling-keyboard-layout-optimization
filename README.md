# or-and-modeling-keyboard-layout-optimization
モデル化とORのコード共有用リポジトリ

# 動かし方
ampl_mswin64をダウンロードして解凍し、リポジトリにコピーする。
学習してほしいテキストを` input `にコピーし、
Pythonをインストールして、以下のコマンドで実行できる。
` py script.py `

もしくは、手動で実行(ただし、Pythonを先に実行しないと.datファイルが生成されない)
` ampl_mswin64\ampl.exe script.run `

# キーボード画像の出力
> py script.py 

を実行

` logs\log `の`y [*,*]`をコピーして` output `にペースト

> py print.py 
