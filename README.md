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