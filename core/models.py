from django.db import models


class GpuType(models.Model):
    """
    List of Values for types gpu - i.e. RTX 3060, GTX 1060, ...
    Configured via database scripts
    """
    name = models.CharField(max_length=255)
    msrp = models.DecimalField()


class GpuStoreItem(models.Model):
    # Type of gpu from LOV table GpuType
    gpuType = models.ForeignKey(GpuType, on_delete=models.DO_NOTHING)

    # Identifier in store - this is used to search for price drops
    storeId = models.CharField(max_length=1024)

    # "last update time"
    fetchTime = models.DateTimeField()

    # Hyperlink reference - url
    href = models.CharField(max_length=2048)

