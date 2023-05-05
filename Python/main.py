class Produit:
    """ Classe Produit : produit de l'inventaire représenté par un nom, une description, un prix et une quantité en
    stock"""

    global liste_produits
    liste_produits = []

    def __init__(self, nom: str, description: str, prix: float, quantity: int):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.quantity = quantity
        liste_produits.append(self)

    def __str__(self):
        return f"Produit : {self.nom} - Description : {self.description} - Prix : {self.prix} € - Quantité : " \
               f"{self.quantity}"

    def __repr__(self):
        return f"Produit : {self.nom} - Description : {self.description} - Prix : {self.prix} € - Quantité : " \
               f"{self.quantity}"

    def exists(self, nom):
        if nom in liste_produits:
            return True


class Inventaire:
    def __init__(self):
        self.stock = {}

    def stocker(self, produit: Produit):
        self.stock[produit.nom] = produit.quantity

    def ajouter_stock(self, produit: Produit, quantity):
        self.stock[produit.nom] += quantity

    def retirer_stock(self, produit: Produit, quantity):
        self.stock[produit.nom] -= quantity

    def __str__(self):
        return f"Inventaire : {self.stock}"

    def __repr__(self):
        return f"Inventaire : {self.stock}"


class Commande:
    def __init__(self, identification_number: int):
        self.identification_number = identification_number
        self.dico_produits = {}
        self.statut = "En attente"

    def __str__(self):
        return f"Commande : N°{self.identification_number} - Produits: {self.dico_produits} - Statut : {self.statut}"

    def ajouter_produit(self, inventaire: Inventaire, produit: Produit, quantity: int):
        if produit.nom not in inventaire.stock:
            raise ValueError("Le produit n'est pas dans la commande")
        if quantity <= 0:
            raise ValueError("La quantité doit être supérieure à 0")
        if produit.quantity == 0:
            raise ValueError("Le produit n'est plus en stock")
        if quantity > produit.quantity:
            raise ValueError("La quantité demandée est supérieure à la quantité en stock")
        self.dico_produits[produit.nom] = quantity
        inventaire.retirer_stock(produit, quantity)

    def retirer_produit(self, inventaire: Inventaire, produit: Produit, quantity: int):
        if quantity > self.dico_produits[produit.nom]:
            raise ValueError("La quantité demandée est supérieure à la quantité en stock")
        if quantity == self.dico_produits[produit.nom]:
            self.dico_produits.pop(produit.nom)
        else:
            self.dico_produits[produit.nom] -= quantity
        inventaire.ajouter_stock(produit, quantity)

    def change_status(self, id_status: int):
        if id_status == 1:
            self.statut = "En attente"
        elif id_status == 2:
            self.statut = "Pris en charge"
        elif id_status == 3:
            self.statut = "Expédiée"
        elif id_status == 4:
            self.statut = "Livrée"
        else:
            raise ValueError("Statut invalide")

    def show_status(self):
        return f"Statut de la commande N°{self.identification_number} : {self.statut}"

    def show_products(self):
        return f"Produits de la commande N°{self.identification_number} : {self.dico_produits}"

    def show_id(self):
        return f"Numéro d'identification de la commande : {self.identification_number}"

    def get_price(self):
        total_price = 0
        for produit, quantity in self.dico_produits.items():
            produit_prix = 0
            for p in liste_produits:
                if produit == p.nom:
                    produit_prix = p.prix
            total_price += (produit_prix * quantity)
        return total_price

    def __repr__(self):
        return f"Commande : N°{self.identification_number} - Produits: {self.dico_produits} - Statut : {self.statut}"


