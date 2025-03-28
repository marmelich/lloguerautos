
from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import timedelta
from lloguer.models import Automobil, Reserva 
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Crea 4 coches, 4 usuarios y sus reservas cada vez que se ejecuta"

    def handle(self, *args, **kwargs):
        faker = Faker()

        # ---------- Automóviles ----------
        for _ in range(4):
            automobil = Automobil.objects.create(
                marca=faker.company(),
                model=faker.word(),
                matricula=faker.unique.license_plate()
            )
            self.stdout.write(f'Automobil creado: {automobil}')

        # ---------- Usuarios ----------
        for _ in range(8):
            username = faker.unique.user_name()
            user = User.objects.create_user(
                username=username,
                email=faker.email(),
                password='1234'  # puedes mejorar esto luego
            )
            self.stdout.write(f'Usuario creado: {user.username}')

        # ---------- Reservas ----------
        automobiles = list(Automobil.objects.order_by('-id')[:4])  # los 4 últimos creados
        users = list(User.objects.order_by('-id')[:4])             # los 4 últimos creados

        for user in users:
            n_reservas = random.randint(1, 2)
            for _ in range(n_reservas):
                automobil = random.choice(automobiles)

                # Generar una data_inici que no choque
                for _ in range(10):  # intenta hasta 10 veces evitar duplicados
                    data_inici = faker.date_between(start_date='-30d', end_date='+30d')
                    if not Reserva.objects.filter(automobil=automobil, data_inici=data_inici).exists():
                        break
                else:
                    self.stdout.write(self.style.WARNING(f'No se pudo crear reserva para {user} (conflicto de fechas)'))
                    continue

                data_fi = data_inici + timedelta(days=random.randint(1, 10))

                Reserva.objects.create(
                    automobil=automobil,
                    user=user,
                    data_inici=data_inici,
                    data_fi=data_fi if random.choice([True, False]) else None
                )
                self.stdout.write(f'Reserva creada: {user.username} -> {automobil} desde {data_inici}')

        self.stdout.write(self.style.SUCCESS("Seeder ejecutado correctamente ✅"))
