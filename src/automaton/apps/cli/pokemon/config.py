BUG = "#A6B91A"
DARK = "#705746"
DRAGON = "#6F35FC"
ELECTRIC = "#F7D02C"
FAIRY = "#D685AD"
FIGHTING = "#C22E28"
FIRE = "#EE8130"
FLYING = "#A98FF3"
GHOST = "#735797"
GRASS = "#7AC74C"
GROUND = "#E2BF65"
ICE = "#96D9D6"
NORMAL = "#A8A77A"
POISON = "#A33EA1"
PSYCHIC = "#F95587"
ROCK = "#B6A136"
STEEL = "#B7B7CE"
WATER = "#6390F0"

POKEMON_TYPES_COLORS = {
    "Bug": BUG,
    "Dark": DARK,
    "Dragon": DRAGON,
    "Electric": ELECTRIC,
    "Fairy": FAIRY,
    "Fighting": FIGHTING,
    "Fire": FIRE,
    "Flying": FLYING,
    "Ghost": GHOST,
    "Grass": GRASS,
    "Ground": GROUND,
    "Ice": ICE,
    "Normal": NORMAL,
    "Poison": POISON,
    "Psychic": PSYCHIC,
    "Rock": ROCK,
    "Steel": STEEL,
    "Water": WATER,
}


class TableConfig:
    columns = [
        "dex_number",
        "name",
        "type_01",
        "type_02",
        "hp",
        "attack",
        "defense",
        "sp_attack",
        "sp_defense",
        "speed",
        "total",
    ]

    def __init__(self, title: str):
        self.title = title