class Delivery:
    def __init__(self, id_company: int, name_company: str):
        self.id_company = id_company
        self.name_company = name_company
        self.liste_commandes = []

    def ajouter_commande(self, commande: Commande, paid: bool = True):
        if commande in self.liste_commandes:
            raise ValueError("La commande est déjà dans la liste de commandes de la société")
        if commande.statut != "En attente":
            raise ValueError("La commande n'est pas en attente")
        if not paid:
            raise ValueError("La commande n'est pas payée")
        self.liste_commandes.append(commande)

    def retirer_commande(self, commande: Commande):
        if commande not in self.liste_commandes:
            raise ValueError("La commande n'est pas dans la liste de commandes de la société")
        if commande.statut != "En attente":
            raise ValueError("La commande n'est pas en attente")
        self.liste_commandes.remove(commande)

    def show_commandes(self):
        return f"Commandes de la société {self.name_company} : {self.liste_commandes}"

    def show_id(self):
        return f"Numéro d'identification de la société : {self.id_company}"

    def show_name(self):
        return f"Nom de la société : {self.name_company}"

    def livraison(self, commande: Commande):
        if commande not in self.liste_commandes:
            raise ValueError("La commande n'est pas dans la liste de commandes de la société")
        commande.change_status(3)

    def command_received(self, commande: Commande, check: bool):
        if commande not in self.liste_commandes:
            raise ValueError("La commande n'est pas dans la liste de commandes de la société")
        commande.change_status(4) if check else commande.change_status(3)

    def __str__(self):
        return f"ID de Société: {self.id_company} - Société de livraison : {self.name_company} - Commandes : " \
               f"{self.liste_commandes}"

    def __repr__(self):
        return f"ID de Société: {self.id_company} - Société de livraison : {self.name_company} - Commandes : " \
               f"{self.liste_commandes}"


class Client:
    def __init__(self, id: int, nom: str, prenom: str, adresse: str, email: str, argent: float):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.email = email
        self.panier = []
        self.argent = argent
        self.received_commands = []

    def __str__(self):
        return f"Client : {self.id} - Nom : {self.nom} - Prénom : {self.prenom} - Adresse : {self.adresse} - Email : {self.email}"

    def __repr__(self):
        return f"Client : {self.id} - Nom : {self.nom} - Prénom : {self.prenom} - Adresse : {self.adresse} - Email : {self.email}"

    def commander(self, commande):
        self.panier.append(commande)

    def show_panier(self):
        return f"Panier du client {self.nom} : {self.panier}"

    def payer(self, commande):
        total_price = commande.get_price()
        if self.argent < total_price:
            print("Vous n'avez pas assez d'argent pour payer cette commande")
            return False
        self.argent -= total_price
        print(f"{self.nom} a payé {total_price} €")
        return True

    def ajouter_argent(self, argent: float):
        self.argent += argent
        print(f"Vous avez ajouté {argent} € à votre compte")

    def received(self, commande: Commande, check: bool):
        if commande not in self.panier:
            raise ValueError("La commande n'est pas dans le panier du client")
        if check:
            self.received_commands.append(commande)
            self.panier.remove(commande)
            print(f"La commande {commande.identification_number} a bien été reçue")
        return check


########################################################################################################################
# Tests (instanciation des classes)

# Produits

p001 = Produit("Pomme", "Fruit rouge", 1.5, 10)
p002 = Produit("Poire", "Fruit jaune", 2, 5)
p003 = Produit("Banane", "Fruit jaune", 1, 10)
p004 = Produit("Orange", "Fruit orange", 1.5, 0)

# Inventaire

inventaire1 = Inventaire()

# Commandes

c001 = Commande(1)
c002 = Commande(2)
c003 = Commande(3)

# Livraison

soc1 = Delivery(1, "Transport Express")
soc2 = Delivery(2, "D-Expert")

########################################################################################################################
# Tests (affichage des informations)

# Produits

print(p001.nom)
print(p001.description)
print(p001.prix)
print(p001.quantity)

print(p002)
print(p003)
print(p004)

# Inventaire

print(inventaire1)
print(inventaire1.stock)

# Commandes

print(c001)
print(c002)
print(c003)

# Livraison

print(soc1)
print(soc2)

########################################################################################################################
# Tests (ajout de produits dans l'inventaire)

inventaire1.stocker(p001)
inventaire1.stocker(p002)
inventaire1.stocker(p003)
inventaire1.stocker(p004)

print(inventaire1.stock)

########################################################################################################################

# Tests (ajout de produits dans la commande)

c001.ajouter_produit(inventaire1, p001, 2)
c001.ajouter_produit(inventaire1, p002, 5)
c002.ajouter_produit(inventaire1, p003, 9)
c003.ajouter_produit(inventaire1, p001, 6)

print(c001)
print(inventaire1.stock)
print(c001.show_products())
print(c001.show_status())
print(c001.show_id())
print(c001.get_price())

