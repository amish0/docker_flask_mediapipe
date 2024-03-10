FROM python:3.9 AS builder
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
# Install the required system dependencies
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
COPY requirements.txt requirements.txt
COPY ./static ./static
COPY ./templates ./templates
COPY ./model model
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Stage 2: Runtime stage
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app
ENV PATH="/opt/venv/bin:$PATH"
# Copy installed Python packages from the builder stage
# COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

# Copy the application code from the builder stage
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app .

# Expose the port on which the Flask app will run
EXPOSE 8000

# Set the entrypoint command to run the Flask app
CMD ["python", "app.py"]
