# Base Image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Update apt
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the app
COPY .streamlit .streamlit
COPY config config
COPY assets assets
COPY src src
COPY requirements.txt .

# Install requirements
RUN pip3 install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Perform Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the app
ENTRYPOINT [ "streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]