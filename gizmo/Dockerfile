ARG BUILD_FROM
FROM $BUILD_FROM

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn pydantic pymysql

COPY app /app
COPY run.sh /run.sh

RUN chmod a+x /run.sh

EXPOSE 8000

CMD ["/run.sh"]
