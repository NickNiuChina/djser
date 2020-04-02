from django.contrib import admin

# Register your models here.


from api.models import UnitInfo
 

#模型的管理器
class UnitInfoAdmin(admin.ModelAdmin):
    list_display=('id', 'pcid', 'order', 'customer', 'all_mac', 'ipmi_mac', 'workstation')
    list_filter = ['pcid']
    search_fields = ['pcid', 'order', 'customer',]


# Register your models here.
admin.site.register(UnitInfo, UnitInfoAdmin)
