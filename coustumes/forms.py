from django import forms  # type:ignore
from coustumes.models import RentedCostumes


class RentedCostumeForm(forms.ModelForm):
    class Meta:
        model = RentedCostumes
        fields = "__all__"
