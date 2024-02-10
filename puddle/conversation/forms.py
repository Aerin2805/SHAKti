from django import forms
from .models import ConversationaMessage

class ConversationaMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationaMessage
        fields = ('content',)
        widgets={
            'content' : forms.Textarea(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            })
        }