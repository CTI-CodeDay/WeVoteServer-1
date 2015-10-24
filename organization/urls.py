# organization/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views, views_admin

urlpatterns = [
    # views_admin
    url(r'^(?P<organization_id>[0-9]+)/edit/$', views_admin.organization_edit_view, name='organization_edit'),
    url(r'^edit_process/$', views_admin.organization_edit_process_view, name='organization_edit_process'),
    url(r'^$', views_admin.organization_list_view, name='organization_list',),
    url(r'^edit/$', views_admin.organization_edit_view, name='organization_edit'),
    url(r'^export/', views_admin.ExportOrganizationDataView.as_view(), name='organizations_export'),
    # url(r'^import/', views_admin.organizations_import_from_sample_file_view, name='organizations_import'),
    url(r'^new/$', views_admin.organization_new_view, name='organization_new'),
    url(r'^(?P<organization_id>[0-9]+)/pos/$', views_admin.organization_position_list_view,
        name='organization_position_list',),
    url(r'^(?P<organization_id>[0-9]+)/pos/(?P<position_id>[0-9]+)/delete/$',
        views_admin.organization_delete_existing_position_process_form_view,
        name='organization_position_delete',),
    url(r'^(?P<organization_id>[0-9]+)/pos/(?P<position_id>[0-9]+)/$',
        views_admin.organization_edit_existing_position_form_view,
        name='organization_position_edit',),
    url(r'^(?P<organization_id>[0-9]+)/pos/new/$', views_admin.organization_add_new_position_form_view,
        name='organization_position_new',),
    url(r'^pos/edit_process/$', views_admin.organization_save_new_or_edit_existing_position_process_form_view,
        name='organization_position_edit_process'),

    # views
    # This is used for a voter to follow an organization
    url(r'^(?P<organization_id>[0-9]+)/follow/$', views.organization_follow_view,
        name='organization_follow_view',),
    # This is used for a voter to unfollow an organization
    url(r'^(?P<organization_id>[0-9]+)/stop_following/$', views.organization_stop_following_view,
        name='organization_stop_following_view',),
    # # This is used for a voter to ignore an organization
    # url(r'^(?P<organization_id>[0-9]+)/follow_ignore/$', views.organization_follow_ignore_view,
    #     name='organization_follow_ignore_view',),
]
