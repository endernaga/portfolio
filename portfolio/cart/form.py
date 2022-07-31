from django import forms

class CartAddProductForm(forms.Form):
    QUANTITY = 21
    PRODUCT_QUANTITY_CHOICE = [(i, str(i)) for i in range(QUANTITY)]
    print(QUANTITY)
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICE,
        coerce=int)
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )