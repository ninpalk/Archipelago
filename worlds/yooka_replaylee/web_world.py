from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld


class ReplayleeWebWorld(WebWorld):
    game = "Yooka-Replaylee"
    theme = "grassFlowers"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Yooka-Replaylee for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["tommadness"],
    )

    tutorials = [setup_en]
