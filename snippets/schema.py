import graphene
from graphene_django.types import DjangoObjectType
from .models import Snippet

class SnippetType(DjangoObjectType):

    class Meta:
        model = Snippet

class Query(graphene.ObjectType):
    all_snippets = graphene.List(SnippetType)
    snippet = graphene.Field(SnippetType, 
                            id = graphene.Int(),
                            title = graphene.String(),
                            content = graphene.String(),
                            created_at = graphene.Time())

    def resolve_all_snippets(self, info, **kwargs):
        return Snippet.objects.all()
    
    def resolve_snippet(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')
        content = kwargs.get('content')
        created_at = kwargs.get('crated_at')

        if id is not None:
            return Snippet.objects.get(pk=id)

        if title is not None:
            return Snippet.objects.get(title=title)
        
        if content is not None:
            return Snippet.objects.get(content=content)
        
        if created_at is not None:
            return Snippet.objects.get(created_at=created_at)
            
        return None