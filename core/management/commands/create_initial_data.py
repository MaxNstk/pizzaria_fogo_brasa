from django.core.management import BaseCommand
from core.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        try:
            max = User.objects.create_user(username='max',password='max123',first_name='Max',last_name='Starke',
            email='max@pizzariafogobrasa.com', phone_number='88888-888', cpf_cnpj='000.000.000-00')

            admin = User.objects.create_user(username='admin',password='admin123',is_superuser=True,
            first_name='admin',email='admin@pizzariafogobrasa.com', phone_number='99999-9999', cpf_cnpj='99.999.999/9999-99')
            
            joao = User.objects.create_user(username='joao',password='joao123',first_name='João',last_name='Krieger',
            email='max@pizzariafogobrasa.com', phone_number='99999-9999', cpf_cnpj='000.000.000-99')
        except Exception as e:
            admin = User.objects.get(username='admin')
            max = User.objects.get(username='max')
            joao = User.objects.get(username='joao')

        size_gg = Size.objects.get_or_create(short_name='GG', description='Gigante')

        flavor_calabresa =  Flavor.objects.get_or_create(name='Calabresa', description='Molho de tomate, queijo mussalera e muita calabresa!')

        pizza_calabresa_gg = Pizza.objects.get_or_create(flavor=flavor_calabresa, size=size_gg, price=80)

        pedido1 = Order.objects.get_or_create(customer=max).add_pizza(pizza_calabresa_gg)
        feedback1 = FeedBack.objects.get_or_create(rating=FeedBack.GREAT, description='Estava incrível!')
        pedido1.feedback = feedback1