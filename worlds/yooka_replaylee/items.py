from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ReplayleeWorld


class ItemData(NamedTuple):
    qty: int
    classification: ItemClassification


ITEM_NAME_TO_ID = {
    'Quill': 1,
    'Pagie': 2,
    'Glide': 3,
    'Q.U.I.D.': 4,
    'Tail Twirl': 5,
    'Invisibility': 6,
    'Aerial Tail Twirl': 7,
    'Sonar Shot': 8,
    'Sonar Boom': 9,
    'Roll': 11,
    'Elemental Fruits': 12,
    'Cloud Yooka': 13,
    'Wheel Spin Attack': 15,
    'Ground Pound': 17,
    'High Jump': 18,
    'Air Bubble': 19,
    'Tongue Grapple Hook': 20,
    'Wheel Dash Attack': 21,
    'Triple Pagie Medal': 22,
    'TT Quill': 23,
    'GlGl Quill': 24,
    'MM Quill': 25,
    'CC Quill': 26,
    'GaGa Quill': 27,
    'Golden Pagie': 28,
    'Progressive Pagie Door': 29,
    'Capital Key': 30,
    'Victory': 31,
}

MOVES = {
    'Tail Twirl': ItemData(1, ItemClassification.progression),
    'Glide': ItemData(1, ItemClassification.progression),
    'Invisibility': ItemData(1, ItemClassification.progression),
    'Aerial Tail Twirl': ItemData(1, ItemClassification.progression),
    'Sonar Shot': ItemData(1, ItemClassification.progression),
    'Sonar Boom': ItemData(1, ItemClassification.progression),
    'Roll': ItemData(1, ItemClassification.progression),
    'Elemental Fruits': ItemData(1, ItemClassification.progression),
    'Cloud Yooka': ItemData(1, ItemClassification.progression),
    'Wheel Spin Attack': ItemData(1, ItemClassification.progression),
    'Ground Pound': ItemData(1, ItemClassification.progression),
    'High Jump': ItemData(1, ItemClassification.progression),
    'Air Bubble': ItemData(1, ItemClassification.progression),
    'Tongue Grapple Hook': ItemData(1, ItemClassification.progression),
    'Wheel Dash Attack': ItemData(1, ItemClassification.progression),
}

SPECIAL_REWARDS = {
    'Triple Pagie Medal': ItemData(0, ItemClassification.progression),
    'Golden Pagie': ItemData(100, ItemClassification.progression),
    'Progressive Pagie Door': ItemData(4, ItemClassification.progression),
    'Capital Key': ItemData(0, ItemClassification.progression),
    'Victory': ItemData(0, ItemClassification.progression),
}

WORLD_QUILL_ITEMS = {
    'TT Quill': ItemData(150, ItemClassification.progression),
    'GlGl Quill': ItemData(150, ItemClassification.progression),
    'MM Quill': ItemData(150, ItemClassification.progression),
    'CC Quill': ItemData(150, ItemClassification.progression),
    'GaGa Quill': ItemData(150, ItemClassification.progression),
}

COLLECTIBLES = {
    'Quill': ItemData(150, ItemClassification.progression),
    'Pagie': ItemData(300, ItemClassification.progression),
    'Q.U.I.D.': ItemData(0, ItemClassification.filler),
}

ALL_ITEMS = {**MOVES, **COLLECTIBLES, **SPECIAL_REWARDS, **WORLD_QUILL_ITEMS}


class ReplayleeItem(Item):
    game = "Yooka-Replaylee"


def get_random_filler_item_name(world: ReplayleeWorld) -> str:
    return "Q.U.I.D."




def get_world_quill_item_names(world):
    """Return world-specific Quill items only when Quillsanity is enabled."""
    if world.options.quillsanity.value:
        return {"TT Quill", "GlGl Quill", "MM Quill", "CC Quill", "GaGa Quill"}
    return set()
def create_item_with_correct_classification(world: ReplayleeWorld, name: str) -> ReplayleeItem:
    data = ALL_ITEMS[name]
    return ReplayleeItem(name, data.classification, ITEM_NAME_TO_ID[name], world.player)


def create_event(world: ReplayleeWorld, name: str) -> ReplayleeItem:
    """Create a generation-only event item with no AP ID."""
    return ReplayleeItem(name, ItemClassification.progression, None, world.player)


def create_all_items(world: ReplayleeWorld) -> None:
    """Create the progression pool and fill all remaining item slots with Q.U.I.D."""
    itempool = [world.create_item(name) for name in MOVES]

    # Four progressive hub-door unlocks are always part of the pool.
    # 1/2/3/4 copies unlock the 15/35/55/75 Pagie doors respectively.
    itempool.extend(
        world.create_item("Progressive Pagie Door")
        for _ in range(SPECIAL_REWARDS["Progressive Pagie Door"].qty)
    )

    if world.options.quillsanity.value:
        itempool.extend(
            world.create_item(name)
            for name, data in WORLD_QUILL_ITEMS.items()
            for _ in range(data.qty)
        )

    if world.options.goal.value == 2:  # defeat_capital_b
        key_pool = world.options.capital_key_pool.value
        key_goal = world.options.capital_key_goal.value
        if key_goal > key_pool:
            raise ValueError(
                f"Capital Key Goal ({key_goal}) cannot exceed Capital Key Pool ({key_pool})."
            )
        itempool.extend(world.create_item("Capital Key") for _ in range(key_pool))

    if world.options.goal.value == 1:  # golden_pagie_hunt
        golden_pool = world.options.golden_pagie_pool.value
        golden_goal = world.options.golden_pagie_goal.value
        if golden_goal > golden_pool:
            raise ValueError(
                f"Golden Pagie Goal ({golden_goal}) cannot exceed Golden Pagie Pool ({golden_pool})."
            )
        itempool.extend(
            world.create_item("Golden Pagie")
            for _ in range(golden_pool)
        )

    needed_filler = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)
    if needed_filler < 0:
        raise ValueError("Yooka-Replaylee has more items than unfilled locations.")
    itempool.extend(world.create_filler() for _ in range(needed_filler))
    world.multiworld.itempool += itempool
