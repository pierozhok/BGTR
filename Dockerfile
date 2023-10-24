FROM python:3.10-slim

COPY . .

RUN pip install --no-cache-dir requirements.txt

ENTRYPOINT [ "uvicorn", "main:app" ]
