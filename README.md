DRF
   

**many_to_many branch**

Get list of the many many 
Content & Genre two models

Content can have multiple Genre.
 
One Genre can have More than one Content.

__eg.__ 
    
    One Movie can have both Comedy & Drama
    Under Drama genre there could be multiple movies
 
 
 `@action` decorator used to add custom api method apart from the default viewset methods like put,list,post,delete etc
 

 **Learning Point**
    
    1. To change column values or add mulitple column in Admin Panel Model listing.
        Added listing_fields in `/movies/admin.py`
    2. To add search feature in admin panel
        Added `search_fields` in `/movies/admin.py`
    