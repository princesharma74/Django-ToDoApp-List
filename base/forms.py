from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    tags = forms.CharField(
        label='Tags',
        max_length=100,
        required=False,
        help_text='Enter tags separated by commas',
    )

    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'tags', 'status')
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Prepopulate tags field with existing tags of the instance
            tags = ', '.join(tag.name for tag in self.instance.tags.all())
            self.initial['tags'] = tags

    def clean_tags(self):
        tags_data = self.cleaned_data['tags']
        tags_list = [tag.strip() for tag in tags_data.split(',') if tag.strip()]
        unique_tags_list = list(set(tags_list))
        tags = []

        for tag_name in unique_tags_list:
            # Get or create tags from the input
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)

        return tags

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()  # Save the many-to-many relationships (tags)
        return instance
