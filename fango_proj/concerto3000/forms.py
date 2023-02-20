from django import forms

class ShowForm(forms.Form):
    kategorie = forms.CharField(label='Kategorie',
                                widget=forms.Select(choices=[('Festival', 'Festival'), ('Konzert', 'Konzert') ,
                                                             ('Sport', 'Sport'), ('Theater', 'Theater'),
                                                             ('Veranstaltung', 'Veranstaltung')]))
    genre = forms.CharField(label='Genre',
                            widget=forms.Select(choices=[('Advanced Rock', 'Advanced Rock'), ('Austro', 'Austro'),
                                                         ('Basketball', 'Basketball'), ('Elektro', 'Elektro'),
                                                         ('Fußball', 'Fußball'), ('Hamburger Schule', 'Hamburger Schule'),
                                                         ('Kabarett', 'Kabarett'), ('Pop', 'Pop'),
                                                         ('Rap', 'Rap'), ('Rock', 'Rock'),
                                                         ('Singer/Songwriter', 'Singer/Songwriter'), ('Theater', 'Theater'),
                                                         ('Veranstaltung', 'Veranstaltung'), ('Vortrag', 'Vortrag')]))
    artist = forms.CharField(label='Artist', max_length=50)
    ort = forms.CharField(label='Ort', max_length=50)
    location = forms.CharField(label='Location', max_length=50)
    kosten = forms.DecimalField(label='Kosten', max_digits=5, decimal_places=2)
    jahr = forms.CharField(label='Jahr', max_length=4)

class TXTForm(forms.Form):
    txt_file = forms.FileField(label='.txt-File')