print(c002)
print(inventaire1.stock)
print(c002.show_products())
print(c002.show_status())
print(c002.show_id())
print(c002.get_price())

print(c003.get_price())
# Livraison des commandes
print(inventaire1.stock)

soc1.ajouter_commande(c001)
soc1.ajouter_commande(c003)
soc2.ajouter_commande(c002)

print(c001.show_status())
print(c002.show_status())

print(soc1.show_commandes())
print(soc2.show_commandes())
soc1.livraison(c001)
soc2.livraison(c002)

print(c001.show_status())
print(c002.show_status())
print(soc1.show_commandes())
print(soc2.show_commandes())

soc1.command_received(c001, True)
soc2.command_received(c002, False)

print(c001.show_status())
print(c002.show_status())

print(soc1.show_commandes())
soc2.command_received(c002, True)
print(soc2.show_commandes())
print(c002.show_status())

########################################################################################################################
# Tests (avec clients)

client1 = Client(1, "Dupont", "Jean", "1 rue de la Paix 75012 Paris", "dupont@xyz.com", 50)
client2 = Client(2, "Durand", "Pierre", "2 rue de la Paix 93210 Saint-Denis", "durant@xyz.fr", 15)
client3 = Client(3, "Marie", "Jeanne", "420 rue de la Joie 75016 Paris", "martin@xyz.com", 100)

p005 = Produit("Fruit du dragon", "Fruit rose", 6, 15)
p006 = Produit("Fruit de la passion", "Fruit jaune", 4, 25)
p007 = Produit("Mangue", "Fruit exotique", 3, 15)
p008 = Produit("Goyave", "Fruit très exotique", 6, 20)

inventaire2 = Inventaire()
inventaire2.stocker(p005)
inventaire2.stocker(p006)
inventaire2.stocker(p007)
inventaire2.stocker(p008)

print(inventaire2)
# Ajout de produits dans le panier
cmd4 = Commande(4)
cmd5 = Commande(5)
cmd6 = Commande(6)

cmd4.ajouter_produit(inventaire2, p005, 4)
cmd4.ajouter_produit(inventaire2, p006, 6)

cmd5.ajouter_produit(inventaire2, p007, 5)
cmd6.ajouter_produit(inventaire2, p008, 10)
cmd6.ajouter_produit(inventaire2, p005, 4)

print(cmd4)
print(cmd5)
print(cmd6)

client1.commander(cmd4)
client2.commander(cmd5)
client3.commander(cmd6)

print(client1.show_panier())
print(client2.show_panier())
print(client3.show_panier())

print(cmd4.get_price())
print(cmd5.get_price())
print(cmd6.get_price())

# Paiement des commandes

soc2.ajouter_commande(cmd4, client1.payer(cmd4))
soc2.ajouter_commande(cmd5, client2.payer(cmd5))
soc1.ajouter_commande(cmd6, client3.payer(cmd6))

# Affichage des commandes
print(soc1.show_commandes())
print(soc2.show_commandes())

# Livraison des commandes
soc1.livraison(cmd6)
soc2.livraison(cmd4)
soc2.livraison(cmd5)

# Affichage des commandes
print(soc1.show_commandes())
print(soc2.show_commandes())

# Reception des commandes
soc1.command_received(cmd6, client1.received(cmd4, True))
soc2.command_received(cmd4, client2.received(cmd5, True))
soc2.command_received(cmd5, client3.received(cmd6, False))

print(soc1.show_commandes())
print(soc2.show_commandes())

soc2.command_received(cmd5, client3.received(cmd6, True))
print(soc2.show_commandes())

########################################################################################################################

print(c001)
print(c002)
print(c003)
print(cmd4)
print(cmd5)
print(cmd6)

print(client1.show_panier())
print(client2.show_panier())
print(client3.show_panier())
print(client1.received_commands)
print(client2.received_commands)
print(client3.received_commands)
########################################################################################################################

# Gestion des exceptions
# c002.ajouter_produit(inventaire1, p003, 20)
# c002.ajouter_produit(inventaire1, p004, 10)
# c002.ajouter_produit(inventaire1, p999, 10)
# c002.ajouter_produit(inventaire1, p001, 0)
