# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev

# Copy the requirements file to the container
COPY requirements.txt requirements.txt
COPY ./static ./static
COPY ./templates ./templates
COPY ./model model

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port on which the Flask app will run
# EXPOSE 8000

# Set the entrypoint command to run the Flask app
CMD ["python", "app1.py"]
