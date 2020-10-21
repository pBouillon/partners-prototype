d-run:
	docker-compose up -d --build

d-stop:
	docker-compose down

install:
	pip install -r requirements.txt

run:
	uvicorn main:app --reload
