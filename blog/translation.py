from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from taggit.models import Tag

from .models import (
    BlogIndexPage,
    BlogPage,
    BlogCategory,
    BlogTag
)

@register(BlogIndexPage)
class BlogIndexPageTR(TranslationOptions):
    pass

@register(BlogPage)
class BlogPageTR(TranslationOptions):
    fields = (
        'body',
    )


@register(BlogCategory)
class BlogCategoryTR(TranslationOptions):
    fields = (
        'name', 'description'
    )

@register(Tag)
class TagTR(TranslationOptions):
    fields = ( 'name', 'slug' )


@register(BlogTag)
class BlogTagTR(TranslationOptions):
    pass
