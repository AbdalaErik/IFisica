# Generated by Django 4.2.7 on 2023-12-10 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
            },
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Ocupação',
                'verbose_name_plural': 'Ocupações',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('ocupacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao', verbose_name='Ocupação')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, verbose_name='Título')),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area', verbose_name='Área')),
            ],
            options={
                'verbose_name': 'Questionário',
                'verbose_name_plural': 'Questionários',
            },
        ),
        migrations.CreateModel(
            name='Subarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area', verbose_name='Área')),
            ],
            options={
                'verbose_name': 'Subárea',
                'verbose_name_plural': 'Subáreas',
            },
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.pessoa')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Integrante',
                'verbose_name_plural': 'Integrantes',
            },
            bases=('app.pessoa',),
        ),
        migrations.CreateModel(
            name='Inventor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.pessoa')),
                ('biografia', models.CharField(max_length=300, verbose_name='Biografia')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
            ],
            options={
                'verbose_name': 'Inventor(a)',
                'verbose_name_plural': 'Inventores(as)',
            },
            bases=('app.pessoa',),
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=2000, verbose_name='Descrição')),
                ('subarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subarea', verbose_name='Subárea')),
            ],
            options={
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
            },
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, verbose_name='Título')),
                ('enunciado', models.CharField(max_length=500, verbose_name='Enunciado')),
                ('alternativa_a', models.CharField(max_length=300, verbose_name='Alternativa A')),
                ('alternativa_b', models.CharField(max_length=300, verbose_name='Alternativa B')),
                ('alternativa_c', models.CharField(max_length=300, verbose_name='Alternativa C')),
                ('alternativa_d', models.CharField(max_length=300, verbose_name='Alternativa D')),
                ('alternativa_e', models.CharField(max_length=300, verbose_name='Alternativa E')),
                ('alternativa_correta', models.CharField(max_length=1, verbose_name='Alternativa correta')),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questionario', verbose_name='Questionário')),
            ],
            options={
                'verbose_name': 'Questão',
                'verbose_name_plural': 'Questões',
            },
        ),
        migrations.CreateModel(
            name='QuestionarioRespondido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_realizacao', models.DateTimeField(verbose_name='Data de realização')),
                ('numero_acertos', models.PositiveIntegerField(verbose_name='Número de acertos')),
                ('respostas_integrante', models.TextField(blank=True, null=True, verbose_name='Respostas do integrante')),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questionario', verbose_name='Questionário')),
                ('integrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.integrante', verbose_name='Integrante')),
            ],
            options={
                'verbose_name': 'Questionário respondido',
                'verbose_name_plural': 'Questionários respondidos',
            },
        ),
        migrations.CreateModel(
            name='Invencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('ano', models.PositiveIntegerField(verbose_name='Ano')),
                ('area', models.ManyToManyField(to='app.area', verbose_name='Área')),
                ('inventor', models.ManyToManyField(to='app.inventor', verbose_name='Inventor(a)')),
            ],
            options={
                'verbose_name': 'Invenção',
                'verbose_name_plural': 'Invenções',
            },
        ),
    ]
