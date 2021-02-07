# Serving React/Angular apps with Django

Create and built the app in the root directory. We then have to serve up the built version to the users that is available at `./frontend_path/build/`

## Enable CORS (for development)

> For ease of development, this project stores the dev-specific settings in `local_settings.py` and appends them to appropriate properties when `DEBUG = True` 

In `settings.py`
- Add `'corsheaders'` in the `INSTALLED_APPS` setting
- Update the setting `MIDDLEWARE`, add `'corsheaders.middleware.CorsMiddleware','django.middleware.common.CommonMiddleware'`
- Add new setting `CORS_ORIGIN_ALLOW_ALL = True` 

## Set path to static files

- Create `STATICFILES_DIRS` in `settings.py`
    ```
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'recipe-frontend', "build", "static"),
    )
    ```
- This serves all the required css/js files for the html file to collect to work

## Serve the file within Django

- Create a new view that renders the built app.
    ```python
    # core/views.py
    def index(request):
        # the path must be set relatively as they are aggregated by collectstatic
        return render(request, "recipe-frontend/build/index.html")
    ```
- The html served to client is derived from the Django's `TEMPLATES` setting as a relative path

- Update the `urls.py` to serve the view at the preferred endpoint. (Generally, the root)

    ```python
    # core/urls.py
    # ...imports...
    from .views import index

    urlpatterns = [
        # api, admin ...
        path('', index, name="index") # Serve React build
    ]
    ```