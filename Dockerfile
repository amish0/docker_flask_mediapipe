# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
# RUN apt-get update && apt-get install -y \
#     libgl1-mesa-glx \
#     libglib2.0-0 \
#     libsm6 \
#     libxext6 \
#     libxrender-dev

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the container
COPY requirements.txt requirements.txt
COPY ./fmd/static ./static
COPY ./fmd/templates ./templates
COPY ./fmd/model model

# Install the Python dependencies
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 8000

# Set the entrypoint command to run the Flask app
CMD ["python", "app.py"]
