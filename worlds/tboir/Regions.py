from typing import Dict, Callable, List, Set
from typing_extensions import DefaultDict

from BaseClasses import Region, CollectionState, Entrance
from worlds.AutoWorld import World

from .Locations import logic_mode_locations, TheBindingOfIsaacRepentanceLocation

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
    "Angel Room 2",
    "Blue Womb",
    "Womb 1",
    "Womb 2",
    "Corpse 1",
    "Corpse 2",
    "Alternate Mom's Heart",
    "Alternate Mausoleum 2",
}


def can_advance(player: int, i_boss: int, i_treasure: int, quality_four: bool = False, extras: Set[str] = frozenset()):
    if quality_four:
        if extras:
            return lambda state: (
                state.has("Boss Item", player, i_boss)
                and state.has("Treasure Room Item", player, i_treasure)
                and state.has("Quality 4 Item", player)
                and all(state.has_any([extra, extra + " Acquired"], player) for extra in extras)
            )
        else:
            return lambda state: (
                    state.has("Boss Item", player, i_boss)
                    and state.has("Treasure Room Item", player, i_treasure)
                    and state.has("Quality 4 Item", player)
            )
    else:
        if extras:
            return lambda state: (
                state.has("Boss Item", player, i_boss)
                and state.has("Treasure Room Item", player, i_treasure)
                and all(state.has_any([extra, extra + " Acquired"], player) for extra in extras)
            )
        else:
            return lambda state: (
                state.has("Boss Item", player, i_boss)
                and state.has("Treasure Room Item", player, i_treasure)
            )


