from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Comment

BAD_WORDS = (
    'rascal',
    'scoundrel',
    # Add to the list at your discretion.
)
WARNING = 'Don\'t argue!'


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

    def clean_text(self):
        """We do not allow swearing in the comments."""
        text = self.cleaned_data['text']
        lowered_text = text.lower()
        for word in BAD_WORDS:
            if word in lowered_text:
                raise ValidationError(WARNING)
        return text
