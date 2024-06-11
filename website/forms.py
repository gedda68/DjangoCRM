from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
#from formset.richtext.widgets import RichTextarea




class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'email address'}))
    first_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'first name'}))
    last_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'last name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email' ,'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
        
# Add Record Form
class AddRecordForm(forms.ModelForm):
    title = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Title", "class":"form-control"}), label="")
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    middle_name = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Middle Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    address_line1 = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Address Line 1", "class":"form-control"}), label="")
    address_line2 = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Address Line 2", "class":"form-control"}), label="")
    city = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    state = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
    postcode = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Postcode", "class":"form-control"}), label="")
    country = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Country", "class":"form-control"}), label="")
    date_of_birth = forms.DateField(label="date of birth", widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}), input_formats=["%Y-%m-%d"])
   # bio = forms.CharField(richtext_widget = RichTextarea(control_elements=[controls.Bold(),controls.Italic(),controls.Heading(),]))
    
    class Meta:
        model = Record
        exclude = ("user",)

    