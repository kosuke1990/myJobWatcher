# Pythonの公式イメージをベースとして使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコンテナにコピー
COPY requirements.txt /app/

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコンテナにコピー
COPY src /app

# カスタムエクスポーターを実行するコマンドを指定
CMD ["python", "app.py"]
