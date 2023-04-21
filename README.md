# api_project


Run swagger 
---
```
docker pull swaggerapi/swagger-ui  
docker run -p 80:8080 swaggerapi/swagger-ui
http://localhost:8080
```

Run postgres 
---
```pip install alembicpip install alembic
docker pull postgres
docker run -d \
	--name dev-postgres \
	-e POSTGRES_PASSWORD=samplePassword\
	-v ${HOME}/postgres-data/:/var/lib/postgresql/data \
        -p 5432:5432
        postgres


docker pull dpage/pgadmin4
docker run \ 
    -p 80:8001 \
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.local' \
    -e 'PGADMIN_DEFAULT_PASSWORD=samplePassword' \
    --name dev-pgadmin \ 
    -d dpage/pgadmin4
    
http://localhost:8001

docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
Fpages%2Fdiffpagesbyversion.action
```
