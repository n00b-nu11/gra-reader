## GraReader
GraReader は macOS 上で iPhone の画面をキャプチャすることにより、 Gravity の音声ルームに投稿されたコメントを読み上げるツールです。

https://user-images.githubusercontent.com/108191157/177111321-115aa721-355f-4909-960a-86caf89e0322.MP4

## 使い方
1. macにiPhoneを有線接続し、QuickTimePlayerで音声ルームを開いた状態のiPhoneの画面をキャプチャしてください
2. キャプチャしているウインドウを左に配置してください

<img width="1440" alt="configure.png" src="https://user-images.githubusercontent.com/108191157/175783305-f568913a-13da-4c22-94ae-b83c70b4829c.png">

3. 以下のコマンドを実行してツールを起動してください

```bash
: ライブラリのインストール
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
: 実行
python3 main.py
```

## Author
なる

質問等あれば気軽にコメントしてください :bow:
