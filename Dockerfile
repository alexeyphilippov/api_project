FROM python:3.8
USER root

WORKDIR  /app
COPY . .

COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

RUN sed -i 's/\r$//' scripts/entrypoint.sh

CMD ["/bin/bash", "scripts/entrypoint.sh"]