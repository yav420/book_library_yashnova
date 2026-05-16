FROM ubuntu:latest
LABEL authors="yashn"

ENTRYPOINT ["top", "-b"]

FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv
RUN uv sync

EXPOSE 5000

CMD ["uv", "run", "flask", "--app", "app", "run", "--host=0.0.0.0", "--debug"]