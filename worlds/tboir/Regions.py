from typing import Dict, Callable, List

from typing_extensions import DefaultDict

from BaseClasses import MultiWorld, Region, CollectionState, Entrance, ItemClassification
from . import TheBindingOfIsaacRepentanceItem
from .Locations import unlock_related_locations, logic_mode_locations, TheBindingOfIsaacRepentanceLocation, \
    get_logic_mode_locations
from .Utils import determine_enabled_bosses

base_regions = [
    "Basement 1",
    "Basement 2",
    "Caves 1",
    "Caves 2",
    "Depths 1",
    "Depths 2",
    "Womb 1",
    "Womb 2",
    "Downpour 1",
    "Downpour 2",
    "Mines 1",
    "Mines 2",
    "Mausoleum 1",
    "Mausoleum 2",
    "Corpse 1",
    "Corpse 2",
    "Angel Room 1",
    "Angel Room 2",
    "Devil Room 1",
    "Devil Room 2",
    "Planetarium",
    "Shop 1",
    "Shop 2",
    "Shop 3",
    "Shop 4",
    "Shop 5",
    "Sheol",
    "Cathedral",
    "Dark Room",
    "Chest",
    "Alternate Mom's Heart",
    "Boss Rush",
    "Blue Womb",
    "Void",
    "Home",
    "Beast",
    "Mega Satan",
    "Key Piece 1",
    "Key Piece 2",
    "Knife Piece 1",
    "Knife Piece 2",
    "Alternate Mausoleum 2",
    "Ultra Greed",
]

level_3_regions = {
    "Void",
    "Home",
    "Mega Satan",
    "Dark Room",
    "Chest",
    "Key Piece 1",
    "Key Piece 2",
}

level_2_regions = {
    "Sheol",
    "Cathedral",
}

level_1_regions = {
    "Blue Womb",
    "Womb 1",
    "Womb 2",
    "Corpse 1",
    "Corpse 2",
    "Alternate Mom's Heart",
    "Alternate Mausoleum 2",
}


def connect(source: Region, target: Region, player: int, condition: Callable[[CollectionState], bool]):
    """
    connect two regions and set the corresponding requirement
    """

    connection = Entrance(
        player,
        source.name + " to " + target.name,
        source
    )

    connection.access_rule = condition

    source.exits.append(connection)
    connection.connect(target)


