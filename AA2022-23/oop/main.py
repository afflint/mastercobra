from vans import FoodVan, RaceCar, Camper, Batteria
from clienti import Cliente

# creo le istanze di tipo FoodVan
donut_van = FoodVan("Donut Van", "17 x 12 x 12", "legno", 18)
gelati_van = FoodVan("Ice Cream Van", "17 x 14 x 12", "legno", 20)

# creo l'istanza di tipo Cliente
marco = Cliente("mark00", 1234)

# aggiungo l'istanza di tipo FoodVan al carrello di Marco
for i in range(10):
    gelati_van.add_to_cart(marco)
donut_van.add_to_cart(marco)
donut_van.add_to_cart(marco)
print(f"Carrello di Marco: {marco.cart}")

# creo l'istanza di tipo Batteria
batteria = Batteria("Gecoty", "6V")

# ricarico la Batteria
batteria.recharge()

# creo l'istanza di tipo RaceCar
black_jack = RaceCar("BlackJack 21", "16 x 10 x 10", "legno", "28", batteria)
print(black_jack.modello)

# creo l'istanza di tipo Camper
camper_arizona = Camper("Camper", "20 x 15 x15", "legno", 20)
print("Prezzo iniziale:", camper_arizona.prezzo)

# uso il metodo dell'istanza per cambiare il suo prezzo
camper_arizona.applica_sconto(.5)
print("Prezzo finale:", camper_arizona.prezzo)

