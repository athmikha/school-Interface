# Generated by Django 4.2.1 on 2023-08-31 15:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Enter a valid phone/mobile number', regex='^\\+?[0-9]+-?[0-9]{6,}$')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=6)),
                ('updated', models.DateField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.city')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.state')),
            ],
        ),
        migrations.CreateModel(
            name='MessageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messagetype', models.CharField(choices=[('Single Message', 'Single Message'), ('Bulk Message', 'Bulk Message')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_association', models.CharField(max_length=200, unique=True)),
                ('date_of_association', models.DateField()),
                ('type', models.CharField(choices=[('Central Government', 'Central Government'), ('State Government', 'State Government'), ('Public Company', 'Public Company'), ('Private Company', 'Private Company'), ('NGO', 'NGO'), ('Foreign', 'Foreign')], max_length=100)),
                ('updated', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='associated_organisation', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.location')),
            ],
            options={
                'ordering': ['name_of_association', '-date_of_association'],
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_association', models.CharField(max_length=200, unique=True)),
                ('date_of_association', models.DateField()),
                ('type', models.CharField(choices=[('Central Government Funded', 'Central Government Funded'), ('State Government Funded', 'State Government Funded'), ('Public Company Funded', 'Public Company Funded'), ('Private Company Funded', 'Private Company Funded'), ('NGO Funded', 'NGO Funded'), ('Foreign Funded', 'Foreign Funded'), ('Self-Funded', 'Self-Funded')], max_length=100)),
                ('updated', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='school_added', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.location')),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.organisation')),
            ],
            options={
                'ordering': ['name_of_association', '-date_of_association'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(help_text='YYYY-MM-DD')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('NA', 'Not applicable')], max_length=2)),
                ('updated', models.DateField(auto_now=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='profile_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateField()),
                ('amount', models.IntegerField()),
                ('utr', models.CharField(max_length=200, unique=True)),
                ('receipt', models.FileField(upload_to='receipts/')),
                ('expiry_date', models.DateField()),
                ('status', models.CharField(choices=[('IN_PROCESS', 'IN_PROCESS'), ('COMPLETED', 'COMPLETED')], max_length=50)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.organisation')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.school')),
            ],
            options={
                'ordering': ['date_of_payment'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('message_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_type', to='accounts.messagetype')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('receiver_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_role', to='auth.group')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
                ('sender_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_role', to='auth.group')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.location'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='TrainingTeam',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.profile')),
            ],
            options={
                'verbose_name': 'Training Team',
                'verbose_name_plural': 'Training Team',
                'ordering': ['first_name', 'last_name'],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('unique_id', models.CharField(max_length=50)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.profile')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.school')),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('unique_id', models.CharField(max_length=50)),
                ('current_class', models.IntegerField(choices=[(1, 'Class 1'), (2, 'Class 2'), (3, 'Class 3'), (4, 'Class 4'), (5, 'Class 5'), (6, 'Class 6'), (7, 'Class 7'), (8, 'Class 8'), (9, 'Class 9'), (10, 'Class 10'), (11, 'Class 11'), (12, 'Class 12')])),
                ('division', models.CharField(max_length=50)),
                ('_parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='accounts.parent')),
                ('_teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='students', to='accounts.teacher')),
                ('preferred_lang', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.language')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.profile')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.school')),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolCoordinator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.profile')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.school')),
            ],
            options={
                'verbose_name': 'School Coordinator',
                'verbose_name_plural': 'School Coordinators',
                'ordering': ['first_name', 'last_name'],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_msg', models.BooleanField(default=False)),
                ('bulk_msg', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='auth.group')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='auth.group')),
            ],
            options={
                'unique_together': {('sender', 'receiver')},
            },
        ),
        migrations.CreateModel(
            name='ClassCoordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classVal', models.IntegerField(choices=[(1, 'Class 1'), (2, 'Class 2'), (3, 'Class 3'), (4, 'Class 4'), (5, 'Class 5'), (6, 'Class 6'), (7, 'Class 7'), (8, 'Class 8'), (9, 'Class 9'), (10, 'Class 10'), (11, 'Class 11'), (12, 'Class 12')])),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.teacher')),
            ],
            options={
                'ordering': ['teacher__first_name', 'teacher__last_name'],
            },
        ),
        migrations.CreateModel(
            name='CentralCoordinator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.organisation')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.profile')),
            ],
            options={
                'verbose_name': 'Central Coordinator',
                'verbose_name_plural': 'Central Coordinators',
                'ordering': ['first_name', 'last_name'],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
