from django.views.generic import ListView
from django.db.models import Prefetch
from .models import Post, Comment


class PostListView(ListView):
    model = Post

    # def get_queryset(self):
    #     comment_queryset = Comment.objects.all()[:3]
    #     return self.model.objects.all().prefetch_related(
    #         Prefetch('comment', queryset=comment_queryset,
    #                  to_attr='first_comments'))


post_list_view = PostListView.as_view()
