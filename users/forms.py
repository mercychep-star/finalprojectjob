from django import forms
from  django.contrib.auth.forms import UserCreationForm

from users.models import Account, Profile, Invite


class AccountRegisterForm(UserCreationForm):
    CHOICES = [('is_employee','Employee'),('is_employer', 'Employer')]
    user_types = forms.CharField( label="User Type",widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = Account
        fields = ['email','first_name','last_name']


class  UserUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude = ('user',)

        widgets ={
            'birth_day': forms.DateTimeInput(attrs={'type':'date'})
        }

class InviteEmployeeForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ('date','message')

        widgets = {
            'date':forms.DateInput(attrs={'type':'date'})
        }


