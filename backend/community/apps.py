from django.apps import AppConfig


class CommunityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'community'
# class MemoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Memo
#         fields = ['content']
