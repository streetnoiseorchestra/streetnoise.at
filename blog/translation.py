from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import BlogIndexPage, BlogPage, BlogCategory, BlogTag


@register(BlogIndexPage)
class BlogIndexPageTR(TranslationOptions):
    pass


@register(BlogPage)
class BlogPageTR(TranslationOptions):
    fields = ("intro", "body",)


@register(BlogCategory)
class BlogCategoryTR(TranslationOptions):
    fields = ("name", "description")


@register(BlogTag)
class BlogTagTR(TranslationOptions):
    pass
