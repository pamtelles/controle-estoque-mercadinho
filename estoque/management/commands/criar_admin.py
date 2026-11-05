
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Cria o administrador inicial usando variáveis de ambiente."

    def handle(self, *args, **options):
        username = os.environ.get("ADMIN_USERNAME")
        email = os.environ.get("ADMIN_EMAIL")
        password = os.environ.get("ADMIN_PASSWORD")

        if not all([username, email, password]):
            raise CommandError(
                "Configure ADMIN_USERNAME, ADMIN_EMAIL e ADMIN_PASSWORD."
            )

        User = get_user_model()

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                "Administrador já existe. Nenhuma alteração realizada."
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Administrador criado com sucesso.")
        )
