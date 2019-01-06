FROM python:3.6-alpine
RUN pip install gunicorn
COPY server.py /server.py
ENTRYPOINT ["gunicorn"  , "-b", "0.0.0.0:8000", "server:app"]
