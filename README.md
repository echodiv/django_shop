# CLOTHES SHOP 
#### Make with Django

### Local environment variables:
```buildoutcfg
DJANGO_ENV - current django enviorement [DEV | TEST | OTHER]
if django enviorement variable is not exist or not [DEV | TEST]
django run as production server
```
### Applications
#### 1. Shop
#### 2. Cart
#### 3. Orders
#### 4. Coupons

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