# Generated by Django 4.2.6 on 2023-10-11 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empregado',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identificador do Empregado', primary_key=True, serialize=False)),
                ('matricula', models.CharField(max_length=30)),
                ('nome', models.CharField(max_length=100)),
                ('data_admissao', models.DateField()),
                ('data_deslig', models.DateField(blank=True, null=True)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=9)),
                ('unidade_salario', models.PositiveSmallIntegerField(choices=[(1, 'Por hora'), (2, 'Por dia'), (3, 'Por semana'), (4, 'Por quinzena'), (5, 'Por mês')], default=5)),
                ('qtd_horas_semana', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'ordering': ['matricula'],
            },
        ),
        migrations.CreateModel(
            name='InssRange',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identificador do range da Tabela do INSS', primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('low_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('high_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'ordering': ['low_amount'],
            },
        ),
        migrations.CreateModel(
            name='IrrfRange',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identificador da faixa da Tabela do IRRF', primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('low_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('high_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('deduction_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'ordering': ['low_amount'],
            },
        ),
        migrations.CreateModel(
            name='IrrfTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identificador da Tabela de IRRF', primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('valid_from', models.DateField()),
                ('simplified_deduction', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dependent_deduction', models.DecimalField(decimal_places=2, max_digits=7)),
                ('irrf_ranges', models.ManyToManyField(to='payroll_lab.irrfrange', verbose_name='irrf_ranges')),
            ],
            options={
                'ordering': ['-valid_from'],
            },
        ),
        migrations.CreateModel(
            name='InssTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identificador da Tabela do INSS', primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('valid_from', models.DateField()),
                ('inss_ranges', models.ManyToManyField(to='payroll_lab.inssrange', verbose_name='inss_ranges')),
            ],
            options={
                'ordering': ['-valid_from'],
            },
        ),
    ]