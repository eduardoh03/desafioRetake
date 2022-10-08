#Definindo o sistema operacional do container
FROM python:3.9-alpine

# Definir uma porta que será exposta (Porta que o django irá rodar)
EXPOSE 8001

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalando bibliotecas de suporte na imagem
RUN apk update \
    && apk add --virtual build-deps gcc make automake g++ subversion python3-dev libpq-dev musl-dev \
    && python -m pip install --upgrade pip \
    && python -m pip install Cmake \
    && ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/lib \
    && ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib \
    && ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib

# instalando o requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


#Definido um ambiente para trabalho
WORKDIR /app
COPY . /app


#Executando os comandos do manage.py
RUN python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "desafioRetake.wsgi"]