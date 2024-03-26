# Streamlit-Authenticator Demo App

This repository contain a demo multilingual Streamlit app with authentication provided by the great Streamlit-Authenticator package.

## Content

This repository contains:

- Code of the web application with its [Dockerfile](./Dockerfile) for deployment:
  - Directory [.streamlit/](./.streamlit/): Streamlit configuration
  - Directory [src/](./src/): Application sources
  - Directory [config/](./config/): App and streamlit-authenticator configuration files
  - Directory [assets/](./assets/): App assets (Can contain stylesheets, images...). It contains app strings for the different languages in the [lang/](./assets/lang/) subdirectory.
  - File [requirements.txt](./requirements.txt): App requirements

## Description

This project is a simple demo/boilerplate streamlit multilingual application with user authentication.

## Technologies

This project use the following technologies:

- Streamlit framework for the web UI [streamlit](https://github.com/streamlit/streamlit)
- The [streamlit-authenticator](https://github.com/mkhorasani/Streamlit-Authenticator) package for user authentication

## Usage

## Configuration

The application configuration is made via two yaml configuration files:

- [config/app_config.yaml](./config/app_config.yaml):
  - The main application configuration file, that contains:
    - Path of the streamlit-authenticator configuration file
    - Paths of the languages files that contains strings of the application
    - Default language to use
- [config/auth.yaml](./config/auth.yaml):
  - The streamlit-authenticator configuration file, more information on the [streamlit-authenticator documentation](https://github.com/mkhorasani/Streamlit-Authenticator)

The [assets/lang/](./assets/lang/) directory contain the lang yaml files containing the strings for each language of the application. The paths can be configured in the [config/app_config.yaml](./config/app_config.yaml) file.

## Deployment

It can be deployed by following the instructions of the [streamlit deployment documentation](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app).

The repository contains a [DockerFile](./Dockerfile) for deploying it with docker, more information can be found of the [streamlit docker deployment documentation](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker).

### Build a docker image

```sh
docker build -t [image_name] .
```

Verifying that the image was built:

```sh
docker images
```

### Run a docker container from the image:

```sh
docker run -p 8501:8501 [image_name]
```

## Contributing

Contributions to enhance the script or fix issues are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is Open Source and is available under the [Apache License 2.0](./LICENSE).
