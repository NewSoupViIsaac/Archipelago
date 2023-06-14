from typing import Dict

from BaseClasses import MultiWorld


def determine_enabled_bosses(
        multiworld: MultiWorld, player: int, goal_only: bool = False, hard_required: bool = False
) -> Dict[str, bool]:
    goal = multiworld.goal[player]

    required_bosses = {
        "Mom": goal == 0,
        "Mom's Heart": goal == 1,
        "Isaac": goal == 2 or goal == 3,
        "Satan": goal == 2 or goal == 4,
        "Blue Baby": goal == 5 or goal == 6,
        "Lamb": goal == 5 or goal == 7,
        "Mega Satan": goal == 8,
        "Boss Rush": goal == 9,
        "Hush": goal == 10,
        "Beast": goal == 11 or goal == 12,
        "Mother": goal == 13,
        "Delirium": goal == 14,
        "Ultra Greed": False,
    }

    if goal_only:
        return required_bosses

    if goal == 16:  # Full Notes
        for k in required_bosses:
            required_bosses[k] = True
    elif goal == 17 and not hard_required:  # Note Marks
        amt_of_characters = 26  # Assuming that up to 8/34 characters are "disliked"
        required_note_marks = multiworld.note_marks_amount[player]
        needed_bosses = required_note_marks / amt_of_characters

        boss_difficulty_order = ["Mom's Heart",
                                 "Boss Rush",
                                 "Isaac", "Satan", "Blue Baby", "Lamb",
                                 "Hush",
                                 "Mega Satan",
                                 "Beast", "Mother",
                                 "Delirium",
                                 "Ultra Greed"]

        while sum(required_bosses.values()) < needed_bosses:
            required_bosses[boss_difficulty_order.pop()] = True

    return required_bosses
