from django.db import models
import uuid

# The BaseModel class you posted is an abstract base model in Django. It is used to provide common fields and functionality 
# to other models in a Django project, so you don't have to repeat code in every model

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True