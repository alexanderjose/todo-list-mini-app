from django import forms
# from django.utils.translation import ugettext as _


class CrearTareaForm(forms.Form):

    STATUS_TAREA = (
        (1, 'Por iniciar'),
        (2, 'Iniciada'),
        (3, 'En progreso'),
        (4, 'Retrasada'),
        (5, 'Resuelta')
    )

    descripcion = forms.CharField(
        max_length=255,
        label='Descripcion',
        widget=forms.Textarea()
    )
    fecha_culminacion = forms.DateField(
        input_formats=['%d/%m/%Y'],
        required=False
        # error_messages={'required': _("Indique una fecha")}
    )
    status = forms.ChoiceField(
        widget=forms.Select, choices=STATUS_TAREA, required=False)