def connect_all_regions(world: World, regions: Dict[str, Region]):
    player = world.player

    # Meh

    regions["Basement 1"].connect(regions["Ultra Greed"])

    # Regular Path Down

    regions["Basement 1"].connect(regions["Basement 2"])
    regions["Basement 2"].connect(regions["Caves 1"], rule=can_advance(player, 2, 1))
    regions["Caves 1"].connect(regions["Caves 2"], rule=can_advance(player, 2, 1))
    regions["Caves 2"].connect(regions["Depths 1"], rule=can_advance(player, 4, 3))
    regions["Depths 1"].connect(regions["Depths 2"], rule=can_advance(player, 4, 3))
    regions["Depths 2"].connect(regions["Womb 1"], rule=can_advance(player, 5, 5))
    regions["Womb 1"].connect(regions["Womb 2"], rule=can_advance(player, 5, 5))
    regions["Womb 2"].connect(regions["Sheol"], rule=can_advance(player, 6, 5))
    regions["Womb 2"].connect(regions["Cathedral"], rule=can_advance(player, 6, 5))

    regions["Cathedral"].connect(regions["Chest"], rule=can_advance(player, 6, 5, True, {"Polaroid"}))
    regions["Sheol"].connect(regions["Dark Room"], rule=can_advance(player, 6, 5, True, {"Negative"}))

    # Alt Path

    regions["Basement 1"].connect(regions["Downpour 1"], rule=can_advance(player, 1, 1))
    regions["Basement 2"].connect(regions["Downpour 2"], rule=can_advance(player, 1, 1))
    regions["Caves 1"].connect(regions["Mines 1"], rule=can_advance(player, 3, 2))
    regions["Caves 2"].connect(regions["Mines 2"], rule=can_advance(player, 3, 2))
    regions["Depths 1"].connect(regions["Mausoleum 1"], rule=can_advance(player, 5, 4))

    regions["Downpour 1"].connect(regions["Downpour 2"], rule=can_advance(player, 1, 1))
    regions["Downpour 2"].connect(regions["Mines 1"], rule=can_advance(player, 3, 2))
    regions["Mines 1"].connect(regions["Mines 2"], rule=can_advance(player, 3, 2))
    regions["Mines 2"].connect(regions["Mausoleum 1"], rule=can_advance(player, 5, 4))
    regions["Mausoleum 1"].connect(regions["Mausoleum 2"], rule=can_advance(player, 5, 4))
    regions["Mausoleum 2"].connect(
        regions["Alternate Mom's Heart"],
        rule=can_advance(player, 5, 4, extras={"Knife Piece 1", "Knife Piece 2"})
    )
    regions["Alternate Mom's Heart"].connect(regions["Corpse 1"], rule=can_advance(player, 6, 5))
    regions["Corpse 1"].connect(regions["Corpse 2"], rule=can_advance(player, 6, 5))

    # Alt Bosses

    regions["Depths 2"].connect(regions["Boss Rush"], rule=can_advance(player, 5, 4))
    regions["Womb 2"].connect(regions["Blue Womb"], rule=can_advance(player, 6, 5))
    regions["Blue Womb"].connect(regions["Void"], rule=can_advance(player, 6, 5, True))

    regions["Depths 2"].connect(regions["Alternate Mausoleum 2"], rule=lambda state: (
        state.has_any(["Polaroid", "Polaroid Acquired", "Negative", "Negative Acquired"], player)
        and state.has("Boss Item", player, 5) and state.has("Treasure Room Item", player, 4)
    ))

    regions["Alternate Mausoleum 2"].connect(
        regions["Home"], rule=can_advance(player, 6, 5, True, {"Dad's Note"})
    )

    regions["Home"].connect(regions["Beast"], rule=can_advance(player, 6, 5, True))

    regions["Dark Room"].connect(regions["Mega Satan"], rule=lambda state: (
        state.has_any(["Key Piece 1", "Key Piece 1 Acquired"], player)
        and state.has_any(["Key Piece 2", "Key Piece 2 Acquired"], player)
    ))

    regions["Chest"].connect(regions["Mega Satan"], rule=lambda state: (
        state.has_any(["Key Piece 1", "Key Piece 1 Acquired"], player)
        and state.has_any(["Key Piece 2", "Key Piece 2 Acquired"], player)
    ))

    # Angel/Devil

    regions["Basement 2"].connect(regions["Devil Room 1"])
    regions["Depths 1"].connect(regions["Devil Room 2"])
    regions["Depths 1"].connect(regions["Angel Room 1"])
    regions["Womb 1"].connect(regions["Angel Room 2"])

    regions["Angel Room 1"].connect(regions["Key Piece 1"])
    regions["Angel Room 2"].connect(regions["Key Piece 2"])

    # Shops/Planetarium

    regions["Basement 2"].connect(regions["Shop 1"])
    regions["Caves 1"].connect(regions["Shop 2"])
    regions["Caves 2"].connect(regions["Shop 3"])
    regions["Depths 1"].connect(regions["Shop 4"])
    regions["Depths 2"].connect(regions["Shop 5"])
    regions["Depths 2"].connect(regions["Planetarium"])


def create_regions_logic(world: World, locations: List[str], event_locations: List[str]):
    from . import create_region

    regions_to_locations = DefaultDict(lambda: [])
    regions_by_name = dict()

    for location in locations:
        real_location = logic_mode_locations[location]
        regions_to_locations.setdefault(real_location[1], []).append(location)

    for region_name in base_regions:
        region_locations = regions_to_locations[region_name]
        new_region = create_region(world.multiworld, world.player, region_name, locations=region_locations)
        regions_by_name[region_name] = new_region

    starting_region = create_region(world.multiworld, world.player, "Menu", None)
    starting_region.connect(regions_by_name["Basement 1"], "New Run")

    world.multiworld.regions += [
        starting_region
    ]

    connect_all_regions(world, regions_by_name)

    for event_location in event_locations:
        real_location = logic_mode_locations[event_location[0]]
        region = regions_by_name[real_location[1]]
        region.locations.append(
            TheBindingOfIsaacRepentanceLocation(world.player, event_location[1], None, region)
        )

    world.multiworld.regions += regions_by_name.values()

    return
