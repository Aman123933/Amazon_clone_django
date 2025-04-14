

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
