# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pika

# Run publisher or consumer
CMD ["python", "publisher.py"]
