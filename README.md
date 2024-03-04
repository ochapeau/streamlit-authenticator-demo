# Streamlit-Authenticator Demo App

This repository contain a demo app for organizing a Streamlit App with Streamlit-Authenticator

## Content of the repository

Ce repository contient:
- Code of the web application with its [Dockerfile](./Dockerfile) for deployment:
    - Directory [.streamlit/](./.streamlit/): Streamlit configuration
    - Directory [src/](./src/): Application sources
    - Directory [config/](./config/): Application and streamlit-authenticator configuration files
    - Directory [assets/](./assets/): Application assets (Can contain stylesheets, images...)
    - File [requirements.txt](./requirements.txt): Application requirements

## Description

## Used Technologies

## Application usage

## Application configuration

## Deployment

### Building Docker image
```sh
docker build -t [image_name] .
```
Verifying that the image was built:
```sh
docker images
```

### Execute the Docker Container:
```sh
docker run -p 8501:8501 [image_name]
```