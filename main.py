from ariadne import make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL

from resolvers import query, mutation

schema = make_executable_schema(load_schema_from_path("schema.graphql"), query, mutation)

app = GraphQL(schema, debug=True)
