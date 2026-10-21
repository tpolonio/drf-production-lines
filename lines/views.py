from rest_framework import viewsets
from rest_framework.response import Response

# from rest_framework.views import APIView
from .models import ProductionLine
from .serializers import ProductionLineSerializer

""" class LineApiView(APIView):
    def get(self, request):
        lines = ProductionLine.objects.all()
        return Response(ProductionLineSerializer(lines, many=True).data)

    def post(self, request):
        serializer = ProductionLineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)
 """

# ------------------------- OR using VIEWSETS


class LineViewSet(viewsets.ModelViewSet):
    queryset = ProductionLine.objects.all()
    serializer_class = ProductionLineSerializer

    def list(self, request):
        queryset = ProductionLine.objects.all()
        serializer = ProductionLineSerializer(queryset, many=True)
        return Response(serializer.data)
