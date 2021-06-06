from django import forms


class CouponApplyForm(forms.Form):
    """
    Форма для ввода номера купона при оформлении заказа
    """
    code = forms.CharField()
