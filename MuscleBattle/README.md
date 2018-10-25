# MuscleBattle

## 構成

* MuscleBattle_django：本体
* MuscleBattle_node：webRTC配信用サーバー

## 環境構築


### node

```
brew install ndenv

cd MuscleBattle_node
ndenv install v11.0.0
ndenv rehash
ndenv local v11.0.0
```

### django
https://www.anaconda.com/download/ からpython3系のやつをinstall

```
cd MuscleBattle_django
conda create -n py36django python=3.6 django
source activate py36django
python manage.py runserver 0:8000
```
