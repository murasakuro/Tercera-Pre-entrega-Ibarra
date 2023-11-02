from django.urls import path, include
from start.views import welcome, dice, make_dice, dice_bag, make_bag, tray, make_tray

urlpatterns = [
    path('', welcome, name='inicio'),
    path('dados/', dice, name='dice'),
    path('dados/crear', make_dice, name='make_dice'),
    path('bolsas/', dice_bag, name='bags'),
    path('bolsas/crear', make_bag, name='make_bags'),
    path('bandejas/', tray, name='trays'),
    path('bandejas/crear', make_tray, name='make_trays')
]
