from django.shortcuts import render


def style_guide_view(request):
    return render(request, "style_guide/style_guide.html")
