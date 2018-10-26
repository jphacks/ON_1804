# Dev Cheat Sheet

## 1. ブランチを切る
```
git checkout master
git checkout -b <branch_name>
~作業する~
git add -A
git commit -m "変更内容を書く"
git push origin <branch_name>
```

## 2. pull requestを作る
githubのレポジトリのページからPull Requestを作る．

## 3. 再度やり直す場合
```
(作業中のブランチだとして)
git pull
~作業する~
git add -A
git commit -m "変更内容を書く"
git push origin <branch_name>
```

## 4. 終わったら
```
git checkout master
git pull
```
`1.` に戻る

