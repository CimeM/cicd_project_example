# CICD ideal project example (template)
This project is an ideal project where testing and local developmet is better organised to support CICD actions.

Motivations:

- de-complexify the CICD pipelines
- build and run tests locally
- re-use configuration

# Use cases

## Case1: Local development

1. run mongodb and app1
`docker-compose up --build traefik app1 mongodb --build`
2. develop and run app2 locally

## Case2: Integration testing (Level1)

1. Test container runs test examples against individual containers
`docker-compose --profile integrationtestL1 up -d --build`

> You can use this example in pipeline

## Case3: Integration testing (Level2)

1. Test container runs test examples against multiple containers
`docker-compose --profile integrationtestL2 up -d --build`

> You can use this example in pipeline

## Case4: integrate to pipeline

``` bash
docker-compose --profile integrationtestL2 up -d --build --env-file .cicd.env --file docker-compose.prod.yaml
```

# Cleanup

``` bash 
docker-compose down && docker-compose rm -f
```