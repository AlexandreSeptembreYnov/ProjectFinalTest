FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip install -r requirements.txt

WORKDIR /workspace

COPY . .

CMD ["python3", "main.py"]