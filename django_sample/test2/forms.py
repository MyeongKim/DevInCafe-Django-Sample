from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2')


    def save(self, commit=True, args=(), **kwargs):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = user.cleaned_data.get('username')
        if commit:
            user.save()
        return user
