"""_summary_
    """
from uuid import uuid4
from django.db import models
from tree_queries.models import TreeNode, TreeNodeForeignKey


class Category(TreeNode):
    """_summary_
    Args:
        models (_type_): _description_
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=40)
    parent = TreeNodeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)


class Brand(models.Model):
    """
    Args:
        models (_type_): _description_
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=40, unique=True)


class Product(models.Model):
    """_summary_
    Args:
        models (_type_): _description_
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=50, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeNodeForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
