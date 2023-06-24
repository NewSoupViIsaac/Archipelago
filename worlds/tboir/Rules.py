from typing import Callable, Dict

from BaseClasses import MultiWorld, CollectionState
from worlds.generic.Rules import set_rule, add_rule
from worlds.tboir.Utils import determine_enabled_bosses


def get_rules_lookup(player):
    return {
        "Mom": lambda state: state.has("Boss Item", player, 5) and state.has("Treasure Room Item", player, 5),
        "Mom's Heart": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5),
        "Alternate Mom's Heart": lambda state: state.has("Boss Item", player, 6)
                                               and state.has("Treasure Room Item", player, 5),
        "Satan": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                               and state.has("Quality 4 Item", player),
        "Isaac": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                               and state.has("Quality 4 Item", player),
        "Lamb": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                              and state.has("Quality 4 Item", player),
        "Blue Baby": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                                   and state.has("Quality 4 Item", player),
        "Dogma": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                                   and state.has("Quality 4 Item", player),
        "Beast": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                                   and state.has("Quality 4 Item", player),
        "Hush": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                               and state.has("Quality 4 Item", player),
        "Delirium": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                              and state.has("Quality 4 Item", player),
        "Ultra Greed": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                              and state.has("Quality 4 Item", player),
        "Mother": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                                     and state.has("Quality 4 Item", player),
        "Boss Rush": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                                and state.has("Quality 4 Item", player),
        "Mega Satan": lambda state: state.has("Boss Item", player, 6) and state.has("Treasure Room Item", player, 5)
                                   and state.has("Quality 4 Item", player),
    }


def beats_bosses(multiworld: MultiWorld, player: int, bosses: Dict[str, bool]) -> Callable[[CollectionState], bool]:
    bosses = [boss for boss, req in bosses.items() if req]
    return lambda state: not bosses or all([state.has(boss + " Beaten", player) for boss in bosses])


def set_rules(world: MultiWorld, player: int, progression_item_count: int, required_prog_item_factor: float):
    if world.logic_mode[player]:
        required_bosses = determine_enabled_bosses(world, player)
        world.completion_condition[player] = beats_bosses(world, player, required_bosses)

        rules_lookup = get_rules_lookup(player)

        for location in world.get_locations(player):
            name = location.name
            if name.endswith(" Beaten"):
                name = name[:-7]
                set_rule(location, rules_lookup[name])
                continue
            if name.endswith(" Acquired"):
                name = name[:-9]
            set_rule(location, rules_lookup.get(name, lambda state: True))
        return

    set_rule(world.get_location("Run End", player),
             lambda state: state.has(f"Progression Item", player,
                                     progression_item_count * required_prog_item_factor) and state.can_reach(
                 world.get_location(f"ItemPickup{world.required_locations[player].value}", player).parent_region))

    world.completion_condition[player] = lambda state: state.has("Victory", player)
