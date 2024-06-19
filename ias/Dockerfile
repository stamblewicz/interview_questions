# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Define the argument
ARG WMATA_API_KEY

# Set the environment variable using the argument's value
ENV WMATA_API_KEY=${WMATA_API_KEY}                                                 

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run wmata_trains.py when the container launches
CMD ["python", "./wmata_trains.py"]

