from django.db import models


class ProductionLine(models.Model):
    CODES = {  # noqa: RUF012
        "MDF": "Medium Density Fiberboard",
        "PB": "Particleboard",
        "OSB": "Oriented Strand Board",
    }
    code = models.CharField(max_length=3, choices=CODES)
    capacity = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)


class Panel(models.Model):
    production_ref = models.CharField(max_length=4)
    production_line = models.ForeignKey(
        ProductionLine, on_delete=models.CASCADE, related_name="panels"
    )
    volume_produced = models.PositiveIntegerField()
