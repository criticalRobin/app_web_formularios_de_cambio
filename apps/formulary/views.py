from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Formulary
from .forms import CreateFormularyForm, UpdateFormularyForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.template.loader import render_to_string
from weasyprint import HTML


# Create your views here.
class ListFormulary(ListView):
    model = Formulary
    template_name = (
        "dashboard.html"  # nombrar el template de dashboard como dashboard.html
    )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # filtrado de formularios por en los que el usuario es revisor
        context["formularys"] = Formulary.objects.all()
        print(context["formularys"])
        context["formulary_reviewer"] = Formulary.objects.filter(
            reviewer=self.request.user
        )
        # filtrado de formularios por en los que el usuario es creador
        context["formulary_pending"] = Formulary.objects.filter(
            user_name=self.request.user.first_name,
            user_surname=self.request.user.last_name,
            user_email=self.request.user.email,
            status="Pending",
        )
        # filtrado de formularios del usuario que han sido aprobados
        context["formulary_approved"] = Formulary.objects.filter(
            user_name=self.request.user.first_name,
            user_surname=self.request.user.last_name,
            user_email=self.request.user.email,
            status="Approved",
        )

        context["formulary_rejected"] = Formulary.objects.filter(
            user_name=self.request.user.first_name,
            user_surname=self.request.user.last_name,
            user_email=self.request.user.email,
            status="Rejected",
        )
        
        return context


class CreateFormulary(CreateView):
    model = Formulary
    template_name = "create.html"
    form_class = CreateFormularyForm
    success_url = reverse_lazy("formulary:form_list")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            user = request.user
            form.user_name = user.first_name
            form.user_surname = user.last_name
            form.user_email = user.email
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)


class UpdateFormulary(UpdateView):
    model = Formulary
    template_name = "update.html"
    form_class = UpdateFormularyForm
    success_url = reverse_lazy("dashboard.html")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)


def form_pdf(request, pk):
    # Obtener el reporte específico usando la PK
    form = get_object_or_404(Formulary, pk=pk)

    # Renderizar la plantilla HTML con los datos
    html_string = render_to_string("form-pdf.html", {"form": form})

    # Generar el PDF
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(presentational_hints=True)

    response = HttpResponse(result, content_type="application/pdf;")
    response["Content-Disposition"] = f"inline; filename=formulario_{form.pk}.pdf"
    return response


