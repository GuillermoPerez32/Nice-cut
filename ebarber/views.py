from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from ebarber.models import Barber
from ebarber.serializers import BarberSerializer

# Create your views here.


# class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

#     # queryset = Product.objects.filter(stock__gt = 0)
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = []
#     filterset_fields = ['categories']
#     search_fields = ['name']

#     @action(
#         methods=['POST'],
#         detail=True,
#         permission_classes=[IsAuthenticated],
#         serializer_class=RatingSerializer
#     )
#     def rate(self, request, pk=None):
#         """Rate product"""
#         product = self.get_object()
#         user = request.user

#         data = request.data
#         data['user'] = user.id
#         data['product'] = product.uuid
        
#         serializer = RatingSerializer(data=data)

#         serializer.is_valid(True)
#         serializer.save()

#         return Response(status = status.HTTP_200_OK)


# class CartProductViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
#     queryset = Cart_Product.objects.all()
#     serializer_class = CartProductSerializer
#     permission_classes = [IsAuthenticated]
