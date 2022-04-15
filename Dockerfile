FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip -r required.txt

WORKDIR /workspace

COPY . .

CMD ["python3", "main.py"]