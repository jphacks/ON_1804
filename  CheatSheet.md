# Dev Cheat Sheet

## 開発の流れ
### 1. ブランチを切る
```
git checkout master
git checkout -b <branch_name>
~作業する~
git add -A
git commit -m "変更内容を書く"
git push origin <branch_name>
```

### 2. pull requestを作る
githubのレポジトリのページからPull Requestを作る．

### 3. 再度やり直す場合
```
(作業中のブランチだとして)
git pull
~作業する~
git add -A
git commit -m "変更内容を書く"
git push origin <branch_name>
```

### 4. 終わったら
```
git checkout master
git pull
```
`1.` に戻る

### 5. その他
```
git status (状態を見る)
git log --graph (logを見る)
git log -p (変更内容logも見る)
```

## Django
※環境構築がまだの人は `MuscleBattle/README.md` 辺りを見てください

ターミナル立ち上げて最初にやること
```
source ~/.bash_profile (zshならsource ~/.zshrcとか)
source activate py36django
```

サーバー起動
```
python manage.py runserver 0:8000
```

アプリ作成
```
python manage.py startapp <app name>
```

マイグレーション
```
python manage.py makemigrations <app name>
python manage.py migrate
```
