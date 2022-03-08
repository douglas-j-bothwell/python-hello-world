https://docs.docker.com/language/python/build-images/#tag-images

docker build --tag python-docker .

docker tag python-docker:latest python-docker:v1.0.0

docker run -d -p 8000:5000 python-docker
