urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^password-change-done/$',
        auth_views.password_change_done,
        {'template_name': 'pollster/password_change_done.html'},
        name='password_change_done'
        ),
    #...
]
