import graphene
from snippets.schema import Query as snippets_query

class Query(snippets_query):  # root type 스키마
    pass

schema_re = graphene.Schema(query=Query)
