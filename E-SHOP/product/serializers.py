from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.CharField(help_text="In Rupees")
    image = serializers.ImageField(max_length=None, allow_empty_file=False,
                                   allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'product_name', 'description', 'price', 'image',)
