from django import forms  # type:ignore
from coustumes.models import RentedCostumes, BookingRentedCostumes, DressCode


class RentedCostumeForm(forms.ModelForm):
    class Meta:
        model = RentedCostumes
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class BookingRentedCollectionForm(forms.ModelForm):
    # item=forms.CharField(
    #     widget=forms.TextInput(attrs={"readonly": "readonly", "class": "form-control"})
    # )

    class Meta:
        model = BookingRentedCostumes
        fields = ["pairs", "return_date", "address", "item"]
        widgets = {
            "return_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class DressCodeForm(forms.ModelForm):
    class Meta:
        model = DressCode
        fields = ["name","material","image","outfit_type","total_stock","price"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class DressCodeEnquiryForm(forms.ModelForm):
    class Meta:
        model = DressCode
        fields = ["name","material","image","outfit_type","quantity"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        self.fields["image"].required = True




