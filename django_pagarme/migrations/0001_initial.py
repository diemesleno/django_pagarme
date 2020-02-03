# Generated by Django 3.0.3 on 2020-02-03 19:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellableOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('max_installments', models.IntegerField(default=12, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('default_installment', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('free_installment', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('interest_rate', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('payments_methods', models.CharField(choices=[('boleto', 'Somente Boleto'), ('credit_card', 'Somente Cartão de Crédito'), ('credit_card,boleto', 'Cartão de Crédito ou Boleto')], default='credit_card,boleto', max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Sellable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('price', models.PositiveIntegerField(verbose_name='Preço em Centavos')),
                ('tangible', models.BooleanField(verbose_name='Produto físico?')),
                ('default_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellables', to='django_pagarme.SellableOption')),
            ],
        ),
    ]