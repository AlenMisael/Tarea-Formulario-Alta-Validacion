FROM python:3.8

ENV DOCKER_CONTAINER = True

WORKDIR /app


COPY . /app

RUN pip install --no-cache-dir -r requirements.txt 
RUN chmod +x /app/init-db.sh

EXPOSE 5000

CMD ["/app/init-db.sh"]

CMD ["python", "src/app.py"]

