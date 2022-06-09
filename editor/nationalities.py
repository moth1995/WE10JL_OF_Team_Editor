def get_nation(idx:int):
    return nations[idx] if 0 <= idx < len(nations) else nations[nations.index("Free Nationality")]

def get_nation_idx(nation:str):
    return nations.index(nation) if nation in nations else nations.index("Free Nationality")

nations = [
    "Japon",
    "Inglaterra",
    "Francia",
    "Italia",
    "Holanda",
    "España",
    "Ucrania",
    "Grecia",
    "Suecia",
    "Escocia",
    "Rep.Checa",
    "Dinamarca",
    "Alemania",
    "Turquía",
    "Noruega",
    "Bélgica",
    "Portugal",
    "Argentina",
    "Brasil",
    "Corea del Sur",
    "China",
    "Indonesia",
    "Tailandia",
    "Vietnam",
    "Irán",
    "Irak",
    "Kuwait",
    "Qatar",
    "Arabia Saudita",
    "Siria",
    "Emiratos Arabes",
    "Uzbekistán",
    "Costa Rica",
    "México",
    "Estados Unidos",
    "Nueva Zelanda",
    "Papúa Nueva Guinea",
    "Australia",
    "Nigeria",
    "Sudáfrica",
    "Argelia",
    "Albania",
    "Armenia",
    "Austria",
    "Bielorrusia",
    "Bosnia y Herzegovina",
    "Bulgaria",
    "Croacia",
    "Chipre",
    "Estonia",
    "Finlandia",
    "Georgia",
    "Hungría",
    "Islandia",
    "Irlanda",
    "Israel",
    "Letonia",
    "Liechtenstein",
    "Lituania",
    "Macedonia del Norte",
    "Irlanda del Norte",
    "Polonia",
    "Rumania",
    "Rusia",
    "Serbia",
    "Eslovaquia",
    "Eslovenia",
    "Suiza",
    "Gales",
    "Angola",
    "Benín",
    "Burkina Faso",
    "Camerún",
    "Cabo Verde",
    "Congo",
    "Costa de Marfil",
    "RD Congo",
    "Egipto",
    "Guinea Ecuatorial",
    "Gabón",
    "Gambia",
    "Ghana",
    "Guinea",
    "Guinea-Bissau",
    "Kenia",
    "Liberia",
    "Libia",
    "Malí",
    "Marruecos",
    "Mozambique",
    "Senegal",
    "Sierra Leona",
    "Togo",
    "Túnez",
    "Zimbabwe",
    "Canadá",
    "Granada",
    "Guadalupe",
    "Honduras",
    "Jamaica",
    "Martinica",
    "Antillas Holandesas",
    "Panamá",
    "Trinidad y Tobago",
    "Bolivia",
    "Chile",
    "Colombia",
    "Ecuador",
    "Paraguay",
    "Perú",
    "Uruguay",
    "Venezuela",
    "Bahrein",
    "Malasia",
    "Corea del Norte",
    "Omán",
    "Turkmenistán",
    "Free Nationality",
]
