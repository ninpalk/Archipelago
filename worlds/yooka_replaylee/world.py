from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from .options import ReplayleeOptions


class ReplayleeWorld(World):
    """Archipelago world implementation for Yooka-Replaylee."""

    game = "Yooka-Replaylee"
    web = web_world.ReplayleeWebWorld()

    options_dataclass = ReplayleeOptions
    options: ReplayleeOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Hivory Towers Entrance"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.ReplayleeItem:
        return items.create_item_with_correct_classification(self, name)

    def create_event(self, name: str) -> items.ReplayleeItem:
        return items.create_event(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "goal": self.options.goal.current_key,
            "triple_pagie_medal_goal": self.options.triple_pagie_medal_goal.value,
            "golden_pagie_goal": self.options.golden_pagie_goal.value,
            "golden_pagie_pool": self.options.golden_pagie_pool.value,
            "capital_key_pool": self.options.capital_key_pool.value,
            "capital_key_goal": self.options.capital_key_goal.value,
            "quillsanity": self.options.quillsanity.value,
        }
