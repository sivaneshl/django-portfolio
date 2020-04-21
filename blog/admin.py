from django.contrib import admin
from blog.models import Post, Category, Comment


# No need to add any attributes or methods to these classes. They are used to customize what is shown on the admin
# pages. The default configuration is enough.
class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


# Register the models with the admin classes
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
