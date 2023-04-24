import random
import datetime
from faker import Faker
from collections import OrderedDict

locales = OrderedDict([
    ('de_DE', 1)
])

fake = Faker(locales)
# de = faker.providers.date_time

####
# Menüs
##
bigmac_menu = [  # 8,99
    "1 Big Mac    MM",
    "  1 Big Mac",
    "  1 Pommes Frittes groß",
    "    1 Mayonnaise",
    "  1 Cola 0,5l"
]

shake_vanille_g_menu = [  # 3,99
    "1 Shake Vanille G",
    "  1 Ohne Zutat"
]

mcflurry_schoko_menu = [  # 3,79
    "1 McFlurry Schoko",
    "  2 Oreo",
    "  1 Schokolinsen"  # 0,40
]

mcsundae_original_menu = [  # 3,58
    "2 McSundae Original",
    "  2 Karamellsauce"
]

doppelpack_menu = [  # 9,99
    "1 App Coupon",
    "  1 Big Mac",
    "  1 Big Mac",
    "  1 Cola Zero 0,5l",
    "  1 Pommes Frites groß",
    "    1 Mayonnaise"
]

zwanziger_nuggets_menu = [  # 6,99
    "1 20er Ch.McNuggets",
    "  1 Süss-Sauer Sc.",
    "  1 Barbecue Sauce",
    "  1 Dip Sour Cream-Schnittlauch",
]
####
# Einzelne
##
chickenburger_single = [  # 1,50
    "1 Chickenburger"
]
snack_salad_classic_single = [  # 2,49
    "1 Snach Salad Classic",
    "  1 Ohne Dressing"
]

######
# Alle zusammen
###

az = [
    bigmac_menu,
    shake_vanille_g_menu,
    mcflurry_schoko_menu,
    mcsundae_original_menu,
    doppelpack_menu,
    zwanziger_nuggets_menu,
    chickenburger_single,
    snack_salad_classic_single
]

def die_rechnung_bitte():
    # kopf vorbereiten
    randORD = random.randint(1, 99)
    randKS = random.randint(4,32)
    randDTM = fake["de_DE"].date_between(start_date='-2d', end_date='today')
    datum = randDTM.strftime('%d-%m-%Y')
    randH = random.randint(10, 23)
    randM = random.randint(10, 59)
    randS = random.randint(10, 59)
    zeit = f"{randH}:{randM}:{randS}"

    # körper vorbereiten
    randANZANZ = random.randint(1,6)

    # füsse vorbereiten
    kartenzahlung = random.choice([True, False])
    hieressen = random.choice([True, False])



    # kopf+körper+füße generieren
    print("QUITTUNG")
    print(u'\u2500' * 40)
    print(f"#ORD {randORD} -KS  {randKS}     {datum} {zeit}")
    print("ANZ ARTIKEL                      GESAMT")

    for x in range(randANZANZ):
        randLIST = random.choice(az)
        for y, v in enumerate(randLIST):
            print(f"  {randLIST[y]}")

    if kartenzahlung:
        print()
        print("INNEN TOTAL")
        print("Kiosk Debit Cards")
    else:
        print()
        print("INNEN TOTAL")
        print("EUR")
        print("Rueckgeld")

    if hieressen:
        print()
        print("St.Nr./UStIDNr. 66/203/50600")
        print("              SATZ      BRUTTO      MWST")
        print("INCL. MWSt  19,00%       wx,yz     ab,cd")
        print("INCL. MWSt   7,00%       ef,gh     ij,kl")
        print(u'\u2500' * 40)
    else:
        print()
        print("St.Nr./UStIDNr. 66/203/50600")
        print("              SATZ      BRUTTO      MWST")
        print("INCL. MWSt   7,00%       ef,gh     ij,kl")
        print(u'\u2500' * 40)


die_rechnung_bitte()
