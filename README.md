DRF
   

Function based apiview example

#Point notes
    What is many = True ?
    What is safe ?
    What is DoesNotExist ?

#GenreSerializer class
    Meta class required to define fields.
    In this example only fields property added


**api_view_decorator branch**


**Function base decorator api**

This will provide default template for the api view.
Django's default api form view.

**key point learned & added**
   1. `fields` , `exclude` related in serializer meta(Ref class GenreSerializer[movies/serializers.py])
   2. Used `__str__` override function in model to display name in admin panel instead object(1),Object(2)
   

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
   

**crudel_operation**
    
    Override default modelviewset method for the api
    
    pagination added
     
    Changing default error message for blank and null field related

https://docs.google.com/document/d/1o8d0A0Hwf54Vjkv6AD1pq2Q2iYWOgpfzcCiaOIMbiPA/edit?usp=sharing
    
    