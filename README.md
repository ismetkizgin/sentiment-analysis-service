<div align="center">
  <a href="http://nestjs.com/" target="blank"><img src="https://www.python.org/static/img/python-logo@2x.png" width="200" alt="Nest Logo" /></a>
  <h1>SENTIMENT ANALYSIS SERVICE</h1>
</div>


## Description
It is a service that makes good and bad prediction of messages that come to an application. `Sentiment Analysis` algorithm was used as machine learning algorithm and served with `Python Flask`. You can examine the graph of the data in the data set from the visual below. Those with a positivity value of `0 represent a negative message`, and those with a `1 represent a positive message`.

<p align="center">
  <img src="https://raw.githubusercontent.com/ismetkizgin/sentiment-analysis-service/master/model/graph.png">
</p>

## Instructions
### Installation

```bash
$ cd model
$ pip3 install --no-cache-dir -r requirements.txt
$ python3 model.py
$ cd ../service
$ pip3 install --no-cache-dir -r requirements.txt
```

### Running the app

```bash
# The following command must be executed within the `service` folder.
$ python3 app.py
```

### Docker Compose
By creating the `docker-compose.yml` file, it is possible to deploy the project with `docker` commands below. You can visit the [Docker Hub Repository](https://hub.docker.com/r/ismetkizgin/sentiment-analysis-service/tags) to review the versions.
```yml
version: "3"
services:
  serve:
    container_name: sentiment-analysis-service
    image: ismetkizgin/sentiment-analysis-service:latest
    expose:
      - ${PORT}
    restart: always
    ports:
      - "${PORT}:${PORT}"
    env_file:
      - .env
```

```bash
$ docker-compose up -d
```
## Environment Variables

| Variable Name           | Description                                                                                             | Required | Default  |
| ----------------------- | ------------------------------------------------------------------------------------------------------- | -------- | -------- |
| ENVIRONMENT             | Specifies the environment name.                                                                         | NO       | -        |
| CORS                    | Website endpoints can be defined for Cors safety.                                                       | NO       | *        |
| PORT                    | It is determined which port will be deploy.                                                             | NO       | 3310     |
| BODY_SIZE_LIMIT         | Specifies the maximum size of the data that will come from the body during the request.(Type: MB)       | NO       | 1        |
| API_KEY                 | It allows to add an api key control to the service for security during service use.                     | NO       | -        |

## Request Examples

REQUEST
```json
// POST {{ENDPOINT}}/{{GLOBAL_PREFIX}}/predict
{
    "text": "Uygulama kötü bir şekilde tasarlanmış ve gereksiz."
}
```
RESPONSE
```json
{
    "predictState": true
}
```
## License

Sentiment analysis service is [GNU licensed](LICENSE).
