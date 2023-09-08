from django import forms
from .models import MILL

class destform(forms.ModelForm):
    class Meta:
        model=MILL
        fields=("OWNER_NAME","COST","UPLOAD_IMAGE1","UPLOAD_IMAGE2","UPLOAD_IMAGE3","ADDRESS","ENTER_LOCATION","STATE","CHOOSE_TYPE","VIDEO")