def connect_all_regions(multiworld: MultiWorld, player: int, regions: Dict[str, Region], ):
    # Meh

    connect(
        regions["Basement 1"], regions["Ultra Greed"], player,
        lambda state: True
    )

    # Regular Path Down

    connect(
        regions["Basement 1"], regions["Basement 2"], player,
        lambda state: True
    )
    connect(
        regions["Basement 2"], regions["Caves 1"], player,
        lambda state: state.has("Boss Item", player, 2) and state.has("Treasure Room Item", player, 1)
    )
    connect(
        regions["Caves 1"], regions["Caves 2"], player,
        lambda state: state.has("Boss Item", player, 2) and state.has("Treasure Room Item", player, 1)
    )
    connect(
        regions["Caves 2"], regions["Depths 1"], player,
        lambda state: state.has("Boss Item", player, 4) and state.has("Treasure Room Item", player, 3)
    )
    connect(
        regions["Depths 1"], regions["Depths 2"], player,
        lambda state: state.has("Boss Item", player, 4) and state.has("Treasure Room Item", player, 3)
    )
    connect(
        regions["Depths 2"], regions["Womb 1"], player,
        lambda state: state.has("Boss Item", player, 5) and state.has("Treasure Room Item", player, 5)
    )
    connect(
        regions["Womb 1"], regions["Womb 2"], player,
        lambda state: state.has("Boss Item", player, 5) and state.has("Treasure Room Item", player, 5)
    )
    connect(
        regions["Womb 2"], regions["Sheol"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
    )
    connect(
        regions["Womb 2"], regions["Cathedral"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
    )
    connect(
        regions["Cathedral"], regions["Chest"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
        and state.has("Quality 4 Item", player, 1)
        and (state.has("Polaroid", player, 1) or state.has("Polaroid Acquired", player, 1))
    )
    connect(
        regions["Sheol"], regions["Dark Room"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
        and state.has("Quality 4 Item", player, 1)
        and (state.has("Negative", player, 1) or state.has("Negative Acquired", player, 1))
    )

    # Alt Path

    connect(
        regions["Basement 1"], regions["Downpour 1"], player,
        lambda state: state.has("Boss Item", player, 1) and state.has("Treasure Room Item", player, 1)
    )
    connect(
        regions["Downpour 1"], regions["Downpour 2"], player,
        lambda state: state.has("Boss Item", player, 1) and state.has("Treasure Room Item", player, 1)
    )
    connect(
        regions["Basement 2"], regions["Downpour 2"], player,
        lambda state: state.has("Boss Item", player, 1) and state.has("Treasure Room Item", player, 1)
    )
    connect(
        regions["Downpour 2"], regions["Mines 1"], player,
        lambda state: state.has("Boss Item", player, 3) and state.has("Treasure Room Item", player, 2)
    )
    connect(
        regions["Caves 1"], regions["Mines 1"], player,
        lambda state: state.has("Boss Item", player, 3) and state.has("Treasure Room Item", player, 2)
    )
    connect(
        regions["Mines 1"], regions["Mines 2"], player,
        lambda state: state.has("Boss Item", player, 3) and state.has("Treasure Room Item", player, 2)
    )
    connect(
        regions["Caves 2"], regions["Mines 2"], player,
        lambda state: state.has("Boss Item", player, 3) and state.has("Treasure Room Item", player, 2)
    )
    connect(
        regions["Mines 2"], regions["Mausoleum 1"], player,
        lambda state: state.has("Boss Item", player, 5) and state.has("Treasure Room Item", player, 4)
    )
    connect(
        regions["Depths 1"], regions["Mausoleum 1"], player,
        lambda state: state.has("Boss Item", player, 5) and state.has("Treasure Room Item", player, 4)
    )
    connect(
        regions["Mausoleum 1"], regions["Mausoleum 2"], player,
        lambda state: state.has("Boss Item", player, 5) and state.has("Treasure Room Item", player, 4)
    )
    connect(
        regions["Mausoleum 2"], regions["Alternate Mom's Heart"], player,
        lambda state: state.has("Knife Piece 1", player) and state.has("Knife Piece 2", player)
        or state.has("Knife Piece 1 Acquired", player) and state.has("Knife Piece 2 Acquired", player)
    )
    connect(
        regions["Alternate Mom's Heart"], regions["Corpse 1"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
    )
    connect(
        regions["Corpse 1"], regions["Corpse 2"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
    )

    # Alt Bosses

    connect(
        regions["Depths 2"], regions["Boss Rush"], player,
        lambda state: state.has("Boss Item", player, 5) and state.has("Treasure Room Item", player, 4)
    )

    connect(
        regions["Womb 2"], regions["Blue Womb"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
    )

    connect(
        regions["Blue Womb"], regions["Void"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
        and state.has("Quality 4 Item", player, 1)
    )

    connect(
        regions["Depths 2"], regions["Alternate Mausoleum 2"], player,
        lambda state: (state.has("Polaroid", player) or state.has("Negative", player)
                       or state.has("Polaroid Acquired", player) or state.has("Negative Acquired", player))
        and state.has("Boss Item", player, 5) and state.has("Treasure Room Item", player, 4)
    )

    connect(
        regions["Alternate Mausoleum 2"], regions["Home"], player,
        lambda state: state.has("Dad's Note", player) or state.has("Dad's Note Acquired", player)
    )

    connect(
        regions["Alternate Mausoleum 2"], regions["Home"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
        and state.has("Quality 4 Item", player, 1)
    )

    connect(
        regions["Home"], regions["Beast"], player,
        lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
        and state.has("Quality 4 Item", player, 1)
    )

    connect(
        regions["Dark Room"], regions["Mega Satan"], player,
        lambda state: state.has("Key Piece 1", player) and state.has("Key Piece 2", player)
        or state.has("Key Piece 1 Acquired", player) and state.has("Key Piece 2 Acquired", player)
    )

    connect(
        regions["Chest"], regions["Mega Satan"], player,
        lambda state: state.has("Key Piece 1", player) and state.has("Key Piece 2", player)
        or state.has("Key Piece 1 Acquired", player) and state.has("Key Piece 2 Acquired", player)
    )

    # Angel/Devil

    connect(
        regions["Basement 2"], regions["Devil Room 1"], player,
        lambda state: True
    )

    connect(
        regions["Depths 1"], regions["Devil Room 2"], player,
        lambda state: True
    )

    connect(
        regions["Depths 1"], regions["Angel Room 1"], player,
        lambda state: True
    )

    connect(
        regions["Womb 1"], regions["Angel Room 2"], player,
        lambda state: True
    )

    connect(
        regions["Angel Room 1"], regions["Key Piece 1"], player,
        lambda state: True
    )

    connect(
        regions["Angel Room 2"], regions["Key Piece 2"], player,
        lambda state: True
    )

    # Shops/Planetarium

    connect(
        regions["Basement 2"], regions["Shop 1"], player,
        lambda state: True
    )

    connect(
        regions["Caves 1"], regions["Shop 2"], player,
        lambda state: True
    )

    connect(
        regions["Caves 2"], regions["Shop 3"], player,
        lambda state: True
    )

    connect(
        regions["Depths 1"], regions["Shop 4"], player,
        lambda state: True
    )

    connect(
        regions["Depths 2"], regions["Shop 5"], player,
        lambda state: True
    )

    connect(
        regions["Depths 2"], regions["Planetarium"], player,
        lambda state: True
    )


def create_regions_logic(multiworld: MultiWorld, player: int, locations: List[str], event_locations: List[str]):
    from . import create_region

    regions_to_locations = DefaultDict(lambda: [])
    regions_by_name = dict()

    for location in locations:
        real_location = logic_mode_locations[location]
        regions_to_locations.setdefault(real_location[1], []).append(location)

    for region_name in base_regions:
        new_region = create_region(multiworld, player, region_name, locations=regions_to_locations[region_name])
        regions_by_name[region_name] = new_region

    starting_region = create_region(multiworld, player, "Menu", None)

    starting_entrance = Entrance(player, "New Run", starting_region)
    starting_entrance.connect(regions_by_name["Basement 1"])

    multiworld.regions += [
        starting_region
    ]

    starting_region.exits.append(starting_entrance)

    connect_all_regions(multiworld, player, regions_by_name)

    for event_location in event_locations:
        real_location = logic_mode_locations[event_location[0]]
        region = regions_by_name[real_location[1]]
        region.locations.append(
            TheBindingOfIsaacRepentanceLocation(player, event_location[1], None, region)
        )

    multiworld.regions += regions_by_name.values()

    return
