# from django import forms
# class RegistrationForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     dob = forms.DateField()
#     age = forms.IntegerField()
#     gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
#     phone = forms.CharField(max_length=20)
#     email = forms.EmailField()
#     address = forms.CharField(widget=forms.Textarea)
#     department = forms.ChoiceField(choices=[('Computer_science', 'Computer_science'), ('Commerce', 'Commerce'), ('Bio_Science', 'Bio_Science'), ('Home_Science', 'Home_Science'), ('Humanities', 'Humanities')])
#     course = forms.ChoiceField(choices=[], required=False)  # We'll populate this dynamically
#     purpose = forms.ChoiceField(choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
#     materials_provided = forms.MultipleChoiceField(choices=[
#         ('notebook', 'Notebook'), ('pen', 'Pen'), ('papers', 'Exam Papers')
#     ], widget=forms.CheckboxSelectMultiple)