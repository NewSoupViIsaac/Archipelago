import typing
from BaseClasses import Location


class TheBindingOfIsaacRepentanceLocation(Location):
    game: str = "The Binding of Isaac Rebirth"


base_id = 78000

base_location_table = {
    "Run End": None
}

item_pickups = {
    f"ItemPickup{i + 1}": base_id + i for i in range(0, 500)
}

logic_regular_locations = {
    "Basement 1 Item Room": (base_id + 1000, "Basement 1"),
    "Basement 2 Item Room": (base_id + 1001, "Basement 2"),
    "Caves 1 Item Room": (base_id + 1002, "Caves 1"),
    "Caves 2 Item Room": (base_id + 1003, "Caves 2"),
    "Depths 1 Item Room": (base_id + 1004, "Depths 1"),
    "Depths 2 Item Room": (base_id + 1005, "Depths 2"),

    "Downpour 1 Item Room": (base_id + 1020, "Downpour 1"),
    "Downpour 2 Item Room": (base_id + 1021, "Downpour 2"),
    "Mines 1 Item Room": (base_id + 1022, "Mines 1"),
    "Mines 2 Item Room": (base_id + 1023, "Mines 2"),
    "Mausoleum 1 Item Room": (base_id + 1024, "Mausoleum 1"),
    "Mausoleum 2 Item Room": (base_id + 1025, "Mausoleum 2"),

    "Blue Womb Left Item Room": (base_id + 1040, "Blue Womb"),
    "Blue Womb Right Item Room": (base_id + 1041, "Blue Womb"),

    "Basement 1 Boss Item": (base_id + 1050, "Basement 1"),
    "Basement 2 Boss Item": (base_id + 1051, "Basement 2"),
    "Caves 1 Boss Item": (base_id + 1052, "Caves 1"),
    "Caves 2 Boss Item": (base_id + 1053, "Caves 2"),
    "Depths 1 Boss Item": (base_id + 1054, "Depths 1"),
    "Mom": (base_id + 1055, "Depths 2"),
    "Womb 1 Boss Item": (base_id + 1056, "Womb 1"),
    "Mom's Heart": (base_id + 1057, "Womb 2"),

    "Downpour 1 Boss Item": (base_id + 1060, "Downpour 1"),
    "Downpour 2 Boss Item": (base_id + 1061, "Downpour 2"),
    "Mines 1 Boss Item": (base_id + 1062, "Mines 1"),
    "Mines 2 Boss Item": (base_id + 1063, "Mines 2"),
    "Mausoleum 1 Boss Item": (base_id + 1064, "Mausoleum 1"),
    "Mausoleum 2 Boss Item": (base_id + 1065, "Mausoleum 2"),
    "Corpse 1 Boss Item": (base_id + 1066, "Corpse 1"),
    "Mother": (base_id + 1067, "Corpse 2"),

    "Satan": (base_id + 1070, "Sheol"),
    "Lamb": (base_id + 1071, "Dark Room"),
    "Isaac": (base_id + 1072, "Cathedral"),
    "Blue Baby": (base_id + 1073, "Chest"),

    "Boss Rush": (base_id + 1080, "Boss Rush"),
    "Hush": (base_id + 1081, "Blue Womb"),
    "Delirium": (base_id + 1082, "Void"),
    "Beast": (base_id + 1083, "Home"),
    "Mega Satan": (base_id + 1084, "Mega Satan"),
    "Alternate Mom's Heart": (base_id + 1085, "Alternate Mom's Heart"),

    "Angel Deal Item 1": (base_id + 1100, "Angel Deal 1"),
    "Angel Deal Item 2": (base_id + 1101, "Angel Deal 2"),
    "Devil Deal Item 1": (base_id + 1102, "Devil Deal 1"),
    "Devil Deal Item 2": (base_id + 1103, "Devil Deal 2"),

    "Planetarium Item": (base_id + 1110, "Planetarium"),

    "Shop Item 1": (base_id + 1120, "Shop 1"),
    "Shop Item 2": (base_id + 1121, "Shop 2"),
    "Shop Item 3": (base_id + 1122, "Shop 3"),
    "Shop Item 4": (base_id + 1123, "Shop 4"),
    "Shop Item 5": (base_id + 1124, "Shop 5"),
}

unlock_related_locations = {
    "Key Piece 1": (base_id + 1150, "Angel Deal 1", "Mega Satan"),
    "Key Piece 2": (base_id + 1151, "Angel Deal 2", "Mega Satan"),
    "Knife Piece 1": (base_id + 1152, "Downpour 2", "Mother"),
    "Knife Piece 2": (base_id + 1153, "Mines 2", "Mother"),
    "Dad's Note": (base_id + 1154, "Alternate Mausoleum 2", "Beast"),
}

logic_mode_locations = logic_regular_locations.copy()
logic_mode_locations.update(unlock_related_locations)

location_table = {
    **base_location_table,
    **item_pickups,
    **{k: v[0] for k, v in logic_mode_locations.items()}
}

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in location_table.items()}
