from django import forms

class CreateNewRating(forms.Form):
    stars = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 6)],
        widget=forms.Select(attrs={'style': 'font-size: 18px;'}),
    )
    grade = forms.ChoiceField(
        choices=[("A", "A"), ("A-", "A-"), ("B+", "B+"), ("B", "B"), ("B-", "B-"), ("C+", "C+"), ("C", "C"),
                 ("C-", "C-"), ("D+", "D+"), ("D", "D"), ("F", "F")],
        widget=forms.Select(attrs={'style': 'font-size: 18px;'}),
    )
    difficulty = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 6)],
        widget=forms.Select(attrs={'style': 'font-size: 18px;'}),
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40, 'style': 'font-family: Montserrat; font-size: 18px; color: rgb(0, 0, 139);'}),
    )
    anonymous=forms.BooleanField(required= False)
