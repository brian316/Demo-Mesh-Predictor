#!/bin/bash

# This script builds the Docker image for the application.
docker build -t demo_mesh_predictor .
# You can run the container using:
docker run --rm -it -p 8080:8080 -e REDIS_HOST="host.docker.internal" -e REDIS_PORT=6379 -e REDIS_PASSWORD="" demo_mesh_predictor