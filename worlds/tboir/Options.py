import typing
from Options import Option, DefaultOnToggle, Toggle, Range, Choice, DeathLink, OptionDict, AssembleOptions, SpecialRange
from .Items import default_trap_items_weights, default_weights, default_junk_items_weights, item_table


class TotalLocations(Range):
    """Number of location checks which are added."""
    display_name = "Total Locations"
    range_start = 10
    range_end = 500
    default = 125


class RequiredLocations(Range):
    """Number of location checks required to beat the game."""
    display_name = "Required Locations"
    range_start = 1
    range_end = 500
    default = 75


class Goal(Choice):
    """Goal to finish the run. Note that note marks and full notes do include the Cent Sign note mark as greed mode is
    not supported yet. """
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
    option_full_notes = 16
    option_note_marks = 17
    default = 5


class NoteMarkAmount(Range):
    """Number of note marks needed to beat the game (if goal is note marks). """
    display_name = "Full Note Amount"
    range_start = 1
    range_end = 374
    default = 20


class FullNoteAmount(Range):
    """Number of full notes needed to beat the game (if goal is full notes).  """
    display_name = "Full Note Amount"
    range_start = 1
    range_end = 34
    default = 1


class NoteMarksRequireHardMode(Toggle):
    """If set on Note Marks are only considered complete if the run was on hard mode.
    Relevant for both full notes and note marks goal"""
    display_name = "Note marks require hard mode"


class LogicMode(Toggle):
    """In Logic Mode, locations are tied to areas.
    This means you will have to venture further into any singular run to get the "later" locations.
    You will not be asked to go far into the game until you receive enough items to beat the harder floors."""
    display_name = "Logic Mode"


class FurthestLocations(SpecialRange):
    """Only relevant for Logic Mode.
    This determines how far you have to go into the game to clear locations and send items.
    You may still be required to go further than this to beat your goal.
    The floors in brackets are only required if their specific mode is activated."""
    display_name = "Furthest Locations"
    range_start = 0
    range_end = 3
    special_range_names = {
        "Depths, (Mausoleum)": 0,
        "Womb, Corpse, (Blue Womb)": 1,
        "Sheol, Cathedral": 2,
        "Chest, Dark Room, (Void, Isaac's House)": 3
    }


class AlternatePath(Toggle):
    """Requires you to go through the alternate path, starting with Downpour, for extra location checks."""
    display_name = "Alternate Path"


class ExtraBosses(Toggle):
    """Only relevant for Logic Mode.
    Adds defeating Boss Rush, Hush, Beast, Delirium, and Mega Satan, and Mother to the location pool.
    The "Furthest Locations" and "Alternate Path" settings influence which bosses are added."""
    display_name = "Extra Bosses"


class ShopChecks(Toggle):
    """Only relevant for Logic Mode.
    Requires you to buy Shop items for additional location checks."""
    display_name = "Shop Checks"


class PlanetariumCheck(Toggle):
    """Only relevant for Logic Mode.
    Adds a single location check for finding a Planetarium."""
    display_name = "Planetarium Check"


class AngelDevilChecks(Toggle):
    """Only relevant for Logic Mode.
    Adds several location checks for finding items at Angel or Devil Rooms.
    Note that it may be possible that you have to go to Angel Rooms for Key Pieces even if this setting is off."""
    display_name = "Angel/Devil Room Checks"


class ItemPickupStep(Range):
    """Number of items to pick up before an AP Check is completed.
    Setting to 1 means every pickup,
    Setting to 2 means every other pickup,
    Setting to 3 means every third pickup and so on..."""
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
    default = 75


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
    option_custom = 99


class CustomItemWeightsBase(OptionDict):

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
    Put your custom item weights here. Format is item_name: weighting. Leave empty for default weighting. These
    weights are only for progression items. For junk and trap items use Custom Junk Item Weights and Trap Item
    Weights.
    """
    display_name = "Custom Item Weights"
    default = default_weights
    valid_keys = {key for (key, value) in item_table.items() if value.is_progression()}


class CustomJunkItemWeights(CustomItemWeightsBase):
    """
    Put your custom junk item weights here. Format is item_name: weighting. Leave empty for default weighting. These
    weights are only for junk items. For progression and trap items use Custom Item Weights and Trap Item
    Weights.
    """
    display_name = "Custom Junk Item Weights"
    default = default_junk_items_weights
    valid_keys = {key for key, value in item_table.items() if value.is_filler()}


class TrapItemWeights(CustomItemWeightsBase):
    """
    Put your custom trap item weights here. Format is item_name: weighting. Leave empty for default weighting. These
    weights are only for trap items. For progression and junk items use Custom Item Weights and Custom Junk Item
    Weights.
    """
    display_name = "Custom Trap Item Weights"
    default = default_trap_items_weights
    valid_keys = {key for key, value in item_table.items() if value.is_trap()}


class SplitStartItems(Choice):
    """
    Will split items already received on run start to be received over multiple floors.
    This is to avoid getting to many items early and make runs more interesting.
    Always 6 will always divide items over the first 6 floors.
    Furthest will base the division on your furthest run so far.
    """
    display_name = "Split Items received on start"
    option_off = 0
    option_on_always_6 = 1
    option_on_furthest = 2


tobir_options: typing.Dict[str, AssembleOptions] = {
    "total_locations": TotalLocations,
    "required_locations": RequiredLocations,
    "item_pickup_step": ItemPickupStep,
    "goal": Goal,
    "full_note_amount": FullNoteAmount,
    "note_marks_amount": NoteMarkAmount,
    "note_marks_require_hard_mode": NoteMarksRequireHardMode,
    "logic_mode": LogicMode,
    "furthest_locations": FurthestLocations,
    "alternate_path": AlternatePath,
    "extra_bosses": ExtraBosses,
    "shop_checks": ShopChecks,
    "planetarium_check": PlanetariumCheck,
    "angel_devil_checks": AngelDevilChecks,
    "item_weights": ItemWeights,
    "custom_item_weights": CustomItemWeights,
    "junk_percentage": JunkPercentage,
    "custom_junk_item_weights": CustomJunkItemWeights,
    "trap_percentage": TrapPercentage,
    "trap_item_weights": TrapItemWeights,
    "teleport_trap_can_error": TeleportTrapCanError,
    "additional_boss_rewards": AdditonalBossRewards,
    "death_link": DeathLink,
    "split_start_items": SplitStartItems,
}
