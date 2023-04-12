from django import forms
# ---------------------------------------------------------------------------
# -------------------------- for contact form -----------------------
# ---------------------------------------------------------------------------
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(
        max_length=500, widget=forms.Textarea(attrs={"rows": 3, "cols": 30})
    )