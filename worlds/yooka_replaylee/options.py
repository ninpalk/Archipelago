from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, Toggle


class Goal(Choice):
    """Select the victory condition used for this seed."""

    display_name = "Goal"
    option_triple_pagie_medal_hunt = 0
    option_golden_pagie_hunt = 1
    option_defeat_capital_b = 2
    default = 1


class TriplePagieMedalGoal(Range):
    """Number of Triple Pagie Medals required for Triple Pagie Medal Hunt."""

    display_name = "Triple Pagie Medal Goal"
    range_start = 1
    range_end = 10
    default = 5


class GoldenPagieGoal(Range):
    """Number of Golden Pagies required for Golden Pagie Hunt."""

    display_name = "Golden Pagie Goal"
    range_start = 1
    range_end = 300
    default = 150


class GoldenPagiePool(Range):
    """Number of Golden Pagies placed in the item pool for Golden Pagie Hunt."""

    display_name = "Golden Pagie Pool"
    range_start = 1
    range_end = 300
    default = 300


class CapitalKeyPool(Range):
    """Number of Capital Keys placed in the item pool for Defeat Capital B."""

    display_name = "Capital Key Pool"
    range_start = 1
    range_end = 300
    default = 300


class CapitalKeyGoal(Range):
    """Number of Capital Keys required to unlock Capital B for Defeat Capital B."""

    display_name = "Capital Key Goal"
    range_start = 1
    range_end = 300
    default = 150


class Quillsanity(Toggle):
    """Include all 750 individual Quill checks as Archipelago locations as well as 30 Trowzer shop locations + 5 checks for having all 150 quills. Adds 785 locations to the game"""

    display_name = "Quillsanity"
    default = 1


@dataclass
class ReplayleeOptions(PerGameCommonOptions):
    """Options for the Yooka-Replaylee Archipelago world."""

    goal: Goal
    triple_pagie_medal_goal: TriplePagieMedalGoal
    golden_pagie_goal: GoldenPagieGoal
    golden_pagie_pool: GoldenPagiePool
    capital_key_pool: CapitalKeyPool
    capital_key_goal: CapitalKeyGoal
    quillsanity: Quillsanity
