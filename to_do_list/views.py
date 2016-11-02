from django.views.generic import TemplateView, View, UpdateView, CreateView
from django.http import JsonResponse, HttpResponse
import json
import datetime

# Create your views here.
from to_do_list.models import ToDoList


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]


class IndexView(TemplateView):
    template_name = "base.html"


class GetDataView(TemplateView):
    def get(self, *args, **kwargs):
        all_list = ToDoList.objects.values('id', 'name', 'checked',
                                           'description')
        all_dict = ValuesQuerySetToDict(all_list)
        serialized_q = json.dumps(all_dict)
        return HttpResponse(serialized_q)


def create_new(request):
    request_body = json.loads(request.body)
    name = request_body.get('name')
    checked = request_body.get('checked')
    description = request_body.get('textarea')
    response = {}
    if request.method == "POST":
        new_for_to_do = ToDoList()
        new_for_to_do.name = name
        new_for_to_do.checked = checked
        new_for_to_do.description = description
        new_for_to_do.save()
        response['succses'] = True

    return JsonResponse(response)


def update(request, to_do_list_pk):
    response = {}
    request_body = json.loads(request.body)
    if request.method == "POST":
        name = request_body.get('name')
        checked = request_body.get('checked')
        description = request_body.get('textarea')
        get_item = ToDoList.objects.get(id=to_do_list_pk)
        get_item.name = name
        get_item.checked = checked
        get_item.description = description
        get_item.date_modified = datetime.datetime.now()
        get_item.save()
        response['succses'] = True
    return JsonResponse(response)


def delete(request, to_do_list_pk):
    response = {}
    if request.method == "POST":
        ToDoList.objects.get(id=to_do_list_pk).delete()
        response['succses'] = True
    return JsonResponse(response)
