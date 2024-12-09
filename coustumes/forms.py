from django import forms  # type:ignore
from coustumes.models import RentedCostumes


class RentedCostumeForm(forms.ModelForm):
    class Meta:
        model = RentedCostumes
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
