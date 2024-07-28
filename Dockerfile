# Use python:3.10-alpine as the base image
FROM python:3.8-slim-buster

# Create the working directory for our Python Flask application Docker image
WORKDIR /code

# Copy the dependencies and libraries in the requirements.txt to the working directory
COPY requirements.txt /code

# Install the dependencies in the requirements.txt to the Docker image
RUN pip install -r requirements.txt --no-cache-dir

# Expose the port the Flask app runs on
EXPOSE 8001

# Copy the files and source code required to run the application
COPY . /code

# Set the executable permission for the entrypoint script
RUN chmod +x /code/docker-entrypoint.sh

# Use the full path for the entrypoint script
ENTRYPOINT ["/code/docker-entrypoint.sh"]

# RUN python src/models/code/train.py
# CMD ["python","src/app.py"]