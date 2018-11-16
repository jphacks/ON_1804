# MuscleBattle

## 構成

* MuscleBattle_django：本体
* MuscleBattle_node：webRTC配信用サーバー

## 起動方法


### node

```
brew install ndenv

cd MuscleBattle_node
ndenv install v11.0.0
ndenv rehash
ndenv local v11.0.0
npm run test-page
```

### django
https://www.anaconda.com/download/ からpython3系のやつをinstall

httpsで通信するので証明書(localで試すならオレオレでもok)を `/usr/local/etc/openssl/certs/` 辺りに置いておく

```
cd MuscleBattle_django
conda create -n py36django python=3.6 django
source activate py36django
python manage.py migrate
python manage.py loaddata training/fixtures/fixture.json
python manage.py runsslserver 0.0.0.0:8000 --certificate /usr/local/etc/openssl/certs/cert.pem --key /usr/local/etc/openssl/certs/cert.pem
```
