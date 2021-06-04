# CLOTHES SHOP 
#### Make with Django

### Applications
#### 1. Shop
#### 2. Cart
#### 3. Orders

### Docker 
```bash
# build docker image from ./
sudo docker build -t shop .
# run docker image in background
sudo docker run -it -p 8000:8000 -d shop
# goto docker output
sudo docker logs {container id}
```

### RabbitMQ
```bash
sudo docker pull rabbitmq:3.6.14-management
sudo docker volume create rabbitmq_data
sudo docker run -d --hostname rabbitmq --log-driver=journald --name rabbitmq -p 5672:5672 -p 15672:15672 -p 15674:15674 -p 25672:25672 -p 61613:61613 -v rabbitmq_data:/var/lib/rabbitmq rabbitmq:3.6.14-management
# web interface on http://container-ip:15672
# with user guest\guest
```