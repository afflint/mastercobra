from collections import defaultdict

class Batteria():
    # descrizione: attributi e metodi

    def __init__(self, marchio, voltaggio):
        self.marchio = marchio
        self.voltaggio = voltaggio
        self.carica = False

    def recharge(self):
        print("Ora la batteria è carica!")
        self.carica = True


class Vehicle():
    def __init__(self, modello, dimensione, materiale, prezzo):
        self.stock_iniziale = 10
        self.modello = modello
        self.dimensione = dimensione
        self.materiale = materiale
        self.prezzo = prezzo

    def add_to_cart(self, cliente):

        if self.stock_iniziale > 0:

            # aggiunta al carrello del cliente
            if self.modello in cliente.cart:
                cliente.cart[self.modello] += 1
            else:
                cliente.cart[self.modello] = 1

            # riduzione dello stock di un'unità
            self.stock_iniziale -= 1

        else:
            print("Articolo esaurito!")


# DRY Rule: Don't repeat yourself!
class FoodVan(Vehicle):
    pass


class RaceCar(Vehicle):
    def __init__(self, modello, dimensione, materiale, prezzo, batteria):
        self.batteria = batteria
        # la funzione super() chiama il metodo __init__ della classe madre
        super().__init__(modello, dimensione, materiale, prezzo)


class Camper(Vehicle):
    def applica_sconto(self, percentuale):
        self.prezzo = self.prezzo * (1-percentuale)


