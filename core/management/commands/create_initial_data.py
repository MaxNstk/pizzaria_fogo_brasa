from turtle import circle
from django.core.management import BaseCommand
from core.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        try:
            zeca = User.objects.create_user(username='zeca',password='zeca123',first_name='Zeca',last_name='Baleiro',
            email='zeca@pizzariafogobrasa.com', phone_number='99999-9992', cpf_cnpj='000.000.000-39')

            cris = User.objects.create_user(username='cris',password='cr7777',first_name='Cristiano',last_name='Ronaldo',
            email='cr7@pizzariafogobrasa.com', phone_number='99999-3992', cpf_cnpj='000.000.004-39')

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
            zeca = User.objects.get(username='zeca')
            cris = User.objects.get(username='cris')
        
        endereco1, created = Address.objects.get_or_create(customer=joao, address='Rua dos bobs', number='0', district='niterói', zip_code='89150000')
        endereco2, created = Address.objects.get_or_create(customer=zeca, address='Av missler', number='323', district='dalbérgia', zip_code='89150000')
        endereco3, created = Address.objects.get_or_create(customer=cris, address='Manchester', number='231', district='mojevi', zip_code='89150342')

        #size
        size_gg, created = Size.objects.get_or_create(short_name='GG', description='Gigante')
        size_g, created = Size.objects.get_or_create(short_name='G', description='Grande')
        size_m, created = Size.objects.get_or_create(short_name='M', description='Média')
        size_p, created = Size.objects.get_or_create(short_name='P', description='Pequena')


        #flavor
        flavor_calabresa, created =  Flavor.objects.get_or_create(name='Calabresa', description='Molho de tomate, queijo mussalera e muita calabresa!')
        flavor_mexicana, created =  Flavor.objects.get_or_create(name='Mexicana', description='Carne moída apimentada e uma mistura de queijos cheddar, muçarela e requeijão!')
        flavor_alho_oleo, created =  Flavor.objects.get_or_create(name='Alho e óleo', description='O melhor da junção de muçarela, alho e queijo parmesão!')
        flavor_camarao, created =  Flavor.objects.get_or_create(name='Camarão', description='Camarão fresco, molho de tomate, muçarela e catupiry.')
        flavor_bacon, created =  Flavor.objects.get_or_create(name='Bacon', description='Muçarela coberta com bacon e orégano.')
        flavor_california, created =  Flavor.objects.get_or_create(name='California', description='Muçarela, presunto, salada de frutas e orégano.')
        flavor_champignon, created =  Flavor.objects.get_or_create(name='Champignon', description='Queijo muçarela, cogumelos champignon e orégano.')
        flavor_napolitana, created =  Flavor.objects.get_or_create(name='Napolitana', description='É preparada com tomate, queijo, azeite de oliva, orégano e alho.')
        flavor_frango_catupiry, created =  Flavor.objects.get_or_create(name='Frango com catupiry', description='Queijo muçarela, frango, catupiry, sálvia e molho de tomate.')
        flavor_quatro_queijos, created =  Flavor.objects.get_or_create(name='Quatro queijos', description='Assim como o nome já diz, essa pizza é preparada com quatro queijos diferentes, como muçarela, gorgonzola, parmesão e catupiry.')
        flavor_marguerita, created =  Flavor.objects.get_or_create(name='Marguerita', description='É preparada com molho de tomate, manjericão, rodelas de tomate fresco, azeitona, queijo muçarela e orégano salpicado.')
        flavor_mucarela, created =  Flavor.objects.get_or_create(name='Muçarela', description='Esse sabor leva nada mais nada menos que o queijo muçarela em abundância, molho de tomate fresco, azeitona, rodelas de tomate e orégano!')
        flavor_portuguesa, created =  Flavor.objects.get_or_create(name='Portuguesa', description='Queijo, azeitona verde ou preta, ovo cozido, presunto cozido, cebola, ervilha, molho de tomate e azeite.')
        flavor_morango_chocolate, created =  Flavor.objects.get_or_create(name='Morango com chocolate', description='A combinação perfeita de morango e chocolate!')
        flavor_banofe, created =  Flavor.objects.get_or_create(name='Banofe', description='Banana, chocolate e castanhas. Uma verdadeira explosão de sabores!')
        flavor_romeu_julieta, created =  Flavor.objects.get_or_create(name='Romeu e Julieta', description='A combinação doce e salgada mais suculenta!')

        #pizza
        pizza_calabresa_gg, created = Pizza.objects.get_or_create(flavor=flavor_calabresa, size=size_gg, price=100)
        pizza_calabresa_g, created = Pizza.objects.get_or_create(flavor=flavor_calabresa, size=size_g, price=90)
        pizza_calabresa_m, created = Pizza.objects.get_or_create(flavor=flavor_calabresa, size=size_m, price=80)
        pizza_calabresa_p, created = Pizza.objects.get_or_create(flavor=flavor_calabresa, size=size_p, price=70)
        pizza_mexicana_gg, created = Pizza.objects.get_or_create(flavor=flavor_mexicana, size=size_gg, price=105)
        pizza_mexicana_g, created = Pizza.objects.get_or_create(flavor=flavor_mexicana, size=size_g, price=95)
        pizza_alho_oleo_g, created = Pizza.objects.get_or_create(flavor=flavor_alho_oleo, size=size_g, price=80)
        pizza_alho_oleo_m, created = Pizza.objects.get_or_create(flavor=flavor_alho_oleo, size=size_m, price=70)
        pizza_alho_oleo_p, created = Pizza.objects.get_or_create(flavor=flavor_alho_oleo, size=size_p, price=60)
        pizza_camarao_g, created = Pizza.objects.get_or_create(flavor=flavor_camarao, size=size_g, price=100)
        pizza_camarao_m, created = Pizza.objects.get_or_create(flavor=flavor_camarao, size=size_m, price=90)
        pizza_camarao_p, created = Pizza.objects.get_or_create(flavor=flavor_camarao, size=size_p, price=80)
        pizza_bacon_gg, created = Pizza.objects.get_or_create(flavor=flavor_bacon, size=size_gg, price=100)
        pizza_bacon_g, created = Pizza.objects.get_or_create(flavor=flavor_bacon, size=size_g, price=90)
        pizza_bacon_m, created = Pizza.objects.get_or_create(flavor=flavor_bacon, size=size_m, price=80)
        pizza_bacon_p, created = Pizza.objects.get_or_create(flavor=flavor_bacon, size=size_p, price=70)
        pizza_california_m, created = Pizza.objects.get_or_create(flavor=flavor_california, size=size_m, price=85)
        pizza_california_p, created = Pizza.objects.get_or_create(flavor=flavor_california, size=size_p, price=75)
        pizza_champignon_m, created = Pizza.objects.get_or_create(flavor=flavor_champignon, size=size_m, price=85)
        pizza_champignon_p, created = Pizza.objects.get_or_create(flavor=flavor_champignon, size=size_p, price=75)
        pizza_napolitana_g, created = Pizza.objects.get_or_create(flavor=flavor_napolitana, size=size_g, price=90)
        pizza_napolitana_m, created = Pizza.objects.get_or_create(flavor=flavor_napolitana, size=size_m, price=80)
        pizza_napolitana_p, created = Pizza.objects.get_or_create(flavor=flavor_napolitana, size=size_p, price=70)
        pizza_frango_catupiry_gg, created = Pizza.objects.get_or_create(flavor=flavor_frango_catupiry, size=size_gg, price=105)
        pizza_frango_catupiry_g, created = Pizza.objects.get_or_create(flavor=flavor_frango_catupiry, size=size_g, price=95)
        pizza_frango_catupiry_m, created = Pizza.objects.get_or_create(flavor=flavor_frango_catupiry, size=size_m, price=85)
        pizza_frango_catupiry_p, created = Pizza.objects.get_or_create(flavor=flavor_frango_catupiry, size=size_p, price=75)
        pizza_quatro_queijos_gg, created = Pizza.objects.get_or_create(flavor=flavor_quatro_queijos, size=size_gg, price=90)
        pizza_quatro_queijos_g, created = Pizza.objects.get_or_create(flavor=flavor_quatro_queijos, size=size_g, price=80)
        pizza_quatro_queijos_m, created = Pizza.objects.get_or_create(flavor=flavor_quatro_queijos, size=size_m, price=70)
        pizza_quatro_queijos_p, created = Pizza.objects.get_or_create(flavor=flavor_quatro_queijos, size=size_p, price=60)
        pizza_marguerita_g, created = Pizza.objects.get_or_create(flavor=flavor_marguerita, size=size_g, price=95)
        pizza_marguerita_m, created = Pizza.objects.get_or_create(flavor=flavor_marguerita, size=size_m, price=80)
        pizza_mucarela_g, created = Pizza.objects.get_or_create(flavor=flavor_mucarela, size=size_g, price=90)
        pizza_mucarela_m, created = Pizza.objects.get_or_create(flavor=flavor_mucarela, size=size_m, price=80)
        pizza_mucarela_p, created = Pizza.objects.get_or_create(flavor=flavor_mucarela, size=size_p, price=70)
        pizza_portuguesa_g, created = Pizza.objects.get_or_create(flavor=flavor_portuguesa, size=size_g, price=80)
        pizza_portuguesa_m, created = Pizza.objects.get_or_create(flavor=flavor_portuguesa, size=size_m, price=70)
        pizza_portuguesa_p, created = Pizza.objects.get_or_create(flavor=flavor_portuguesa, size=size_p, price=60)
        pizza_morango_chocolate_m, created = Pizza.objects.get_or_create(flavor=flavor_morango_chocolate, size=size_m, price=75)
        pizza_morango_chocolate_p, created = Pizza.objects.get_or_create(flavor=flavor_morango_chocolate, size=size_p, price=65)
        pizza_banofe_m, created = Pizza.objects.get_or_create(flavor=flavor_banofe, size=size_m, price=80)
        pizza_banofe_p, created = Pizza.objects.get_or_create(flavor=flavor_banofe, size=size_p, price=70)
        pizza_romeu_julieta_m, created = Pizza.objects.get_or_create(flavor=flavor_romeu_julieta, size=size_m, price=70)
        pizza_romeu_julieta_p, created = Pizza.objects.get_or_create(flavor=flavor_romeu_julieta, size=size_p, price=60)

        coca_2l, created = Product.objects.get_or_create(description='Coca-Cola 2 Litros', price=12)
        guarana_600ml = Product.objects.get_or_create(description='Guarana 600 ml', price=5)
        cigarro_malboro  = Product.objects.get_or_create(description='Cicarro malboro', price=10)
        hals_menta  = Product.objects.get_or_create(description='Hals de mentas', price=3)
        picole_chocolate  = Product.objects.get_or_create(description='Picolé de Chocolate Lewa', price=6)
        trident_hortela  = Product.objects.get_or_create(description='Trident de Hortelã', price=3.50)
        tictac_canela  = Product.objects.get_or_create(description='TicTac de Canela', price=2.75)
        

        pedido1, created = Order.objects.get_or_create(customer=_max, observation='Capricha ai chefe!',
        situation=Order.FINISHED)
        pedido1.pizzas.add(pizza_calabresa_gg)
        pedido1.pizzas.add(pizza_morango_chocolate_m)
        pedido1.pizzas.add(pizza_frango_catupiry_gg)
        pedido1.products.add(coca_2l)
        pedido1.products.add(tictac_canela)

        feedback1, created = FeedBack.objects.get_or_create(rating=FeedBack.GREAT, description='Estava incrível!')
        pedido1.feedback = feedback1

        pedido2, created = Order.objects.get_or_create(customer=joao)
        pedido2.pizzas.add(pizza_portuguesa_m)
        pedido2.pizzas.add(pizza_bacon_p)
        pedido2.pizzas.add(pizza_napolitana_g)
        pedido2.pizzas.add(pizza_portuguesa_m)

        pedido2.products.add(picole_chocolate)
        pedido2.products.add(guarana_600ml)
        pedido2.products.add(guarana_600ml)

        feedback2, created = FeedBack.objects.get_or_create(rating=FeedBack.OK, description='Demorou mas chegou!')
        pedido2.feedback = feedback2

        pedido3, created = Order.objects.get_or_create(customer=zeca)
        pedido3.pizzas.add(pizza_marguerita_g)
        pedido3.pizzas.add(pizza_romeu_julieta_m)
        pedido3.pizzas.add(pizza_morango_chocolate_p)
        pedido3.pizzas.add(pizza_mucarela_m)
        pedido3.products.add(trident_hortela)
        
        feedback3, created = FeedBack.objects.get_or_create(rating=FeedBack.GOOD, description='Muito boaa!')
        pedido3.feedback = feedback3

        pedido4, created = Order.objects.get_or_create(customer=cris)
        pedido4.pizza.add(pizza_quatro_queijos_g)
        pedido4.pizza.add(pizza_quatro_queijos_gg)
        pedido4.pizza.add(pizza_quatro_queijos_m)
        pedido4.pizza.add(pizza_quatro_queijos_p)

        pedido4.products.add(cigarro_malboro)
        pedido4.products.add(cigarro_malboro)

        feedback4, created = FeedBack.objects.get_or_create(rating=FeedBack.AWFUL, description='Muito óleo e pouco queijo!')
        pedido4.feedback = feedback4