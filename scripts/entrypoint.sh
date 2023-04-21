#!/bin/bash

create_app="uvicorn app:create_app --host=0.0.0.0 --factory --port 8080 --workers 5"


if [[ ${CA_CERT} ]]
 then
  create_app="${create_app}"
fi

migrate="alembic upgrade head"

eval "$migrate" && eval "$create_app"

echo "alembic migrated and service started"