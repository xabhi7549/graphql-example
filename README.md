# graphql-example

graphql example using ariadne

# Update requirements.txt

`pip freeze > requirements.txt
`

# DB Migration

`docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head
`

# To run

`docker-compose up `
