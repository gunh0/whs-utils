# Makefile

kill-local:
	@echo "Killing local Flask server... (port 8000)"
	@lsof -ti:8000 | xargs kill -9

# 설정
IMAGE_NAME=myflaskapp
CONTAINER_NAME=myflaskcontainer

# Docker 이미지 빌드
build:
	docker build -t $(IMAGE_NAME) -f ./Dockerfile .

# Docker 컨테이너 실행
run:
	docker run --name $(CONTAINER_NAME) -p 8001:8000 -d $(IMAGE_NAME)

# 추가적인 clean 명령을 통해 컨테이너 및 이미지 제거 가능
clean:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)
	docker rmi $(IMAGE_NAME)
