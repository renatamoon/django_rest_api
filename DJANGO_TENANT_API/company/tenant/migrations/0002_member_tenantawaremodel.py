# Generated by Django 2.2.28 on 2022-08-03 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantAwareModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tenant.TenantAwareModel')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
    ]
