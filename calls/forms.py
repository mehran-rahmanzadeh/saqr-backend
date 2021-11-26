from django import forms

from calls.models.getintouch import GetInTouch


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = [
            'name',
            'email',
            'subject',
            'phone',
            'message'
        ]
