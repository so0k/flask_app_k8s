# Sample flask app

Based on [docker/labs/flask-app](https://github.com/docker/labs/tree/bd6bcaa1e25e75dc3611ea063b3d38c65e205141/beginner/flask-app)

Added some type of config file to play with Kubernetes ConfigMaps

build the image
```
export DOCKER_REPO=<docker-hub-user>
docker build -t $DOCKER_REPO/flask_app:1.0 .
```

run the container
```
docker run -d --name money_machine -p 5000:5000 $DOCKER_REPO/flask_app:1.0
```

verify container logs
```
docker logs money_machine
```

push the image to the hub
```
docker push $DOCKER_REPO/flask_app:1.0
```

