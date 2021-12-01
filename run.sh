#!/bin/bash

set -e

. .env.build
docker-compose -f docker-compose-deploy.yml down --volumes
docker-compose -f docker-compose-deploy.yml build 
docker-compose -f docker-compose-deploy.yml up
