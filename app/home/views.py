from django.shortcuts import render


def kitchen_sink_view(request):
    return render(request, "home/kitchen_sink_page.html")
