# ベースイメージ（Python入り）
FROM python:3.10-slim

# 必要なパッケージをインストール
RUN pip install --no-cache-dir streamlit pandas

# 作業ディレクトリを作成
WORKDIR /app

# アプリのコードをコピー
COPY app.py .

# Streamlit が外部アクセスを許すように設定
EXPOSE 8501
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV STREAMLIT_SERVER_PORT=8501

# アプリを起動
CMD ["streamlit", "run", "app.py"]