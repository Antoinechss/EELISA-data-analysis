COUNTRY_CODE_TO_NAME = {
    "be": "Belgium",
    "bg": "Bulgaria",
    "cz": "Czechia",
    "dk": "Denmark",
    "de": "Germany",
    "ee": "Estonia",
    "ie": "Ireland",
    "el": "Greece",
    "gr": "Greece",
    "es": "Spain",
    "fr": "France",
    "hr": "Croatia",
    "it": "Italy",
    "cy": "Cyprus",
    "lv": "Latvia",
    "lt": "Lithuania",
    "lu": "Luxembourg",
    "hu": "Hungary",
    "mt": "Malta",
    "nl": "Netherlands",
    "at": "Austria",
    "pl": "Poland",
    "pt": "Portugal",
    "ro": "Romania",
    "si": "Slovenia",
    "sk": "Slovakia",
    "fi": "Finland",
    "se": "Sweden",
    "no": "Norway",
    "ch": "Switzerland",
}

# NUTS1 and NUTS2 tokens-area classification

NUTS_REGIONS = {
    # AUSTRIA (AT) 
    "AT1": "Eastern Austria",
    "AT2": "Southern Austria",
    "AT3": "Western Austria",
    "AT11": "Burgenland",
    "AT12": "Lower Austria",
    "AT13": "Vienna",
    "AT21": "Carinthia",
    "AT22": "Styria",
    "AT31": "Upper Austria",
    "AT32": "Salzburg",
    "AT33": "Tyrol",
    "AT34": "Vorarlberg",

    # BELGIUM (BE) 
    "BE1": "Brussels-Capital",
    "BE2": "Flanders",
    "BE3": "Wallonia",

    # BULGARIA (BG)
    "BG3": "Northern and Eastern Bulgaria",
    "BG4": "South-Western and South-Central Bulgaria",
    "BG31": "North-West",
    "BG32": "North-Central",
    "BG33": "North-East",
    "BG34": "South-East",
    "BG41": "South-West",
    "BG42": "South-Central",

    # SWITZERLAND (CH) 
    "CH0": "Switzerland",
    "CH01": "Northwestern Switzerland",
    "CH02": "Eastern Switzerland",
    "CH03": "Central Switzerland",
    "CH04": "Zürich",
    "CH05": "Lake Geneva Region",
    "CH06": "Midland Switzerland",
    "CH07": "Ticino",

    # CYPRUS (CY)
    "CY0": "Cyprus",
    "CY00": "Cyprus (entire island)",

    # CZECHIA (CZ)
    "CZ0": "Czech Republic",
    "CZ01": "Prague",
    "CZ02": "Central Bohemia",
    "CZ03": "Southwest",
    "CZ04": "Northwest",
    "CZ05": "Northeast",
    "CZ06": "Southeast",
    "CZ07": "Central Moravia",
    "CZ08": "Moravia-Silesia",

    # DENMARK (DK)
    "DK0": "Denmark",
    "DK01": "Capital Region",
    "DK02": "Zealand",
    "DK03": "Southern Denmark",
    "DK04": "Central Jutland",
    "DK05": "North Jutland",

    # GERMANY (DE)
    "DE1": "Baden-Württemberg",
    "DE2": "Bavaria",
    "DE3": "Berlin",
    "DE4": "Brandenburg",
    "DE5": "Bremen",
    "DE6": "Hamburg",
    "DE7": "Hesse",
    "DE8": "Mecklenburg-Vorpommern",
    "DE9": "Lower Saxony",
    "DEA": "North Rhine-Westphalia",
    "DEB": "Rhineland-Palatinate",
    "DEC": "Saarland",
    "DED": "Saxony",
    "DEE": "Saxony-Anhalt",
    "DEF": "Thuringia",
    "DEG": "Schleswig-Holstein",
    "DE11": "Stuttgart",
    "DE12": "Karlsruhe",
    "DE13": "Freiburg",
    "DE14": "Tübingen",
    "DE21": "Upper Bavaria",
    "DE22": "Lower Bavaria",
    "DE23": "Upper Palatinate",
    "DE24": "Upper Franconia",
    "DE25": "Middle Franconia",
    "DE26": "Lower Franconia",
    "DE27": "Swabia",
    "DE30": "Berlin",
    "DE40": "Brandenburg",
    "DE50": "Bremen",
    "DE60": "Hamburg",
    "DE71": "Darmstadt",
    "DE72": "Gießen",
    "DE73": "Kassel",
    "DE80": "Mecklenburg-Vorpommern",
    "DE91": "Braunschweig",
    "DE92": "Hanover",
    "DE93": "Lüneburg",
    "DE94": "Weser-Ems",
    "DEA1": "Düsseldorf",
    "DEA2": "Cologne",
    "DEA3": "Münster",
    "DEA4": "Detmold",
    "DEA5": "Arnsberg",
    "DEB1": "Koblenz",
    "DEB2": "Trier",
    "DEB3": "Rheinhessen-Pfalz",
    "DEC0": "Saarland",
    "DED2": "Dresden",
    "DED4": "Chemnitz",
    "DED5": "Leipzig",
    "DEE0": "Saxony-Anhalt",
    "DEF0": "Thuringia",
    "DEG0": "Schleswig-Holstein",

    # ESTONIA (EE)
    "EE0": "Estonia",
    "EE00": "Estonia",

    # SPAIN (ES)
    "ES1": "North-West",
    "ES2": "North-East",
    "ES3": "Madrid",
    "ES4": "Centre",
    "ES5": "East",
    "ES6": "South",
    "ES7": "Canary Islands",
    "ES11": "Galicia",
    "ES12": "Asturias",
    "ES13": "Cantabria",
    "ES21": "Basque Country",
    "ES22": "Navarra",
    "ES23": "La Rioja",
    "ES24": "Aragon",
    "ES30": "Madrid",
    "ES41": "Castilla y León",
    "ES42": "Castilla-La Mancha",
    "ES43": "Extremadura",
    "ES51": "Catalonia",
    "ES52": "Valencian Community",
    "ES53": "Balearic Islands",
    "ES61": "Andalusia",
    "ES62": "Murcia",
    "ES63": "Ceuta",
    "ES64": "Melilla",
    "ES70": "Canary Islands",

    # FINLAND (FI)
    "FI1": "Mainland Finland",
    "FI2": "Åland",
    "FI19": "Southern Finland",
    "FI1C": "Western Finland",
    "FI1D": "Northern & Eastern Finland",
    "FI20": "Åland",

    # FRANCE (FR)
    "FR1": "Île-de-France",
    "FR2": "Centre-Val de Loire",
    "FR3": "Bourgogne-Franche-Comté",
    "FR4": "Normandy",
    "FR5": "Hauts-de-France",
    "FR6": "Grand Est",
    "FR7": "Pays de la Loire",
    "FR8": "Brittany",
    "FR9": "Nouvelle-Aquitaine",
    "FRA": "Guadeloupe",
    "FRB": "Martinique",
    "FRC": "Guyane",
    "FRD": "La Réunion",
    "FRE": "Mayotte",
    "FRF": "Grand Est",
    "FRG": "Nouvelle-Aquitaine",
    "FRH": "Occitanie",
    "FRI": "Auvergne-Rhône-Alpes",
    "FRJ": "Île-de-France",
    "FRK": "Bourgogne-Franche-Comté",
    "FRL": "Provence-Alpes-Côte d'Azur",
    "FRM": "Corse",
    "FRY": "French Overseas Territories",

    # GREECE (EL)
    "EL3": "Attica",
    "EL4": "Aegean Islands-Crete",
    "EL5": "Northern Greece",
    "EL6": "Central Greece",
    "EL30": "Attica",
    "EL41": "North Aegean",
    "EL42": "South Aegean",
    "EL43": "Crete",
    "EL51": "Eastern Macedonia and Thrace",
    "EL52": "Central Macedonia",
    "EL53": "Western Macedonia",
    "EL54": "Epirus",
    "EL55": "Thessaly",
    "EL61": "Ionian Islands",
    "EL62": "Western Greece",
    "EL63": "Central Greece",
    "EL64": "Peloponnese",

    # CROATIA (HR)
    "HR0": "Croatia",
    "HR02": "Panonia",
    "HR03": "Adriatic Croatia",
    "HR06": "Continental Croatia",

    # HUNGARY (HU)
    "HU1": "Central Hungary",
    "HU2": "Transdanubia",
    "HU3": "Great Plain and North",
    "HU11": "Budapest",
    "HU12": "Pest",
    "HU21": "Central Transdanubia",
    "HU22": "Western Transdanubia",
    "HU23": "Southern Transdanubia",
    "HU31": "Northern Hungary",
    "HU32": "Northern Great Plain",
    "HU33": "Southern Great Plain",

    # IRELAND (IE)
    "IE0": "Ireland",
    "IE04": "Northern & Western Region",
    "IE05": "Eastern & Midland Region",
    "IE06": "Southern Region",

    # ITALY (IT)
    "ITC": "Northwest",
    "ITF": "South",
    "ITG": "Islands",
    "ITH": "Northeast",
    "ITI": "Centre",
    "ITC1": "Piemonte",
    "ITC2": "Valle d'Aosta",
    "ITC3": "Liguria",
    "ITC4": "Lombardia",
    "ITF1": "Abruzzo",
    "ITF2": "Molise",
    "ITF3": "Campania",
    "ITF4": "Puglia",
    "ITF5": "Basilicata",
    "ITF6": "Calabria",
    "ITG1": "Sicilia",
    "ITG2": "Sardegna",
    "ITH1": "Provincia Autonoma di Bolzano",
    "ITH2": "Provincia Autonoma di Trento",
    "ITH3": "Veneto",
    "ITH4": "Friuli Venezia Giulia",
    "ITH5": "Emilia-Romagna",
    "ITI1": "Toscana",
    "ITI2": "Umbria",
    "ITI3": "Marche",
    "ITI4": "Lazio",

    # LATVIA (LV)
    "LV0": "Latvia",
    "LV00": "Latvia",

    # LITHUANIA (LT)
    "LT0": "Lithuania",
    "LT00": "Lithuania",

    # LUXEMBOURG
    "LU0": "Luxembourg",
    "LU00": "Luxembourg",

    # MALTA
    "MT0": "Malta",
    "MT00": "Malta",

    # NETHERLANDS (NL)
    "NL1": "Northern Netherlands",
    "NL2": "Eastern Netherlands",
    "NL3": "Western Netherlands",
    "NL4": "Southern Netherlands",
    "NL11": "Groningen",
    "NL12": "Friesland",
    "NL13": "Drenthe",
    "NL21": "Overijssel",
    "NL22": "Gelderland",
    "NL23": "Flevoland",
    "NL31": "Utrecht",
    "NL32": "North Holland",
    "NL33": "South Holland",
    "NL34": "Zeeland",
    "NL41": "North Brabant",
    "NL42": "Limburg",

    # NORWAY (NO)
    "NO0": "Norway",
    "NO02": "Innlandet",
    "NO06": "Trøndelag",
    "NO07": "Northern Norway",
    "NO08": "Oslo og Viken",
    "NO09": "Vestfold og Telemark",
    "NO0A": "Agder",
    "NO0B": "Vestlandet",

    # POLAND (PL)
    "PL2": "South",
    "PL4": "North-West",
    "PL5": "South-West",
    "PL6": "Central",
    "PL7": "Mazowieckie",
    "PL8": "South-East",
    "PL9": "North",
    "PL21": "Małopolskie",
    "PL22": "Śląskie",
    "PL41": "Wielkopolskie",
    "PL42": "Zachodniopomorskie",
    "PL43": "Lubuskie",
    "PL51": "Dolnośląskie",
    "PL52": "Opolskie",
    "PL61": "Łódzkie",
    "PL62": "Świętokrzyskie",
    "PL63": "Podlaskie",
    "PL71": "Mazowieckie",
    "PL72": "Lubelskie",
    "PL81": "Podkarpackie",
    "PL82": "Świętokrzyskie",
    "PL91": "Pomorskie",
    "PL92": "Kujawsko-Pomorskie",

    # PORTUGAL (PT)
    "PT1": "Mainland Portugal",
    "PT2": "Azores",
    "PT3": "Madeira",
    "PT11": "North",
    "PT15": "Central",
    "PT16": "Lisbon",
    "PT17": "Alentejo",
    "PT18": "Algarve",
    "PT20": "Azores",
    "PT30": "Madeira",

    # ROMANIA (RO)
    "RO1": "Macroregion One",
    "RO2": "Macroregion Two",
    "RO3": "Macroregion Three",
    "RO4": "Macroregion Four",
    "RO11": "North-West",
    "RO12": "North-East",
    "RO21": "South-East",
    "RO22": "South-Muntenia",
    "RO31": "Bucharest-Ilfov",
    "RO32": "South-West Oltenia",
    "RO41": "West",

    # SLOVENIA (SI)
    "SI0": "Slovenia",
    "SI03": "Eastern Slovenia",
    "SI04": "Western Slovenia",

    # SLOVAKIA (SK)
    "SK0": "Slovakia",
    "SK01": "Bratislava Region",
    "SK02": "Western Slovakia",
    "SK03": "Central Slovakia",
    "SK04": "Eastern Slovakia",

    # SWEDEN (SE)
    "SE1": "East Sweden",
    "SE2": "South Sweden",
    "SE3": "North Sweden",
    "SE11": "Stockholm",
    "SE12": "East Middle Sweden",
    "SE21": "Småland and the Islands",
    "SE22": "Southern Sweden",
    "SE23": "West Sweden",
    "SE31": "North Middle Sweden",
    "SE32": "Central Norrland",
    "SE33": "Upper Norrland",

    # UNITED KINGDOM (UK)
    "UKC": "North East",
    "UKD": "North West",
    "UKE": "Yorkshire and the Humber",
    "UKF": "East Midlands",
    "UKG": "West Midlands",
    "UKH": "East of England",
    "UKI": "London",
    "UKJ": "South East",
    "UKK": "South West",
    "UKL": "Wales",
    "UKM": "Scotland",
    "UKN": "Northern Ireland",

    # TURKEY (TR) – NUTS1 + NUTS2
    "TR1": "West Anatolia",
    "TR2": "Aegean",
    "TR3": "Mediterranean",
    "TR4": "East Marmara",
    "TR5": "West Marmara",
    "TR6": "Central Anatolia",
    "TR7": "West Black Sea",
    "TR8": "East Black Sea",
    "TR9": "Northeast Anatolia",
    "TRA": "Central East Anatolia",
    "TRB": "Southeast Anatolia",

    "TR10": "Istanbul",
    "TR21": "Tekirdağ, Edirne, Kırklareli",
    "TR22": "Balıkesir, Çanakkale",
    "TR31": "İzmir",
    "TR32": "Aydın, Denizli, Muğla",
    "TR33": "Manisa, Afyon, Kütahya, Uşak",
    "TR41": "Bursa, Eskişehir, Bilecik",
    "TR42": "Kocaeli, Sakarya, Düzce, Bolu, Yalova",
    "TR51": "Ankara",
    "TR52": "Konya, Karaman",
    "TR61": "Antalya, Isparta, Burdur",
    "TR62": "Adana, Mersin",
    "TR63": "Hatay, Kahramanmaraş, Osmaniye",
    "TR71": "Kırıkkale, Aksaray, Niğde, Nevşehir, Kırşehir",
    "TR72": "Kayseri, Sivas, Yozgat",
    "TR81": "Zonguldak, Karabük, Bartın",
    "TR82": "Kastamonu, Çankırı, Sinop",
    "TR83": "Samsun, Tokat, Çorum, Amasya",
    "TR90": "Trabzon, Ordu, Giresun, Rize, Artvin, Gümüşhane",
    "TRA1": "Erzurum, Erzincan, Bayburt",
    "TRA2": "Ağrı, Kars, Iğdır, Ardahan",
    "TRB1": "Malatya, Elazığ, Bingöl, Tunceli",
    "TRB2": "Van, Muş, Bitlis, Hakkari",
    "TRC1": "Gaziantep, Adıyaman, Kilis",
    "TRC2": "Şanlıurfa, Diyarbakır",
    "TRC3": "Mardin, Batman, Şırnak, Siirt"
}

