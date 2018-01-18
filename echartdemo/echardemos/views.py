from django.shortcuts import render, HttpResponse
# from datetime import datetime
import datetime
from django.views.decorators.http import require_GET
from echardemos.models import LineCharts
import json

# Create your views here.


def line_chars(request):
    if request.method == 'POST':
        now = datetime.datetime.now()
        dates = [now.strftime('%Y-%m-%d')]
        lines = LineCharts.objects.all()
        xtimes = []
        values = []
        for line in lines:
            lxtime = line.xtime
            lvalue = line.value
            xtimes.append(str(lxtime))
            values.append(lvalue)

        result = json.dumps({'dates': dates, 'xtimes': xtimes, 'values': values})
        return HttpResponse(result, content_type='application/json')

    return render(request, 'line_demo.html', locals())

