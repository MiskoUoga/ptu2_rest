from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(_("title"), max_length=150)
    content = models.TextField(_("content"))
    user = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='posts',
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        verbose_name=_("post"), 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField(_("content"))
    user = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)


class PostLike(models.Model):
    post = models.ForeignKey(
        Post, 
        verbose_name=_("post"), 
        on_delete=models.CASCADE,
        related_name='likes',
    )
    user = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("user"), 
        on_delete=models.SET_NULL,
        related_name='post_likes',
        null=True, blank=True,
    )

class CommentLike(models.Model):
    comment = models.ForeignKey(
        Comment, 
        verbose_name=_("comment"), 
        on_delete=models.CASCADE,
        related_name='likes',
    )
    user = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("user"), 
        on_delete=models.SET_NULL,
        related_name='comment_likes',
        null=True, blank=True,
    )