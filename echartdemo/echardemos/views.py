from django.shortcuts import render
# from datetime import datetime
import datetime
from django.views.decorators.http import require_GET
from echardemos.models import LineCharts

# Create your views here.


@require_GET
def line_chars(request):
    # now = datetime.datetime.now()
    # dates = now.strftime('%Y-%m-%d')

    return render(request, 'line_demo.html')