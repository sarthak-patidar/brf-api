from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Branch
from .serializers import BranchSerializer

# Create your views here.


class AllBranchView(APIView):
    """Returns all branches and their details from given bank name and city.
    Usage => /detail/<bank-name>/<city>
    Example: /detail/state-bank-of-india/new-delhi"""

    def get_branches(self, city, bank_name):
        try:
            return Branch.objects.filter(bank_name=bank_name, city=city)
        except Branch.DoesNotExist:
            raise Http404

    def get(self, request, city, bank_name, format=None):
        bank = bank_name.replace("-", " ").upper()
        city = city.replace("-", " ").upper()
        branches = self.get_branches(city=city, bank_name=bank)
        serialized_branches = BranchSerializer(branches, many=True)
        return Response(serialized_branches.data)


class BranchDetailView(APIView):
    """Returns details of a Branch from its IFSC Code.
     Usage => /detail/<ifsc>/
     Example =>  /detail/sbin0000202"""

    def get_detail(self, ifsc):
        try:
            return Branch.objects.get(ifsc=ifsc)
        except Branch.DoesNotExist:
            raise Http404

    def get(self, request, ifsc, format=None):
        ifsc = ifsc.upper()
        branch = self.get_detail(ifsc=ifsc)
        serializer_branch = BranchSerializer(branch)
        return Response(serializer_branch.data)
