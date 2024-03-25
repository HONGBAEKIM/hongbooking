#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 <password>"
    echo "Please provide the password obtained from https://www.hongpage.com/hongbooking as a parameter."
}

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    usage
    exit 1
fi

# Assign the provided password to a variable
password="$1"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed. Please install Docker Desktop from https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Check if Docker Desktop is running
if ! docker info &> /dev/null; then
    echo "Error: Docker Desktop is not running. Please start Docker Desktop and try again."
    exit 1
fi

# Ensure password is provided
if [ -z "$password" ]; then
    echo "Error: No password provided. Exiting."
    exit 1
fi

# Create a temporary directory
temp_dir=$(mktemp -d)
cd "$temp_dir" || exit

# Copy the executable and _internal file to the temporary directory
cp /hongbooking19_student .
cp /_internal .

# Create Dockerfile
cat <<EOF > Dockerfile
FROM ubuntu:latest
COPY hongbooking19_student /usr/local/bin/
COPY _internal /usr/local/bin/
CMD ["hongbooking19_student", "$password"]
EOF

# Build Docker image
docker build -t my_executable_image .

# Run Docker container with the provided password
docker run --rm my_executable_image "$password"

# Clean up
rm -rf "$temp_dir"

