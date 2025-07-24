from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import QuoteSerializer
from .models import Quote

import random

class QuoteApiView(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def list(self, request):
        quotes = self.get_queryset()
        if not quotes.exists():
            return Response({"message": "Цитат пока нет."}, status=status.HTTP_404_NOT_FOUND)

        random_quote = random.choice(quotes)
        serializer = self.get_serializer(random_quote)
        return Response(serializer.data)
    

class QuoteAllApiView(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def list(self, request):
        quotes = self.get_queryset()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)