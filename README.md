# Containers

## About

This project serves as a learning ground to increase my skills with Docker, Docker-compose and Kubernetes. 

This application is a simple Python Flask application, with a PostgreSQL database and an API built in FastAPI to communicate with the database. In other words, this application is split into 3 microservices which created using docker-compose, and some docker images that can be found within the relevant folders.

## Getting Started
To begin, ensure that you have Docker installed from [https://www.docker.com/](https://www.docker.com) and open Docker. Once running, use a commandline terminal such as `cmd` or `WSL` and navigate to the root directory of the project, which will be `containers/` if you have just cloned this. 

From here, enter `docker compose build` into your terminal. You'll see that the Docker images begin building themselves. Once complete, simply run `docker compose up`. After a few seconds you should see "`containers-web-1  |  *Running on all addresses`". 

That's it! You will now be able to open the home page on `localhost:5000` in your browser. 

Alternatively, you can access the API directly by navigating to `localhost:8000` and following the instructions to get the information. For a more detailed look into the API, navigate to `localhost:8000/docs` to look through the swagger UI.

