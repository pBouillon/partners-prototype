FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 808

COPY ./ /

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]