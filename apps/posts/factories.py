import factory
from .models import Post


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    the_image = factory.django.ImageField(color='blue')
