# ソースコードの変更

``` cmd
git clone https://github.com/sh0g0fujIta/bycycle_MAINT.git
```

1. ソースコードの修正を行う

2. githubに変更を取り込みたい第るをステージングエリアに追加する

- すべての変更を取り込む場合
``` cmd
$ git add .
```

- 対象のファイル変更を取り込む場合
``` cmd
$ git add README.md

$ git add README.md docs/api.html
```

3. ステージングエリアに追加したものをコミットする。
``` cmd
$ git commit -m "<コメント(変更した内容などを記載)>"
```

4. 変更をgithubのリポジトリに取り込む
``` cmd
$ git push origin main 
```
