# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /python-docker

# Copy the current directory contents into the container at /app
COPY . /python-docker

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
# listen to requests that come from anywhere, not just localhost
CMD ["flask", "run", "--host", "0.0.0.0"]
