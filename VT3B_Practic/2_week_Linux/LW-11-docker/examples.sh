#Введение в Docker

# Установка docker
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce

# Проверим статус
sudo systemctl status docker

# Список доступных команд
docker

# Информацию о Docker
sudo docker info

# Запустим тестовый контейнер
sudo docker run hello-world

# Поищем nginx
sudo docker search nginx

# Скачаем образ
sudo docker pull nginx

# Запустим контейнер
sudo docker run -d --name nginx -p 80:80 -v /var/www/html:/usr/share/nginx/html nginx

# Список активных контейнеров
sudo docker ps

# Чтобы увидеть и активные, и неактивные контейнеры
sudo docker ps -a

# Зайдём в оболочку контейнера
sudo docker exec -ti nginx bash

# Остановка и запуск контейнеров
sudo docker stop sharp_volhard
sudo docker start d9b100f2f636

# Перезагрузка
sudo docker restart nginx

# Отправка сигнала
sudo docker kill -s HUP nginx

# Логи контейнера
sudo docker logs nginx

# Информация о контейнере
sudo docker inspect nginx

# Публичные порты
sudo docker port nginx

# Выполняющиеся процессы
sudo docker top nginx

# Использование ресурсов
sudo docker stats nginx

# Список образов
sudo docker images

# Просмотр истории образа
sudo docker history nginx

# Удаление контейнера
sudo docker rm nginx

# Удаление образа
sudo docker rmi nginx

# mysql install
docker pull mysql/mysql-server:8.0

docker run --name=mysql1 -p 3306:3306 -d mysql/mysql-server:8.0

docker logs mysql1 2>&1 | grep GENERATED

docker exec -it mysql1 bash

mysql -uroot -p

ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

docker run --name=mysql80 \
   --mount type=bind,src=/path-on-host-machine/my.cnf,dst=/etc/my.cnf \
   --mount type=bind,src=/path-on-host-machine/datadir,dst=/var/lib/mysql \        
   -d mysql/mysql-server:8.0

# Установка контейнеров для работы WordPress с помощью docker-compose

https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-docker-compose-ru

