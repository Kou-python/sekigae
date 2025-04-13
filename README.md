## 実行方法

以下のコマンドで Docker のイメージをビルドし、コンテナ内でコマンドを実行する。

```shell
$ docker build --no-cache -t sekigae .
$ docker run --rm sekigae seat_change
```