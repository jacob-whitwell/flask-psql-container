FROM python:3.7
ENV FLASK_ENV development
ENV POSTGRES_DB postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5432 
CMD [ "python3", "init_db.py" ]
#CMD ["flask", "--app", "app", "--debug", "run", "--host=0.0.0.0"]