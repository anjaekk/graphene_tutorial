from django.contrib import admin
from django.urls import path, include
from graphene.types import schema
from graphene_django.views import GraphQLView
import graphql
from .schema import schema_re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema_re)),
]
