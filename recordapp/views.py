from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from recordapp.forms import RecordForm
from recordapp.models import Record
from recordapp.serializers import RecordSerializer
from rest_framework.renderers import JSONRenderer


class CreateRecordView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'record_main.html'
    success_url = '/record/create/'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return JsonResponse({
            'message': 'success'
        })


class ListRecordView(ListView):
    model = Record
    template_name = 'record_main.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        date = request.GET.get('date')
        query_obj = Record.objects.filter(date=date).select_related()
        serialized_obj = RecordSerializer(query_obj, many=True)
        json_obj = JSONRenderer().render(serialized_obj.data)
        return HttpResponse(json_obj, content_type='application/json')