NUTS_COORDINATES = {
    "AT1": (48.2082, 16.3738),   # Eastern Austria → Vienna
    "AT2": (47.0707, 15.4395),   # Southern Austria → Graz
    "AT3": (47.2692, 11.4041),   # Western Austria → Innsbruck

    "AT11": (47.2010, 16.3691),  # Burgenland → Eisenstadt
    "AT12": (48.1089, 16.2689),  # Lower Austria → Sankt Pölten
    "AT13": (48.2082, 16.3738),  # Vienna
    "AT21": (46.6249, 14.3050),  # Carinthia → Klagenfurt
    "AT22": (47.0707, 15.4395),  # Styria → Graz
    "AT31": (48.3069, 14.2858),  # Upper Austria → Linz
    "AT32": (47.8095, 13.0550),  # Salzburg
    "AT33": (47.2692, 11.4041),  # Tyrol → Innsbruck
    "AT34": (47.5000, 9.7471),   # Vorarlberg → Bregenz

    "BE1": (50.8503, 4.3517),   # Brussels-Capital
    "BE2": (51.0000, 4.0000),   # Flanders → Antwerp area
    "BE3": (50.4669, 4.8675),   # Wallonia → Namur

    "BG3": (43.2141, 27.9147),  # Northern/Eastern Bulgaria → Varna
    "BG4": (42.6977, 23.3219),  # SW & SC Bulgaria → Sofia

    "BG31": (43.4140, 23.2250), # North-West → Vratsa
    "BG32": (43.8500, 25.9667), # North-Central → Ruse
    "BG33": (43.2047, 27.9106), # North-East → Varna
    "BG34": (42.5035, 27.4626), # South-East → Burgas
    "BG41": (42.6977, 23.3219), # South-West → Sofia
    "BG42": (42.1500, 24.7500), # South-Central → Plovdiv

    "CH0": (46.8182, 8.2275),   # Switzerland (country centre)
    "CH01": (47.5596, 7.5886),  # Northwestern → Basel
    "CH02": (47.3769, 8.5417),  # Eastern → St. Gallen
    "CH03": (46.9480, 8.2520),  # Central → Lucerne
    "CH04": (47.3769, 8.5417),  # Zürich
    "CH05": (46.2044, 6.1432),  # Lake Geneva Region → Geneva
    "CH06": (47.3000, 8.5000),  # Midland → Aarau
    "CH07": (46.0037, 8.9511),  # Ticino → Lugano

    "CY0": (35.1856, 33.3823),   # Cyprus → Nicosia
    "CY00": (35.1856, 33.3823),  # Entire island

    "CZ0": (50.0755, 14.4378),   # Czech Republic → Prague
    "CZ01": (50.0755, 14.4378),  # Prague
    "CZ02": (49.8267, 15.4750),  # Central Bohemia → Prague outskirts
    "CZ03": (49.7384, 13.3736),  # Southwest → Pilsen
    "CZ04": (50.6600, 13.8200),  # Northwest → Ústí nad Labem
    "CZ05": (50.0480, 16.2100),  # Northeast → Hradec Králové
    "CZ06": (49.1951, 16.6068),  # Southeast → Brno
    "CZ07": (49.5938, 17.2500),  # Central Moravia → Olomouc
    "CZ08": (49.8209, 18.2625),  # Moravia-Silesia → Ostrava

    "DK0": (55.6761, 12.5683),   # Denmark → Copenhagen
    "DK01": (55.6761, 12.5683),  # Capital Region → Copenhagen
    "DK02": (55.6290, 11.6761),  # Zealand → Sorø
    "DK03": (55.3700, 10.4300),  # Southern Denmark → Odense
    "DK04": (56.1500, 9.5500),   # Central Jutland → Aarhus (approx)
    "DK05": (57.0488, 9.9217),   # North Jutland → Aalborg

    "DE1": (48.7784, 9.1800),   # Baden-Württemberg → Stuttgart
    "DE2": (48.7904, 11.4979),  # Bavaria → Ingolstadt (central)
    "DE3": (52.5200, 13.4050),  # Berlin
    "DE4": (52.5200, 13.4050),  # Brandenburg → Potsdam (near Berlin)
    "DE5": (53.0793, 8.8017),   # Bremen
    "DE6": (53.5511, 9.9937),   # Hamburg
    "DE7": (50.1109, 8.6821),   # Hesse → Frankfurt
    "DE8": (53.6127, 12.4296),  # Mecklenburg-Vorpommern → Schwerin
    "DE9": (52.3759, 9.7320),   # Lower Saxony → Hanover
    "DEA": (51.4556, 7.0116),   # North Rhine–Westphalia → Essen
    "DEB": (49.9929, 8.2473),   # Rhineland-Palatinate → Mainz
    "DEC": (49.2333, 6.9833),   # Saarland → Saarbrücken
    "DED": (51.0504, 13.7373),  # Saxony → Dresden
    "DEE": (52.1205, 11.6276),  # Saxony-Anhalt → Magdeburg
    "DEF": (50.9848, 11.0299),  # Thuringia → Erfurt
    "DEG": (54.4820, 9.0500),   # Schleswig-Holstein → Rendsburg

    # NUTS2+ subdivisions
    "DE11": (48.7784, 9.1800),  # Stuttgart
    "DE12": (49.0069, 8.4037),  # Karlsruhe
    "DE13": (47.9990, 7.8421),  # Freiburg
    "DE14": (48.5227, 9.0536),  # Tübingen

    "DE21": (48.1371, 11.5754), # Upper Bavaria → Munich
    "DE22": (48.4465, 12.8428), # Lower Bavaria → Landshut
    "DE23": (49.0134, 12.1016), # Upper Palatinate → Regensburg
    "DE24": (50.2610, 11.3380), # Upper Franconia → Bayreuth
    "DE25": (49.4521, 11.0767), # Middle Franconia → Nuremberg
    "DE26": (50.0499, 10.2330), # Lower Franconia → Würzburg
    "DE27": (48.3974, 10.0023), # Swabia → Augsburg

    "DE30": (52.5200, 13.4050), # Berlin
    "DE40": (52.3906, 13.0645), # Brandenburg → Potsdam
    "DE50": (53.0793, 8.8017),  # Bremen
    "DE60": (53.5511, 9.9937),  # Hamburg

    "DE71": (49.8728, 8.6512),  # Darmstadt → Darmstadt
    "DE72": (50.5840, 8.6750),  # Gießen
    "DE73": (51.3155, 9.4924),  # Kassel

    "DE80": (53.6127, 12.4296), # Mecklenburg-Vorpommern → Schwerin

    "DE91": (52.2618, 10.5268), # Braunschweig
    "DE92": (52.3705, 9.7332),  # Hanover
    "DE93": (53.2500, 10.4167), # Lüneburg
    "DE94": (53.3669, 8.7770),  # Weser-Ems → Oldenburg

    "DEA1": (51.2333, 6.7833),  # Düsseldorf
    "DEA2": (50.9375, 6.9603),  # Cologne
    "DEA3": (51.9624, 7.6257),  # Münster
    "DEA4": (51.9294, 8.8590),  # Detmold
    "DEA5": (51.4186, 7.5700),  # Arnsberg

    "DEB1": (50.3569, 7.5880),  # Koblenz
    "DEB2": (49.7490, 6.6371),  # Trier
    "DEB3": (49.6322, 8.3480),  # Rheinhessen-Pfalz → Worms

    "DEC0": (49.2333, 6.9833),  # Saarland → Saarbrücken

    "DED2": (51.0504, 13.7373), # Dresden
    "DED4": (50.8323, 12.9253), # Chemnitz
    "DED5": (51.3397, 12.3731), # Leipzig

    "DEE0": (52.1205, 11.6276), # Saxony-Anhalt → Magdeburg
    "DEF0": (50.9848, 11.0299), # Thuringia → Erfurt
    "DEG0": (54.4820, 9.0500),  # Schleswig-Holstein

    "EE0": (59.4370, 24.7536),   # Estonia → Tallinn
    "EE00": (59.4370, 24.7536),  # Estonia

    "ES1": (43.3623, -8.4115),  # Northwest → A Coruña
    "ES2": (41.6488, -0.8891),  # Northeast → Zaragoza
    "ES3": (40.4168, -3.7038),  # Madrid
    "ES4": (39.8568, -4.0245),  # Centre → Toledo
    "ES5": (39.4699, -0.3763),  # East → Valencia
    "ES6": (37.3891, -5.9845),  # South → Sevilla
    "ES7": (28.2916, -16.6291), # Canary Islands → Tenerife

    "ES11": (42.5751, -8.1339), # Galicia → Santiago de Compostela
    "ES12": (43.3619, -5.8494), # Asturias → Oviedo
    "ES13": (43.4623, -3.8099), # Cantabria → Santander
    "ES21": (43.2630, -2.9350), # Basque Country → Bilbao
    "ES22": (42.8125, -1.6458), # Navarra → Pamplona
    "ES23": (42.4627, -2.4453), # La Rioja → Logroño
    "ES24": (41.6488, -0.8891), # Aragon → Zaragoza
    "ES30": (40.4168, -3.7038), # Madrid

    "ES41": (41.6520, -4.7286), # Castilla y León → Valladolid
    "ES42": (39.8568, -4.0245), # Castilla-La Mancha → Toledo
    "ES43": (38.8794, -7.0220), # Extremadura → Mérida

    "ES51": (41.3851, 2.1734),  # Catalonia → Barcelona
    "ES52": (39.4699, -0.3763), # Valencian Community → Valencia
    "ES53": (39.6130, 2.9623),  # Balearic Islands → Palma
    "ES61": (37.3891, -5.9845), # Andalusia → Sevilla
    "ES62": (37.9922, -1.1307), # Murcia
    "ES63": (35.8894, -5.3213), # Ceuta
    "ES64": (35.2923, -2.9381), # Melilla
    "ES70": (28.2916, -16.6291),# Canary Islands

    "FI1": (60.1699, 24.9384),   # Mainland Finland → Helsinki
    "FI2": (60.1000, 19.9500),   # Åland → Mariehamn

    "FI19": (60.2040, 24.9630),  # Southern Finland → Helsinki
    "FI1C": (62.2415, 25.7209),  # Western Finland → Jyväskylä
    "FI1D": (65.0121, 25.4651),  # Northern & Eastern → Oulu
    "FI20": (60.1000, 19.9500),  # Åland

    "FR1": (48.8566, 2.3522),    # Île-de-France → Paris
    "FR2": (47.9000, 1.9000),    # Centre-Val de Loire → Orléans
    "FR3": (47.2900, 5.0400),    # Bourgogne-Franche-Comté → Dijon
    "FR4": (49.1829, -0.3707),   # Normandy → Caen
    "FR5": (50.6292, 3.0573),    # Hauts-de-France → Lille
    "FR6": (48.5846, 7.7507),    # Grand Est → Strasbourg
    "FR7": (47.2184, -1.5536),   # Pays de la Loire → Nantes
    "FR8": (48.1173, -1.6778),   # Brittany → Rennes
    "FR9": (44.8378, -0.5792),   # Nouvelle-Aquitaine → Bordeaux

    "FRA": (16.2650, -61.5510),  # Guadeloupe → Basse-Terre
    "FRB": (14.6415, -61.0242),  # Martinique → Fort-de-France
    "FRC": (4.9224, -52.3135),   # Guyane → Cayenne
    "FRD": (-21.1151, 55.5364),  # La Réunion → Saint-Denis
    "FRE": (-12.8436, 45.1495),  # Mayotte → Mamoudzou

    "FRF": (48.6963, 6.1831),    # Grand Est → Nancy
    "FRG": (44.8378, -0.5792),   # Nouvelle-Aquitaine → Bordeaux
    "FRH": (43.6047, 1.4442),    # Occitanie → Toulouse
    "FRI": (45.7640, 4.8357),    # Auvergne-Rhône-Alpes → Lyon
    "FRJ": (48.8566, 2.3522),    # Île-de-France → Paris
    "FRK": (47.2900, 5.0400),    # Bourgogne-Franche-Comté → Dijon
    "FRL": (43.2965, 5.3698),    # Provence-Alpes-Côte d’Azur → Marseille
    "FRM": (42.0396, 9.0129),    # Corse → Ajaccio
    "FRY": (14.6415, -61.0242),  # French Overseas Territories (avg) → Fort-de-France

    "EL3": (37.9838, 23.7275),   # Attica → Athens
    "EL4": (35.3400, 25.1300),   # Aegean & Crete → Heraklion
    "EL5": (40.6401, 22.9444),   # Northern Greece → Thessaloniki
    "EL6": (38.2466, 21.7346),   # Central Greece → Patras

    "EL30": (37.9838, 23.7275),  # Attica → Athens
    "EL41": (39.1100, 26.5500),  # North Aegean → Mytilene
    "EL42": (36.3932, 25.4615),  # South Aegean → Santorini
    "EL43": (35.3400, 25.1300),  # Crete → Heraklion

    "EL51": (41.1333, 24.8833),  # Eastern Macedonia & Thrace → Komotini
    "EL52": (40.6401, 22.9444),  # Central Macedonia → Thessaloniki
    "EL53": (40.5167, 21.2667),  # Western Macedonia → Kozani
    "EL54": (39.6650, 20.8537),  # Epirus → Ioannina
    "EL55": (39.6372, 22.4200),  # Thessaly → Larissa

    "EL61": (39.6243, 19.9217),  # Ionian Islands → Corfu
    "EL62": (38.2466, 21.7346),  # Western Greece → Patras
    "EL63": (38.4667, 23.6000),  # Central Greece → Lamia
    "EL64": (37.0670, 22.4140),  # Peloponnese → Tripoli

    "HR0": (45.8150, 15.9819),   # Croatia → Zagreb
    "HR02": (45.1600, 18.0156),  # Panonia → Osijek
    "HR03": (44.1194, 15.2314),  # Adriatic Croatia → Zadar
    "HR06": (45.8150, 15.9819),  # Continental Croatia → Zagreb


    "HU1": (47.4979, 19.0402),   # Central Hungary → Budapest
    "HU2": (47.0000, 18.0000),   # Transdanubia → Székesfehérvár
    "HU3": (47.0000, 20.0000),   # Great Plain & North → Debrecen

    "HU11": (47.4979, 19.0402),  # Budapest
    "HU12": (47.4500, 19.3200),  # Pest → Gödöllő
    "HU21": (47.2000, 18.4000),  # Central Transdanubia → Székesfehérvár
    "HU22": (46.3610, 17.7969),  # Western Transdanubia → Zalaegerszeg
    "HU23": (46.0727, 18.2323),  # Southern Transdanubia → Pécs

    "HU31": (48.1000, 20.7833),  # Northern Hungary → Miskolc
    "HU32": (47.5316, 21.6273),  # Northern Great Plain → Debrecen
    "HU33": (46.9080, 19.6917),  # Southern Great Plain → Kecskemét

    "IE0": (53.3498, -6.2603),   # Ireland → Dublin
    "IE04": (54.2766, -8.4761),  # Northern & Western → Sligo
    "IE05": (53.3498, -6.2603),  # Eastern & Midland → Dublin
    "IE06": (52.6680, -8.6305),  # Southern → Limerick

    "ITC": (45.0703, 7.6869),    # Northwest → Turin
    "ITF": (40.8518, 14.2681),   # South → Naples
    "ITG": (39.2238, 9.1217),    # Islands → Cagliari
    "ITH": (45.4408, 12.3155),   # Northeast → Venice
    "ITI": (41.9028, 12.4964),   # Centre → Rome

    "ITC1": (45.0703, 7.6869),   # Piemonte → Turin
    "ITC2": (45.7370, 7.3201),   # Valle d'Aosta → Aosta
    "ITC3": (44.4056, 8.9463),   # Liguria → Genoa
    "ITC4": (45.4642, 9.1900),   # Lombardia → Milan

    "ITF1": (42.3512, 13.3984),  # Abruzzo → L'Aquila
    "ITF2": (41.5600, 14.6600),  # Molise → Campobasso
    "ITF3": (40.8518, 14.2681),  # Campania → Naples
    "ITF4": (41.1171, 16.8719),  # Puglia → Bari
    "ITF5": (40.6667, 15.8000),  # Basilicata → Potenza
    "ITF6": (38.9108, 16.5875),  # Calabria → Catanzaro

    "ITG1": (38.1157, 13.3615),  # Sicilia → Palermo
    "ITG2": (39.2238, 9.1217),   # Sardegna → Cagliari

    "ITH1": (46.4993, 11.3566),  # Bolzano
    "ITH2": (46.0667, 11.1167),  # Trento
    "ITH3": (45.4408, 12.3155),  # Veneto → Venice
    "ITH4": (45.6520, 13.7768),  # Friuli Venezia Giulia → Trieste
    "ITH5": (44.4949, 11.3426),  # Emilia-Romagna → Bologna

    "ITI1": (43.7711, 11.2486),  # Toscana → Florence
    "ITI2": (43.1107, 12.3874),  # Umbria → Perugia
    "ITI3": (43.6167, 13.5167),  # Marche → Ancona
    "ITI4": (41.9028, 12.4964),  # Lazio → Rome    

    "LV0":  (56.9496, 24.1052),  # Latvia → Riga
    "LV00": (56.9496, 24.1052),  # Latvia → Riga

    "LT0":  (54.6872, 25.2797),  # Lithuania → Vilnius
    "LT00": (54.6872, 25.2797),  # Lithuania → Vilnius

    "LU0":  (49.6116, 6.1319),   # Luxembourg → Luxembourg City
    "LU00": (49.6116, 6.1319),

    "MT0":  (35.8989, 14.5146),  # Malta → Valletta
    "MT00": (35.8989, 14.5146),

    "NL1":  (53.2194, 6.5665),   # Northern Netherlands → Groningen
    "NL2":  (52.2112, 5.9699),   # Eastern Netherlands → Apeldoorn (approx)
    "NL3":  (52.3676, 4.9041),   # Western Netherlands → Amsterdam
    "NL4":  (51.4416, 5.4697),   # Southern Netherlands → Eindhoven

    "NL11": (53.2194, 6.5665),   # Groningen
    "NL12": (53.2012, 5.7999),   # Friesland → Leeuwarden
    "NL13": (52.9920, 6.5640),   # Drenthe → Assen

    "NL21": (52.5168, 6.0830),   # Overijssel → Zwolle
    "NL22": (51.9851, 5.8987),   # Gelderland → Arnhem
    "NL23": (52.5185, 5.4714),   # Flevoland → Lelystad

    "NL31": (52.0907, 5.1214),   # Utrecht
    "NL32": (52.3874, 4.6462),   # North Holland → Haarlem
    "NL33": (52.0705, 4.3007),   # South Holland → The Hague
    "NL34": (51.4988, 3.6100),   # Zeeland → Middelburg

    "NL41": (51.6978, 5.3037),   # North Brabant → ’s-Hertogenbosch
    "NL42": (50.8514, 5.6910),   # Limburg → Maastricht

    "NO0":  (59.9139, 10.7522),  # Norway → Oslo
    "NO02": (60.7945, 11.0679),  # Innlandet → Hamar
    "NO06": (63.4305, 10.3951),  # Trøndelag → Trondheim
    "NO07": (69.6492, 18.9553),  # Northern Norway → Tromsø
    "NO08": (59.9139, 10.7522),  # Oslo og Viken → Oslo
    "NO09": (59.2096, 9.6080),   # Vestfold og Telemark → Skien
    "NO0A": (58.1467, 7.9956),   # Agder → Kristiansand
    "NO0B": (60.3913, 5.3221),   # Vestlandet → Bergen

    "PL2":  (50.0647, 19.9450),  # South → Kraków
    "PL4":  (53.4285, 14.5528),  # North-West → Szczecin
    "PL5":  (51.1079, 17.0385),  # South-West → Wrocław
    "PL6":  (51.7592, 19.4550),  # Central → Łódź
    "PL7":  (52.2297, 21.0122),  # Mazowieckie → Warsaw
    "PL8":  (50.0412, 21.9991),  # South-East → Rzeszów
    "PL9":  (54.3520, 18.6466),  # North → Gdańsk

    "PL21": (50.0647, 19.9450),  # Małopolskie → Kraków
    "PL22": (50.2649, 19.0238),  # Śląskie → Katowice

    "PL41": (52.4064, 16.9252),  # Wielkopolskie → Poznań
    "PL42": (53.4285, 14.5528),  # Zachodniopomorskie → Szczecin
    "PL43": (51.9356, 15.5064),  # Lubuskie → Zielona Góra

    "PL51": (51.1079, 17.0385),  # Dolnośląskie → Wrocław
    "PL52": (50.6751, 17.9213),  # Opolskie → Opole

    "PL61": (51.7592, 19.4550),  # Łódzkie → Łódź
    "PL62": (50.8661, 20.6286),  # Świętokrzyskie → Kielce
    "PL63": (53.1325, 23.1688),  # Podlaskie → Białystok

    "PL71": (52.2297, 21.0122),  # Mazowieckie → Warsaw
    "PL72": (51.2465, 22.5684),  # Lubelskie → Lublin

    "PL81": (50.0412, 21.9991),  # Podkarpackie → Rzeszów
    "PL82": (50.8661, 20.6286),  # Świętokrzyskie → Kielce

    "PL91": (54.3520, 18.6466),  # Pomorskie → Gdańsk
    "PL92": (53.1235, 18.0084),  # Kujawsko-Pomorskie → Bydgoszcz

    "PT1":  (38.7223, -9.1393),   # Mainland Portugal → Lisbon (approx)
    "PT2":  (37.7412, -25.6756),  # Azores → Ponta Delgada
    "PT3":  (32.6669, -16.9241),  # Madeira → Funchal

    "PT11": (41.1579, -8.6291),   # North → Porto
    "PT15": (40.2110, -8.4292),   # Central → Coimbra
    "PT16": (38.7223, -9.1393),   # Lisbon
    "PT17": (38.5667, -7.9000),   # Alentejo → Évora
    "PT18": (37.0194, -7.9304),   # Algarve → Faro
    "PT20": (37.7412, -25.6756),  # Azores
    "PT30": (32.6669, -16.9241),  # Madeira

    "RO1":  (46.7712, 23.6236),  # Macroregion One → Cluj-Napoca
    "RO2":  (47.1585, 27.6014),  # Macroregion Two → Iași
    "RO3":  (44.4268, 26.1025),  # Macroregion Three → Bucharest
    "RO4":  (45.7489, 21.2087),  # Macroregion Four → Timișoara

    "RO11": (46.7712, 23.6236),  # North-West → Cluj-Napoca
    "RO12": (47.1585, 27.6014),  # North-East → Iași
    "RO21": (44.1598, 28.6348),  # South-East → Constanța
    "RO22": (44.9460, 26.0365),  # South-Muntenia → Ploiești
    "RO31": (44.4268, 26.1025),  # Bucharest-Ilfov → Bucharest
    "RO32": (44.3302, 23.7949),  # South-West Oltenia → Craiova
    "RO41": (45.7489, 21.2087),  # West → Timișoara

    "SI0":  (46.0569, 14.5058),  # Slovenia → Ljubljana
    "SI03": (46.5547, 15.6459),  # Eastern Slovenia → Maribor
    "SI04": (46.0569, 14.5058),  # Western Slovenia → Ljubljana (approx)

    "SK0":  (48.1486, 17.1077),  # Slovakia → Bratislava
    "SK01": (48.1486, 17.1077),  # Bratislava Region → Bratislava
    "SK02": (48.3774, 17.5872),  # Western Slovakia → Trnava
    "SK03": (48.7363, 19.1462),  # Central Slovakia → Banská Bystrica
    "SK04": (48.7164, 21.2611),  # Eastern Slovakia → Košice
    "SE1":  (59.3293, 18.0686),  # East Sweden → Stockholm
    "SE2":  (55.6050, 13.0038),  # South Sweden → Malmö
    "SE3":  (63.8258, 20.2630),  # North Sweden → Umeå

    "SE11": (59.3293, 18.0686),  # Stockholm
    "SE12": (59.8586, 17.6389),  # East Middle Sweden → Uppsala

    "SE21": (56.8777, 14.8091),  # Småland & the Islands → Växjö
    "SE22": (55.6050, 13.0038),  # Southern Sweden → Malmö
    "SE23": (57.7089, 11.9746),  # West Sweden → Gothenburg

    "SE31": (60.6749, 17.1413),  # North Middle Sweden → Gävle
    "SE32": (63.1792, 14.6357),  # Central Norrland → Östersund
    "SE33": (65.5848, 22.1547),  # Upper Norrland → Luleå

    "UKC": (54.9783, -1.6178),  # North East → Newcastle upon Tyne
    "UKD": (53.4808, -2.2426),  # North West → Manchester
    "UKE": (53.8008, -1.5491),  # Yorkshire & the Humber → Leeds
    "UKF": (52.9548, -1.1581),  # East Midlands → Nottingham
    "UKG": (52.4862, -1.8904),  # West Midlands → Birmingham
    "UKH": (52.2053, 0.1218),   # East of England → Cambridge
    "UKI": (51.5074, -0.1278),  # London
    "UKJ": (51.4543, -0.9781),  # South East → Reading (approx)
    "UKK": (51.4545, -2.5879),  # South West → Bristol
    "UKL": (51.4816, -3.1791),  # Wales → Cardiff
    "UKM": (55.9533, -3.1883),  # Scotland → Edinburgh
    "UKN": (54.5973, -5.9301),  # Northern Ireland → Belfast

    "TR1":  (39.9334, 32.8597),  # West Anatolia → Ankara
    "TR2":  (38.4237, 27.1428),  # Aegean → İzmir
    "TR3":  (36.8969, 30.7133),  # Mediterranean → Antalya
    "TR4":  (40.1950, 29.0600),  # East Marmara → Bursa
    "TR5":  (40.9780, 27.5110),  # West Marmara → Tekirdağ
    "TR6":  (38.7333, 35.4833),  # Central Anatolia → Kayseri
    "TR7":  (41.4564, 31.7987),  # West Black Sea → Zonguldak
    "TR8":  (41.0015, 39.7178),  # East Black Sea → Trabzon
    "TR9":  (39.9043, 41.2679),  # Northeast Anatolia → Erzurum
    "TRA":  (38.3552, 38.3095),  # Central East Anatolia → Malatya
    "TRB":  (37.0662, 37.3833),  # Southeast Anatolia → Gaziantep

    # NUTS2
    "TR10": (41.0082, 28.9784),  # Istanbul
    "TR21": (40.9780, 27.5110),  # Tekirdağ, Edirne, Kırklareli → Tekirdağ
    "TR22": (39.6484, 27.8826),  # Balıkesir, Çanakkale → Balıkesir
    "TR31": (38.4237, 27.1428),  # İzmir
    "TR32": (37.8444, 27.8458),  # Aydın, Denizli, Muğla → Aydın
    "TR33": (38.6191, 27.4289),  # Manisa, Afyon, Kütahya, Uşak → Manisa
    "TR41": (40.1950, 29.0600),  # Bursa, Eskişehir, Bilecik → Bursa
    "TR42": (40.7669, 29.9169),  # Kocaeli, Sakarya, Düzce, Bolu, Yalova → İzmit
    "TR51": (39.9334, 32.8597),  # Ankara
    "TR52": (37.8746, 32.4932),  # Konya, Karaman → Konya
    "TR61": (36.8969, 30.7133),  # Antalya, Isparta, Burdur → Antalya
    "TR62": (37.0000, 35.3213),  # Adana, Mersin → Adana
    "TR63": (36.2028, 36.1605),  # Hatay, Kahramanmaraş, Osmaniye → Antakya
    "TR71": (39.8455, 33.5153),  # Kırıkkale, Aksaray, Niğde, Nevşehir, Kırşehir → Kırıkkale
    "TR72": (38.7333, 35.4833),  # Kayseri, Sivas, Yozgat → Kayseri
    "TR81": (41.4564, 31.7987),  # Zonguldak, Karabük, Bartın → Zonguldak
    "TR82": (41.3887, 33.7827),  # Kastamonu, Çankırı, Sinop → Kastamonu
    "TR83": (41.2867, 36.3300),  # Samsun, Tokat, Çorum, Amasya → Samsun
    "TR90": (41.0015, 39.7178),  # Trabzon, Ordu, Giresun, Rize, Artvin, Gümüşhane → Trabzon
    "TRA1": (39.9043, 41.2679),  # Erzurum, Erzincan, Bayburt → Erzurum
    "TRA2": (39.7191, 43.0514),  # Ağrı, Kars, Iğdır, Ardahan → Ağrı
    "TRB1": (38.3552, 38.3095),  # Malatya, Elazığ, Bingöl, Tunceli → Malatya
    "TRB2": (38.4942, 43.3809),  # Van, Muş, Bitlis, Hakkari → Van
    "TRC1": (37.0662, 37.3833),  # Gaziantep, Adıyaman, Kilis → Gaziantep
    "TRC2": (37.1591, 38.7969),  # Şanlıurfa, Diyarbakır → Şanlıurfa
    "TRC3": (37.3129, 40.7339),  # Mardin, Batman, Şırnak, Siirt → Mardin

}

