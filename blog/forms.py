from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={  # This tells Django to load this field as an HTML text input element
            'class': 'form-control',
            'place-holder': 'Your Name'
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={   # so that the field is rendered as an HTML text area element
            'class': 'form-control',
            'place-holder': 'Leave a comment!'
        })
    )