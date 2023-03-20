from django import forms

from .models import CourseModel

# class AddCourseForm(forms.Form):
#     # title, email, ta number, discussion
#     # hours expected, descrption
#     OPTIONS = (
#         ('1', '1'),
#         ('2', '2'),
#         ('3', '3'),
#         ('4', '4')
#     )
#     DISCUSSION = [
#         ('YES', 'Yes'),
#         ('NO', 'No'),
#     ]
#     course_title = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder': 'Course Title'}))
#     email = forms.EmailField()
#     discussion = forms.ChoiceField(
#         widget=forms.RadioSelect, choices=DISCUSSION)
#     ta_required = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
#     description = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder': 'Description for course'}))

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = [
            'course_title',
            'email',
            'discussion',
            'ta_required',
            'description'
        ]