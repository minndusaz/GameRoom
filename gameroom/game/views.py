from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from . import models, serializers
from django.views.generic import View


# Create your views here.
def index(request):
    return render(request, 'gameweb/index.html')


class HiScoreListView(View):
    def get(self, request):
        top_players = models.Player.objects.order_by('-score')[:10]

        context = {
            'top_players': top_players
        }

        return render(request, 'gameweb/hiscore.html', context)


class PlayerList(generics.ListAPIView):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer