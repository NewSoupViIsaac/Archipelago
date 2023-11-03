from typing import Set, Dict
from BaseClasses import Location
from worlds.tboir.Utils import determine_enabled_bosses
from worlds.AutoWorld import World

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
    "Basement 1 Treasure Room": (base_id + 1000, "Basement 1", "Treasure Room Item"),
    "Basement 2 Treasure Room": (base_id + 1001, "Basement 2", "Treasure Room Item"),
    "Caves 1 Treasure Room": (base_id + 1002, "Caves 1", "Treasure Room Item"),
    "Caves 2 Treasure Room": (base_id + 1003, "Caves 2", "Treasure Room Item"),
    "Depths 1 Treasure Room": (base_id + 1004, "Depths 1", "Treasure Room Item"),
    "Depths 2 Treasure Room": (base_id + 1005, "Depths 2", "Quality 4 Item"),

    "Downpour 1 Treasure Room": (base_id + 1020, "Downpour 1", "Random Pickup"),
    "Downpour 2 Treasure Room": (base_id + 1021, "Downpour 2", "Random Pickup"),
    "Mines 1 Treasure Room": (base_id + 1022, "Mines 1", "Random Pickup"),
    "Mines 2 Treasure Room": (base_id + 1023, "Mines 2", "Random Pickup"),
    "Mausoleum 1 Treasure Room": (base_id + 1024, "Mausoleum 1", "Random Pickup"),
    "Mausoleum 2 Treasure Room": (base_id + 1025, "Mausoleum 2", "Random Pickup"),

    "Blue Womb Left Treasure Room": (base_id + 1040, "Blue Womb", "Treasure Room Item"),
    "Blue Womb Right Treasure Room": (base_id + 1041, "Blue Womb", "Treasure Room Item"),

    "Basement 1 Boss Item": (base_id + 1050, "Basement 1", "Boss Item"),
    "Basement 2 Boss Item": (base_id + 1051, "Basement 2", "Boss Item"),
    "Caves 1 Boss Item": (base_id + 1052, "Caves 1", "Boss Item"),
    "Caves 2 Boss Item": (base_id + 1053, "Caves 2", "Boss Item"),
    "Depths 1 Boss Item": (base_id + 1054, "Depths 1", "Boss Item"),
    "Mom": (base_id + 1055, "Depths 2", "Boss Item"),
    "Womb 1 Boss Item": (base_id + 1056, "Womb 1", "Boss Item"),
    "Mom's Heart": (base_id + 1057, "Womb 2", "Boss Item"),

    "Downpour 1 Boss Item": (base_id + 1060, "Downpour 1", "Random Pickup"),
    "Downpour 2 Boss Item": (base_id + 1061, "Downpour 2", "Random Pickup"),
    "Mines 1 Boss Item": (base_id + 1062, "Mines 1", "Random Pickup"),
    "Mines 2 Boss Item": (base_id + 1063, "Mines 2", "Random Pickup"),
    "Mausoleum 1 Boss Item": (base_id + 1064, "Mausoleum 1", "Random Pickup"),
    "Mausoleum 2 Boss Item": (base_id + 1065, "Mausoleum 2", "Random Pickup"),
    "Corpse 1 Boss Item": (base_id + 1066, "Corpse 1", "Random Pickup"),
    "Mother": (base_id + 1067, "Corpse 2", "Random Item"),

    "Satan": (base_id + 1070, "Sheol", "Random Item"),
    "Lamb": (base_id + 1071, "Dark Room", "Random Item"),
    "Isaac": (base_id + 1072, "Cathedral", "Random Item"),
    "Blue Baby": (base_id + 1073, "Chest", "Random Item"),

    "Boss Rush": (base_id + 1080, "Boss Rush", "Random Item"),
    "Hush": (base_id + 1081, "Blue Womb", "Random Item"),
    "Delirium": (base_id + 1082, "Void", "Random Item"),
    "Dogma": (base_id + 1083, "Home", "Random Item"),
    "Beast": (base_id + 1084, "Beast", "Random Item"),
    "Mega Satan": (base_id + 1085, "Mega Satan", "Random Item"),
    "Alternate Mom": (base_id + 1086, "Mausoleum 2", "Random Item"),
    "Alternate Mom's Heart": (base_id + 1087, "Alternate Mom's Heart", "Random Item"),
    # "Ultra Greed": (base_id + 1088, "Ultra Greed", "Random Item"),

    "Angel Deal Item 1": (base_id + 1100, "Angel Room 1", "Angel Deal Item"),
    "Angel Deal Item 2": (base_id + 1101, "Angel Room 2", "Angel Deal Item"),
    "Devil Deal Item 1": (base_id + 1102, "Devil Room 1", "Devil Deal Item"),
    "Devil Deal Item 2": (base_id + 1103, "Devil Room 2", "Devil Deal Item"),

    "Planetarium Item": (base_id + 1110, "Planetarium", "Planetarium Item"),

    "Shop Item 1": (base_id + 1120, "Shop 1", "Shop Item"),
    "Shop Item 2": (base_id + 1121, "Shop 2", "Shop Item"),
    "Shop Item 3": (base_id + 1122, "Shop 3", "Shop Item"),
    "Shop Item 4": (base_id + 1123, "Shop 4", "Shop Item"),
    "Shop Item 5": (base_id + 1124, "Shop 5", "Shop Item"),
}

unlock_related_locations = {
    "Key Piece 1": (base_id + 1150, "Key Piece 1"),
    "Key Piece 2": (base_id + 1151, "Key Piece 2"),
    "Knife Piece 1": (base_id + 1152, "Downpour 2"),
    "Knife Piece 2": (base_id + 1153, "Mines 2"),
    "Dad's Note": (base_id + 1154, "Alternate Mausoleum 2"),
    "Polaroid": (base_id + 1155, "Depths 2"),
    "Negative": (base_id + 1156, "Depths 2"),
}

logic_mode_locations = logic_regular_locations.copy()
logic_mode_locations.update(unlock_related_locations)

location_table = {
    **base_location_table,
    **item_pickups,
    **{k: v[0] for k, v in logic_mode_locations.items()}
}

lookup_id_to_name: Dict[int, str] = {id: name for name, id in location_table.items()}


def get_logic_mode_locations(world: World, populatable_regions: Set[str]):
    unlock_items = set()
    event_locations = set()

    locations = {
        "Basement 1 Treasure Room",
        "Basement 2 Treasure Room",
        "Caves 1 Treasure Room",
        "Caves 2 Treasure Room",
        "Depths 1 Treasure Room",
        "Depths 2 Treasure Room",

        "Basement 1 Boss Item",
        "Basement 2 Boss Item",
        "Caves 1 Boss Item",
        "Caves 2 Boss Item",
        "Depths 1 Boss Item",
        "Mom",
        "Womb 1 Boss Item",
        "Mom's Heart",
        "Satan",
        "Lamb",
        "Isaac",
        "Blue Baby",
    }

    if world.options.alternate_path:
        locations |= {
            "Downpour 1 Treasure Room",
            "Downpour 2 Treasure Room",
            "Mines 1 Treasure Room",
            "Mines 2 Treasure Room",
            "Mausoleum 1 Treasure Room",
            "Mausoleum 2 Treasure Room",

            "Downpour 1 Boss Item",
            "Downpour 2 Boss Item",
            "Mines 1 Boss Item",
            "Mines 2 Boss Item",
            "Mausoleum 1 Boss Item",
            "Mausoleum 2 Boss Item",
            "Corpse 1 Boss Item",
            "Alternate Mom",
            "Alternate Mom's Heart",
            "Mother",
        }

    if world.options.extra_bosses:
        locations |= {
            "Boss Rush",
            "Hush",
            "Delirium",
            "Dogma",
            "Beast",
            "Mega Satan",
            #  "Ultra Greed",

            "Blue Womb Left Treasure Room",
            "Blue Womb Right Treasure Room",

            "Mother",
        }

    if world.options.shop_checks:
        locations |= {
            "Shop Item 1",
            "Shop Item 2",
            "Shop Item 3",
            "Shop Item 4",
            "Shop Item 5",
        }

    if world.options.planetarium_check:
        locations |= {
            "Planetarium Item",
        }

    if world.options.angel_devil_checks:
        locations |= {
            "Angel Deal Item 1",
            "Angel Deal Item 2",
            "Devil Deal Item 1",
            "Devil Deal Item 2",
        }

    direct_goal_only_bosses = determine_enabled_bosses(world, goal_only=True)
    required_bosses = determine_enabled_bosses(world)

    locations = {location for location in locations if logic_mode_locations[location][1] in populatable_regions}

    event_unlocks = set()

    if "Mother" in locations:
        locations.add("Knife Piece 1")
        locations.add("Knife Piece 2")
        unlock_items.add("Knife Piece 1")
        unlock_items.add("Knife Piece 2")
    elif required_bosses["Mother"]:
        event_unlocks.add("Knife Piece 1")
        event_unlocks.add("Knife Piece 2")

    if "Beast" in locations or "Dogma" in locations:
        locations.add("Dad's Note")
        unlock_items.add("Dad's Note")
        unlock_items.add("Polaroid")
    elif required_bosses["Beast"] or required_bosses["Dogma"]:
        event_unlocks.add("Dad's Note")
        event_unlocks.add("Polaroid")

    if "Blue Baby" in locations:
        unlock_items.add("Polaroid")
    elif required_bosses["Blue Baby"]:
        event_unlocks.add("Polaroid")

    if "Lamb" in locations:
        unlock_items.add("Negative")
        if required_bosses["Lamb"]:
            unlock_items.add("Polaroid")
    elif required_bosses["Lamb"]:
        event_unlocks.add("Negative")

    if "Mega Satan" in locations:
        locations.add("Key Piece 1")
        locations.add("Key Piece 2")
        unlock_items.add("Key Piece 1")
        unlock_items.add("Key Piece 2")
    elif required_bosses["Mega Satan"]:
        event_unlocks.add("Key Piece 1")
        event_unlocks.add("Key Piece 2")

    if "Polaroid" in unlock_items and "Negative" in event_unlocks:
        event_unlocks.remove("Negative")
        unlock_items.add("Negative")

    if "Negative" in unlock_items and "Polaroid" in event_unlocks:
        event_unlocks.remove("Polaroid")
        unlock_items.add("Polaroid")

    for boss in (boss for boss, enabled in direct_goal_only_bosses.items() if enabled):
        if boss in locations:
            locations.remove(boss)

    for unlock_item in event_unlocks:
        if unlock_item not in unlock_items and not (unlock_item in {"Polaroid", "Negative"} and either_photo_in):
            event_locations.add((unlock_item, unlock_item + " Acquired"))

    for boss, enabled in required_bosses.items():
        if enabled:
            event_locations.add((boss, boss + " Beaten"))

    locations = sorted(locations, key=lambda loc: logic_mode_locations[loc][1])

    unlock_items = sorted(unlock_items)

    return locations, unlock_items, event_locations
