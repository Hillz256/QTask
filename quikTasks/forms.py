from django.forms import ModelForm
from quikTasks.models import Poem


class PoemCreateForm(ModelForm):

    class Meta:
        model = Poem
        fields = [
            'title',
            'category',
            'description',
            'author'
        ]
