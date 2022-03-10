https://docs.docker.com/language/python/build-images/#tag-images

docker run -d -p 8000:5000 python-docker

docker build --tag dbothwell/python-docker:v1.0.1 .

https://medium.com/codex/push-docker-image-to-docker-hub-acc978c76ad

docker login

docker tag python-docker:latest python-docker:v1.0.1

docker push dbothwell/python-docker:v1.0.1

v1.0.2 -- removed the last line from Dockerfile
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
