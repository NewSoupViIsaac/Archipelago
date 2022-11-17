import typing
from Options import Option, DefaultOnToggle, Range, Choice, DeathLink, OptionDict
from worlds.tboir import default_weights, default_junk_items_weights, item_table
from worlds.tboir.Items import default_trap_items_weights


class TotalLocations(Range):
    """Number of location checks which are added."""
    display_name = "Total Locations"
    range_start = 10
    range_end = 500
    default = 100


class RequiredLocations(Range):
    """Number of location checks required to beat the game."""
    display_name = "Required Locations"
    range_start = 1
    range_end = 500
    default = 50


class Goal(Choice):
    """Goal to finish the run"""
    display_name = "Goal"
    option_mom = 0
    option_moms_heart = 1
    option_isaac_satan = 2
    option_isaac = 3
    option_satan = 4
    option_blue_baby_lamb = 5
    option_blue_baby = 6
    option_lamb = 7
    option_mega_satan = 8
    option_boss_rush = 9
    option_hush = 10
    option_dogma = 11
    option_beast = 12
    option_mother = 13
    option_delirium = 14
    option_required_locations = 15


class ItemPickupStep(Range):
    """Number of items to pick up before an AP Check is completed.
    Setting to 1 means every other pickup.
    Setting to 2 means every third pickup. So on..."""
    display_name = "Item Pickup Step"
    range_start = 1
    range_end = 5
    default = 1


class AdditonalBossRewards(DefaultOnToggle):
    """If enabled all goal bosses will reward additional checks.
    The amount of checks if determined on how deep the boss in the run:
    Mom = 1
    Mom's Heart/Boss Rush = 2
    Isaac/Satan/Hush = 3
    Blue Baby/The Lamb = 4
    Mega Satan/Mother/Beast/Delirium = 5
    exception:
    Dogma = 0
    """
    display_name = "Additional Boss Rewards"


class JunkPercentage(Range):
    """Percentage of junk items (Non-Collectable Pickups like Coins, Bombs etc.)"""
    display_name = "Junk Percentage"
    range_start = 0
    range_end = 100
    default = 0


class TrapPercentage(Range):
    """Replaces a percentage of junk items with traps"""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0


class TeleportTrapCanError(DefaultOnToggle):
    """Can a Teleport Trap teleport to an Error Room?"""
    display_name = "Teleport Trap can teleport to Error Room"


class ItemWeights(Choice):
    """Preset choices for determining the weights of the item pool."""
    display_name = "Item Weights"
    option_default = 0
    option_custom = 1


class CustomItemWeightsBase(OptionDict):
    verify_item_name = True

    def __init__(self, value: typing.Dict[str, int]):
        if len(value) <= 0:
            value = self.default
        if any(value < 0 for value in value.values()):
            raise Exception("Cannot have negative value.")
        if sum(value.values()) <= 0:
            raise Exception("Sum of all values cannot be non-positive")
        super(CustomItemWeightsBase, self).__init__(value)


class CustomItemWeights(CustomItemWeightsBase):
    """
    Put your custom item weights here. Format is item_name: weighting. Leave empty for default weighting.<br>These
    weights are only for progression items. For junk and trap items use Custom Junk Item Weights and Trap Item
    Weights.
    """
    verify_item_name = True
    display_name = "Custom Item Weights"
    default = default_weights

    def __init__(self, value: typing.Dict[str, int]):
        if any(not item_table[key].is_progression() for key in value.keys()):
            raise Exception("Cannot include non progression items")
        super(CustomItemWeights, self).__init__(value)


class CustomJunkItemWeights(CustomItemWeightsBase):
    """
    Put your custom junk item weights here. Format is item_name: weighting. Leave empty for default weighting.<br>These
    weights are only for junk items. For progression and trap items use Custom Item Weights and Trap Item
    Weights.
    """
    verify_item_name = True
    display_name = "Custom Junk Item Weights"
    default = default_junk_items_weights

    def __init__(self, value: typing.Dict[str, int]):
        if any(item_table[key].is_progression() for key in value.keys()):
            raise Exception("Cannot include progression items")
        if any(item_table[key].is_trap() for key in value.keys()):
            raise Exception("Cannot include trap items")
        super(CustomJunkItemWeights, self).__init__(value)


class TrapItemWeights(CustomItemWeightsBase):
    """
    Put your custom trap item weights here. Format is item_name: weighting. Leave empty for default weighting.<br>These
    weights are only for trap items. For progression and junk items use Custom Item Weights and Custom Junk Item
    Weights.
    """
    verify_item_name = True
    display_name = "Custom Trap Item Weights"
    default = default_trap_items_weights

    def __init__(self, value: typing.Dict[str, int]):
        if any(not item_table[key].is_trap() for key in value.keys()):
            raise Exception("Cannot include non trap items")
        super(TrapItemWeights, self).__init__(value)


tobir_options: typing.Dict[str, type(Option)] = {
    "total_locations": TotalLocations,
    "required_locations": RequiredLocations,
    "item_pickup_step": ItemPickupStep,
    "goal": Goal,
    "item_weights": ItemWeights,
    "custom_item_weights": CustomItemWeights,
    "junk_percentage": JunkPercentage,
    "custom_junk_item_weights": CustomJunkItemWeights,
    "trap_percentage": TrapPercentage,
    "trap_item_weights": TrapItemWeights,
    "teleport_trap_can_error": TeleportTrapCanError,
    "additional_boss_rewards": AdditonalBossRewards,
    "death_link": DeathLink,
}