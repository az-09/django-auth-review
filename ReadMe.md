### Part 2
    django-guardian: permission for object instance level
    
    assign a permission to user: 
    
        perm = Permission.objects.get(codename='view_surveyassignment')

        assign_perm(perm, assigned_to, assigned_survey)

    assign a permission to group:

        group = Group.objects.create(name=f"survey_{survey.id}_result_viewers")
        
        assign_perm('can_view_results', group, survey)


### Part 3

    Used django-allauth instead of social-auth-app-django

    pip install django-allauth==0.42.0 python-dotenv==0.14.0

    settings.py

        import os
        from dotenv import load_dotenv
        load_dotenv(verbose=True, dotenv_path=os.path.join(BASE_DIR, '.env'))


        INSTALLED_APPS = [
            ...

            'django.contrib.sites',
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'allauth.socialaccount.providers.google'
        ]


        AUTHENTICATION_BACKENDS = [
            ...
            'allauth.account.auth_backends.AuthenticationBackend',
        ]


        SOCIALACCOUNT_PROVIDERS = {
            'google': {
                'APP': {
                    'client_id': os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'),
                    'secret': os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'),
                    'key': ''
                }
            }
        }

    urlpatterns = [
        ...
        path('accounts/', include('allauth.urls')),
    ]

    python manage.py migrate

    login.html

        {% load socialaccount %}

        <label for="" class="label">Or login with Google</label>
            <div class="field">
            <div class="control">
                <a href="{% provider_login_url 'google' %}" class="button">
                <span class="icon">
                    <i class="fab fa-google-plus-g"></i>
                </span>
                <span>Google</span>
                </a>
            </div>
        </div>

    127.0.0.1:8000/admin/

    Add a site

        Domain name: 127.0.0.1:8000

        Display name: 127.0.0.1:8000 


### Reference

https://thecodinginterface.com/blog/django-auth-part1/

https://thecodinginterface.com/blog/django-auth-part2/

https://thecodinginterface.com/blog/django-auth-part3/ 

https://medium.com/@whizzoe/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5

https://django-allauth.readthedocs.io/en/latest/installation.html

https://thecodinginterface.com/blog/django-auth-part4/

