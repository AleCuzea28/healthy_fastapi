FROM python:3.11.2-slim-bullseye

SHELL ["/bin/bash", "-c"]

RUN mkdir -p /home/syneto-lab-dark-side/
COPY pyproject.toml /home/syneto-lab-dark-side
WORKDIR /home/syneto-lab-dark-side

RUN apt-get update

RUN python3 -m venv .venv/
RUN .venv/bin/python3 -m pip install --upgrade pip
RUN .venv/bin/python3 -m pip install poetry
RUN .venv/bin/python3 -m poetry install

# ENTRYPOINT [ "tail", "-f", "/dev/null" ]
ENTRYPOINT [ ".venv/bin/python3", "-m", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "healthy.main:app", "--reload" ]

# Build command: docker build -t isyneto .
# Start container: docker run -d --name csyneto -p 8000:8000 --mount type=bind,source="$(pwd)/healthy",target=/home/syneto-lab-dark-side/healthy isyneto
# See logs of container/uvicorn web server: docker logs -f csyneto
# Enter container: docker exec -it csyneto /bin/bash ; once inside, execute `source .venv/bin/activate` and you are ready to code