CAPITAL_COORDINATES = {
    "BE": (50.8503, 4.3517),    # Brussels
    "BG": (42.6977, 23.3219),   # Sofia
    "CZ": (50.0755, 14.4378),   # Prague
    "DK": (55.6761, 12.5683),   # Copenhagen
    "DE": (52.5200, 13.4050),   # Berlin
    "EE": (59.4370, 24.7536),   # Tallinn
    "IE": (53.3498, 6.2603),    # Dublin
    "EL": (37.9838, 23.7275),   # Athens
    "GR": (37.9838, 23.7275),   # Athens
    "ES": (40.4168, -3.7038),   # Madrid
    "FR": (48.8566, 2.3522),    # Paris
    "HR": (45.8150, 15.9819),   # Zagreb
    "IT": (41.9028, 12.4964),   # Rome
    "CY": (35.1856, 33.3823),   # Nicosia
    "LV": (56.9496, 24.1052),   # Riga
    "LT": (54.6872, 25.2797),   # Vilnius
    "LU": (49.6116, 6.1319),    # Luxembourg City
    "HU": (47.4979, 19.0402),   # Budapest
    "MT": (35.8989, 14.5146),   # Valletta
    "NL": (52.3676, 4.9041),    # Amsterdam
    "AT": (48.2082, 16.3738),   # Vienna
    "PL": (52.2297, 21.0122),   # Warsaw
    "PT": (38.7223, -9.1393),   # Lisbon
    "RO": (44.4268, 26.1025),   # Bucharest
    "SI": (46.0569, 14.5058),   # Ljubljana
    "SK": (48.1486, 17.1077),   # Bratislava
    "FI": (60.1699, 24.9384),   # Helsinki
    "SE": (59.3293, 18.0686),   # Stockholm
    "NO": (59.9139, 10.7522),   # Oslo
    "CH": (46.9480, 7.4474),    # Bern
    "TR": (39.9334, 32.8597),   # Ankara
}
