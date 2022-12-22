#!/bin/bash
docker-compose -f create-certs.yml run --rm create_certs

docker-compose up -d

docker run --rm -v es_certs:/certs --network=es_default docker.elastic.co/elasticsearch/elasticsearch:8.1.3 curl --cacert /certs/ca/ca.crt -u elastic:PleaseChangeMe https://es01:9200

docker exec es01 /bin/bash -c "bin/elasticsearch-setup-passwords \
auto --batch \
--url https://localhost:9200"