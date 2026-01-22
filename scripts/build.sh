#!/bin/bash

# This script builds the Docker image for the application.
docker build -t test_wrappers_image .
# You can run the container using:
docker run -p 8000:8000 test_wrappers_image