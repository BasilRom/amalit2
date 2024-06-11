from . import views
from django.urls import path


urlpatterns = [

    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("contacts/", views.contacts, name='contacts'),
    path("categs/<int:cat_id>/", views.show_by_category, name='categs'),
    path("authors/<int:name_id>/", views.show_by_author, name='authors'),
    path("regions/<int:name_id>/", views.show_by_region, name='regions'),
    path("text/<int:text_id>/", views.text, name='text')


]