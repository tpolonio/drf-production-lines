from rest_framework import serializers

from .models import Panel, ProductionLine


class ProductionLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLine
        fields = ("id", "code", "capacity", "active")
        read_only_fields = ("id",)


class PanelSerializer(serializers.ModelSerializer):
    line_code = serializers.CharField(source="production_line.code", read_only=True)

    class Meta:
        model = Panel
        fields = (
            "id",
            "production_ref",
            "production_line",
            "line_code",
            "volume_produced",
        )
        read_only_fields = ("id",)

    def validate_production_ref(self, value):
        value = value.strip().upper()
        if not value.isalnum():
            raise serializers.ValidationError("Panel reference must be alphanumeric")
        return value

    def validate(self, attrs):
        line = attrs.get(
            "production_line", getattr(self.instance, "production_line", None)
        )
        volume = attrs.get(
            "volume_produced", getattr(self.instance, "volume_produced", None)
        )
        if line and volume is not None and volume > line.capacity:
            raise serializers.ValidationError(
                {"volume_produced": "Volume produced cannot exceed line capacity"}
            )
        return attrs
