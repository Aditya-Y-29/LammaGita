#!/bin/bash

# Define variables
IMAGE_NAME="llama-gita"
CONTAINER_NAME="llama-gita-container"
PORT_MAPPING="8501:8501"

# Build the Docker image
docker build -t "$IMAGE_NAME" .

# Run the Docker container
docker run --rm -it -d -p "$PORT_MAPPING" --name "$CONTAINER_NAME" "$IMAGE_NAME"

# Display container status
docker ps -a --filter "name=$CONTAINER_NAME"

# Provide instructions to access the app
echo "The Llama Gita chatbot is now running."
echo "You can access it at http://192.168.225.215:8501"
