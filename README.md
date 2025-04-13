## Docker を利用した実行

ターミナルで以下のコマンドで Dockerイメージをビルドし、コンテナを実行する。

```shell
$ docker build -t sekigae .
$ docker run -p 8501:8501 sekigae
```

Webブラウザで以下にアクセスする。

```text
http://localhost:8501
```
