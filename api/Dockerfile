FROM python:3.9
WORKDIR /api
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
#CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]