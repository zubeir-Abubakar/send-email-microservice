from rest_framework import serializers

class MailSerializer(serializers.Serializer):
    recipient = serializers.EmailField()
    sender = serializers.EmailField()
    subject = serializers.CharField()
    body = serializers.CharField()
    cc = serializers.CharField(allow_blank=True)
    bcc = serializers.CharField(allow_blank=True)

class TemplateMailSerializer(MailSerializer):
    body = None
    htmlBody = serializers.CharField(source='body')