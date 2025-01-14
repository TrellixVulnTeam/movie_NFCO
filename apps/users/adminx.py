from .models import UserProfile, EmailVerifyRecord

import xadmin
from xadmin import views


class BaseSetting(object):
    #  开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "微电影视频管理"
    site_footer = "2018@huangkai 微电影"
    # 收起菜单
    menu_style = "accordion"


class UserProfileAdmin(object):
    pass


class EmailVerityRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerityRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)