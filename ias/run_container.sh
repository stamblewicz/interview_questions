#!/bin/bash

### This script was created by Karolina as per the requested interview task for IAS

# Ensure the WMATA_API_KEY is provided
if [ -z "$WMATA_API_KEY" ]; then
  echo "Please set the WMATA_API_KEY environment variable."
  exit 1
fi

# Build the Docker image
sudo docker build --build-arg WMATA_API_KEY=$WMATA_API_KEY -t wmata_trains .

# Run the Docker container
sudo docker run --rm wmata_trains
