from django.core.management import BaseCommand
from core.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        try:
            _max = User.objects.create_user(username='max',password='max123',first_name='Max',last_name='Starke',
            email='max@pizzariafogobrasa.com', phone_number='88888-888', cpf_cnpj='000.000.000-00')

            admin = User.objects.create_user(username='admin',password='admin123',is_superuser=True,
            first_name='admin',email='admin@pizzariafogobrasa.com', phone_number='99999-9999', cpf_cnpj='99.999.999/9999-99')
            
            joao = User.objects.create_user(username='joao',password='joao123',first_name='João',last_name='Krieger',
            email='max@pizzariafogobrasa.com', phone_number='99999-9999', cpf_cnpj='000.000.000-99')
        except Exception as e:
            admin = User.objects.get(username='admin')
            _max = User.objects.get(username='max')
            joao = User.objects.get(username='joao')

        #size
        size_gg = Size.objects.get_or_create(short_name='GG', description='Gigante')
        size_g = Size.objects.get_or_create(short_name='G', description='Grande')
        size_m = Size.objects.get_or_create(short_name='M', description='Média')
        size_p = Size.objects.get_or_create(short_name='P', description='Pequena')

        #flavor
        flavor_calabresa =  Flavor.objects.get_or_create(name='Calabresa', description='Molho de tomate, queijo mussalera e muita calabresa!')
        flavor_mexicana =  Flavor.objects.get_or_create(name='Mexicana', description='Carne moída apimentada e uma mistura de queijos cheddar, muçarela e requeijão!')
        flavor_alho_oleo =  Flavor.objects.get_or_create(name='Alho e óleo', description='O melhor da junção de muçarela, alho e queijo parmesão!')
        flavor_camarao =  Flavor.objects.get_or_create(name='Camarão', description='Camarão fresco, molho de tomate, muçarela e catupiry.')
        flavor_bacon =  Flavor.objects.get_or_create(name='Bacon', description='Muçarela coberta com bacon e orégano.')
        flavor_california =  Flavor.objects.get_or_create(name='California', description='Muçarela, presunto, salada de frutas e orégano.')
        flavor_champignon =  Flavor.objects.get_or_create(name='Champignon', description='Queijo muçarela, cogumelos champignon e orégano.')
        flavor_napolitana =  Flavor.objects.get_or_create(name='Napolitana', description='É preparada com tomate, queijo, azeite de oliva, orégano e alho.')
        flavor_frango_catupiry =  Flavor.objects.get_or_create(name='Frango com catupiry', description='Queijo muçarela, frango, catupiry, sálvia e molho de tomate.')
        flavor_quatro_queijos =  Flavor.objects.get_or_create(name='Quatro queijos', description='Assim como o nome já diz, essa pizza é preparada com quatro queijos diferentes, como muçarela, gorgonzola, parmesão e catupiry.')
        flavor_marguerita =  Flavor.objects.get_or_create(name='Marguerita', description='É preparada com molho de tomate, manjericão, rodelas de tomate fresco, azeitona, queijo muçarela e orégano salpicado.')
        flavor_mucarela =  Flavor.objects.get_or_create(name='Muçarela', description='Esse sabor leva nada mais nada menos que o queijo muçarela em abundância, molho de tomate fresco, azeitona, rodelas de tomate e orégano!')
        flavor_portuguesa =  Flavor.objects.get_or_create(name='Portuguesa', description='Queijo, azeitona verde ou preta, ovo cozido, presunto cozido, cebola, ervilha, molho de tomate e azeite.')
        flavor_morango_chocolate =  Flavor.objects.get_or_create(name='Morango com chocolate', description='A combinação perfeita de morango e chocolate!')
        flavor_banofe =  Flavor.objects.get_or_create(name='Banofe', description='Banana, chocolate e castanhas. Uma verdadeira explosão de sabores!')
        flavor_romeu_julieta =  Flavor.objects.get_or_create(name='Romeu e Julieta', description='A combinação doce e salgada mais suculenta!')

        #pizza
        pizza_calabresa_gg = Pizza.objects.get_or_create(flavor=flavor_calabresa, size=size_gg, price=100)
        pizza_calabresa_g = Pizza.objects.get_or_create(flavor=flavor_calabresa, size=size_g, price=90)
        pizza_calabresa_m = Pizza.objects.get_or_create(flavor=flavor_calabresa, size=size_m, price=80)
        pizza_calabresa_p = Pizza.objects.get_or_create(flavor=flavor_calabresa, size=size_p, price=70)
        pizza_mexicana_gg = Pizza.objects.get_or_create(flavor=flavor_mexicana, size=size_gg, price=105)
        pizza_mexicana_g = Pizza.objects.get_or_create(flavor=flavor_mexicana, size=size_g, price=95)
        pizza_alho_oleo_g = Pizza.objects.get_or_create(flavor=flavor_alho_oleo, size=size_g, price=80)
        pizza_alho_oleo_m = Pizza.objects.get_or_create(flavor=flavor_alho_oleo, size=size_m, price=70)
        pizza_alho_oleo_p = Pizza.objects.get_or_create(flavor=flavor_alho_oleo, size=size_p, price=60)
        pizza_camarao_g = Pizza.objects.get_or_create(flavor=flavor_camarao, size=size_g, price=100)
        pizza_camarao_m = Pizza.objects.get_or_create(flavor=flavor_camarao, size=size_m, price=90)
        pizza_camarao_p = Pizza.objects.get_or_create(flavor=flavor_camarao, size=size_p, price=80)
        pizza_bacon_gg = Pizza.objects.get_or_create(flavor=flavor_bacon, size=size_gg, price=100)
        pizza_bacon_g = Pizza.objects.get_or_create(flavor=flavor_bacon, size=size_g, price=90)
        pizza_bacon_m = Pizza.objects.get_or_create(flavor=flavor_bacon, size=size_m, price=80)
        pizza_bacon_p = Pizza.objects.get_or_create(flavor=flavor_bacon, size=size_p, price=70)
        pizza_california_m = Pizza.objects.get_or_create(flavor=flavor_california, size=size_m, price=85)
        pizza_california_p = Pizza.objects.get_or_create(flavor=flavor_california, size=size_p, price=75)
        pizza_champignon_m = Pizza.objects.get_or_create(flavor=flavor_champignon, size=size_m, price=85)
        pizza_champignon_p = Pizza.objects.get_or_create(flavor=flavor_champignon, size=size_p, price=75)
        pizza_napolitana_g = Pizza.objects.get_or_create(flavor=flavor_napolitana, size=size_g, price=90)
        pizza_napolitana_m = Pizza.objects.get_or_create(flavor=flavor_napolitana, size=size_m, price=80)
        pizza_napolitana_p = Pizza.objects.get_or_create(flavor=flavor_napolitana, size=size_p, price=70)
        pizza_frango_catupiry_gg = Pizza.objects.get_or_create(flavor=flavor_frango_catupiry, size=size_gg, price=105)
        pizza_frango_catupiry_g = Pizza.objects.get_or_create(flavor=flavor_frango_catupiry, size=size_g, price=95)
        pizza_frango_catupiry_m = Pizza.objects.get_or_create(flavor=flavor_frango_catupiry, size=size_m, price=85)
        pizza_frango_catupiry_p = Pizza.objects.get_or_create(flavor=flavor_frango_catupiry, size=size_p, price=75)
        pizza_quatro_queijos_gg = Pizza.objects.get_or_create(flavor=flavor_quatro_queijos, size=size_gg, price=90)
        pizza_quatro_queijos_g = Pizza.objects.get_or_create(flavor=flavor_quatro_queijos, size=size_g, price=80)
        pizza_quatro_queijos_m = Pizza.objects.get_or_create(flavor=flavor_quatro_queijos, size=size_m, price=70)
        pizza_quatro_queijos_p = Pizza.objects.get_or_create(flavor=flavor_quatro_queijos, size=size_p, price=60)
        pizza_marguerita_g = Pizza.objects.get_or_create(flavor=flavor_marguerita, size=size_g, price=95)
        pizza_marguerita_m = Pizza.objects.get_or_create(flavor=flavor_marguerita, size=size_m, price=80)
        pizza_mucarela_g = Pizza.objects.get_or_create(flavor=flavor_mucarela, size=size_g, price=90)
        pizza_mucarela_m = Pizza.objects.get_or_create(flavor=flavor_mucarela, size=size_m, price=80)
        pizza_mucarela_p = Pizza.objects.get_or_create(flavor=flavor_mucarela, size=size_p, price=70)
        pizza_portuguesa_g = Pizza.objects.get_or_create(flavor=flavor_portuguesa, size=size_g, price=80)
        pizza_portuguesa_m = Pizza.objects.get_or_create(flavor=flavor_portuguesa, size=size_m, price=70)
        pizza_portuguesa_p = Pizza.objects.get_or_create(flavor=flavor_portuguesa, size=size_p, price=60)
        pizza_morango_chocolate_m = Pizza.objects.get_or_create(flavor=flavor_morango_chocolate, size=size_m, price=75)
        pizza_morango_chocolate_p = Pizza.objects.get_or_create(flavor=flavor_morango_chocolate, size=size_p, price=65)
        pizza_banofe_m = Pizza.objects.get_or_create(flavor=flavor_banofe, size=size_m, price=80)
        pizza_banofe_p = Pizza.objects.get_or_create(flavor=flavor_banofe, size=size_p, price=70)
        pizza_romeu_julieta_m = Pizza.objects.get_or_create(flavor=flavor_romeu_julieta, size=size_m, price=70)
        pizza_romeu_julieta_p = Pizza.objects.get_or_create(flavor=flavor_romeu_julieta, size=size_p, price=60)

        pedido1 = Order.objects.get_or_create(customer=_max).add_pizza(pizza_calabresa_gg)
        feedback1 = FeedBack.objects.get_or_create(rating=FeedBack.GREAT, description='Estava incrível!')
        pedido1.feedback = feedback1

        pedido2 = Order.objects.get_or_create(customer=joao).add_pizza(pizza_portuguesa_m)
        feedback2 = FeedBack.objects.get_or_create(rating=FeedBack.OK, description='Demorou mas chegou!')
        pedido2.feedback = feedback2

        pedido3 = Order.objects.get_or_create(customer=joao).add_pizza(pizza_marguerita_g)
        feedback3 = FeedBack.objects.get_or_create(rating=FeedBack.GOOD, description='Muito boaa!')
        pedido3.feedback = feedback3

        pedido4 = Order.objects.get_or_create(customer=max).add_pizza(pizza_quatro_queijos_gg)
        feedback4 = FeedBack.objects.get_or_create(rating=FeedBack.AWFUL, description='Muito óleo e pouco queijo!')
        pedido4.feedback = feedback4