# Generated by Django 3.1.7 on 2021-03-23 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrient_state', '0003_fixing_dabase_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManageModelBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='historynutrientsdata',
            name='active',
            field=models.BooleanField(db_column='active', default=False),
        ),
        migrations.AddField(
            model_name='lettucenutrients',
            name='active',
            field=models.BooleanField(db_column='active', default=False),
        ),
        migrations.AlterField(
            model_name='lettucenutrients',
            name='ph_value',
            field=models.FloatField(db_column='ph_value'),
        ),
        migrations.CreateModel(
            name='HistoryNutrientsDataManager',
            fields=[
                ('managemodelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nutrient_state.managemodelbase')),
            ],
            bases=('nutrient_state.managemodelbase',),
        ),
        migrations.CreateModel(
            name='LettuceNutrientsManager',
            fields=[
                ('managemodelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nutrient_state.managemodelbase')),
            ],
            bases=('nutrient_state.managemodelbase',),
        ),
    ]