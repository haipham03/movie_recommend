build image:
```
    DOCKER_BUILDKIT=1 docker build -t recommend_image .
```
run:
```
    doker compose up
```
api:
```
    on port 500:
    /recommend/<userID>/[numberOfmoviesToRecommend]
```