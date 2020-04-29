DRF
**authentication branch**

Added authentication in two ways 
   1. Authentication with class base view(`class_api_view_generic.py`)
   2. Function base api view decorator.(`fun_api_view_decorator.py`) 

**Function base decorator api**

This will provide default template for the api view.
Django's default api form view.

**key point learned & added**
   1. `fields` , `exclude` related in serializer meta(Ref class GenreSerializer[movies/serializers.py])
   2. Used `__str__` override function in model to display name in admin panel instead object(1),Object(2)
   3. In Function base API View decorator authentication_classes & api_view decorator should be in order as
   mentioned in comment of `fun_api_view_decorator.py`
   

**authentication branch**
Added token base Authentication.

class `GenreGenericAPIView`
 
 1. To use basic authorization required to add below classes in `authentication_classes`
 
 `authentication_classes = [SessionAuthentication, BasicAuthentication]`
 
 2. For the token base authorization django's default `TokenAuthentication` can be used.
    Need to add in settings.py install app `rest_framework.authtoken`
    
    1.  But to get expiration & created time used `django-expiring-token`[https://pypi.org/project/django-expiring-token/] package.
        1. Need to add in settings.py install app  `django_expiring_token`
        2. `DEFAULT_AUTHENTICATION_CLASSES` in `REST_FRAMEWORK` of settings.py
        3. expiration default duration in `settings.py` `EXPIRING_TOKEN_DURATION = timedelta(minutes=5)` 
   
