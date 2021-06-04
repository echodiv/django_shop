# CLOTHES SHOP 
## Make with Django

### docker 
```bash
# build docker image from ./
sudo docker build -t shop .
# run docker image in background
 sudo docker run -it -p 8000:8000 -d shop
# goto docker output
sudo docker logs {container id}
```