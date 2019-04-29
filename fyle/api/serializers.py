from rest_framework.serializers import ModelSerializer
from .models import Branch


class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = [
            "ifsc",
            "bank_id",
            "branch",
            "address",
            "city",
            "district",
            "state",
            "bank_name"
        ]
