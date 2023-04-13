# 必要なモジュールのインポート
from flask import Flask

# flaskのインスタンス作成
app = Flask(__name__)

# ルートディレクトリにアクセスがあった場合の処理
@app.route('/')
def hello():
    return 'Hello World!'

# エントリーポイント
if __name__ == '__main__':
    app.run()



