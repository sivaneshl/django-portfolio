from django.db import models

# Three separate database tables for the blog:
# * Post
# * Category
# * Comment


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True - This assigns the current date and time to this field whenever an instance of this class is
    # created.

    last_modified = models.DateTimeField(auto_now=True)
    # auto_now=True - This assigns the current date and time to this field whenever an instance of this class is saved.
    # That means whenever you edit an instance of this class, the date_modified is updated.

    # We want to link our models for categories and posts in such a way that many categories can be assigned to many
    # posts. ManytoManyField field type links the Post and Category models and allows us to create a relationship
    # between the two tables.
    categories = models.ManyToManyField('Category', related_name='posts')
    # The ManyToManyField takes two arguments. The first argument is the model with which the relationship is, in this
    # case its Category. The second argument allows us to access the relationship from a Category object, even though we
    # haven’t added a field there. By adding a related_name of posts, we can access category.posts to give us a list of
    # posts with that category.


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # ForeignKey defines a many to one relationship. The ForeignKey field takes two arguments. The first is the other
    # model in the relationship, in this case, Post. The second tells Django what to do when a post is deleted. If a
    # post is deleted, then we don’t want the comments related to it hanging around. We, therefore, want to delete them
    # as well, so we add the argument on_delete=models.CASCADE.





