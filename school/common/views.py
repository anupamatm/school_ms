from django.shortcuts import render
from django.views.decorators.cache import cache_control
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def home(request):
    return render(request,"home.html")



# views.py

import json

def chart(request):
    chart_data = [
        {
            'position': 'Position 1',
            'candidates': [
                {'name': 'Candidate A', 'votes': 10},
                {'name': 'Candidate B', 'votes': 5},
                {'name': 'Candidate C', 'votes': 8}
            ]
        },
        {
            'position': 'Position 2',
            'candidates': [
                {'name': 'Candidate X', 'votes': 15},
                {'name': 'Candidate Y', 'votes': 8},
                {'name': 'Candidate Z', 'votes': 10}
            ]
        },
        # ... more positions
    ]
    
    return render(request, 'common/chart.html', {'chart_data': chart_data})
