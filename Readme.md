`python3.9 -m venv venv`  
`. ./venv/bin/activate`  
`pip install --upgrade setuptools pip`  
`pip install -r requirements.txt`

## Docs Selenoid

https://aerokube.com/selenoid/

## !!!!! IP к которому цепляться, если нужно указать не имя docker контейнера !!!!

`ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d: | head -n1`

## Befor start

`docker pull selenoid/vnc:chrome_80.0`  
`docker pull selenoid/vnc:chrome_102.0`

`docker-compose up`

http://localhost:4444/  
http://localhost:8080/  
http://localhost:4444/logs/
