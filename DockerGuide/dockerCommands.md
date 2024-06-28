

buil the images with the tag
```bash
docker build -t savindu9x/devopsAI:latest . 
```

```bash
docker images -a
```
connect from localhost:8501 to container port:8080 -> expose this port in ec2 security group
-d for detached mode
```bash
docker run -d -p 8080:8501 savindu9x/devopsAI 
```
```bash
docker tag savindu9x/devopsAI savindu9x/devopsAI:latest
```
```bash
docker login
```
```bash
docker image push savindu9x/devopsAI:latest
```
see running containers
```bash
docker ps
```
```bash
docker stop container_id
```
```bash
docker rm $(docker ps -a -q)
```
```bash
docker pull savindu9x/devopsAI:latest
```
```bash
docker save -o filename.tar docker_image:latest
```


