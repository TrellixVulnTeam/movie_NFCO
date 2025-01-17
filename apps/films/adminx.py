from .models import Tag, Movie, Region, Language, Comment

import xadmin


class TagAdmin(object):
    pass


class MovieAdmin(object):
    list_display = ['name', 'year', 'name_other', 'director', 'actor', 'tags', 'image', 'languages',
                    'region_id', 'intro',  'duration', 'score_douban', 'score_imdb', 'add_time']
    list_filter = ['year', 'director', 'tags', 'languages', 'region_id', 'score_douban', 'score_imdb']
    search_fields = ['name', 'name_other', 'director', 'actor', 'tags__name', 'image', 'languages__name',
                     'region_id__name', 'duration', 'intro']


class MovieLikeAdmin(object):
    pass


class RegionAdmin(object):
    pass


class LanguageAdmin(object):
    pass


class CommentAdmin(object):
    pass


xadmin.site.register(Movie, MovieAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Region, RegionAdmin)
xadmin.site.register(Language, LanguageAdmin)
xadmin.site.register(Comment, CommentAdmin)
