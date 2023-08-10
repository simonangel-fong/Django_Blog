from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    ''' 
    Table of post
    Rules:
        1. Only authenticated user can manipulate a post
        2. Title contains only less than 80 chars.
        3. Create time is automatically logged.
        4. A post can be a draft, when it is created, or be published, when the published_date is not null.
        5. If a post is published, the published_date is set to be now().
    '''
    # author, refer to auth User.
    # Only the registered user can post.
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )
    # the title of current post
    # allow only 80 characters
    title = models.CharField(
        max_length=80
    )
    # the content of current post
    # Can be blank
    content = models.TextField(
        blank=True
    )
    # the date when current post is created.
    # default: timezone.now(). Using settings.TIME_ZONE variable.
    created_date = models.DateField(
        default=timezone.now
    )
    # the date when current post is set to be published.
    # It can be blan or null when the post is not set published.
    published_date = models.DateField(
        blank=True, null=True
    )

    def publish(self):
        ''' Publishes current post '''
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        ''' Return a list of related approved comments '''
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        ''' the url for current post '''
        # using reverse to transform URLConf name into a url of current post.
        # passing the pk of current post an argument.
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        ''' str() method of current post'''
        return f'{self.title} - {self.author}'

    class Meta:
        # OrderBy created_date in descending order.
        ordering = ["-created_date"]
        # set index for post table
        indexes = [
            models.Index(fields=["author",]),
            models.Index(fields=["title",]),
            models.Index(fields=["created_date",]),
        ]


class Comment(models.Model):
    '''
    Table of Comment
    Rule:
        1. Anonymous user can create a comment.
        2. User to comment should leave an author name
        3. A comment is related to a post.
        4. When a comment is created, created date will be logged.
        5. By default, any comment is not approved.
            When comment is approved, is_approved will be marked.
    '''
    # the related post of current comment.
    post = models.ForeignKey(
        to="AppBlog.Post", on_delete=models.CASCADE
    )
    # the author of current comment.
    # Allows only 64 chars.
    author = models.CharField(
        max_length=64
    )
    # the comment content.
    content = models.TextField()
    # the date when current comment is created.
    # default: timezone.now().
    created_date = models.DateField(
        default=timezone.now
    )
    # whether the current comment is approved.
    # default: current comment is not approved.
    is_approved = models.BooleanField(
        default=False
    )

    def approve(self):
        ''' Approves the current comment '''
        self.is_approved = True
        self.save()

    def get_absolute_url(self):
        ''' the url is post_list after the current comment is manipulated '''
        return reverse("post_list")

    def __str__(self):
        ''' str() method of current comment '''
        return self.content

    class Meta:
        # OrderBy created_date in descending order.
        ordering = ["-created_date"]
        # set index for comment table
        indexes = [
            models.Index(fields=["post",]),
            models.Index(fields=["created_date",]),
        ]