FROM python:3.13

RUN pip install --no-cache-dir streamlit pandas

WORKDIR /app

COPY app.py .

EXPOSE 8501
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV STREAMLIT_SERVER_PORT=8501

# アプリを起動
CMD ["streamlit", "run", "app.py"]