from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import ReplayleeWorld


def create_and_connect_regions(world: ReplayleeWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ReplayleeWorld) -> None:
    region_names = [
        "Hivory Towers Entrance",
        "Tribalstack Tropics Entrance",
        "Hivory Towers Bypass 15 Door",
        "Hivory Towers Bypass 35 Door",
        "Hivory Towers Bypass 55 Door",
        "Glitterglaze Glacier Entrance",
        "Moodymaze Marsh Entrance",
        "Capital Cashino Entrance",
        "Galleon Galaxy Entrance",
    ]

    world.multiworld.regions += [
        Region(name, world.player, world.multiworld)
        for name in region_names
    ]


def connect_regions(world: ReplayleeWorld) -> None:
    ht = world.get_region("Hivory Towers Entrance")
    tt = world.get_region("Tribalstack Tropics Entrance")
    hub_b = world.get_region("Hivory Towers Bypass 15 Door")
    hub_b2 = world.get_region("Hivory Towers Bypass 35 Door")
    hub_c = world.get_region("Hivory Towers Bypass 55 Door")
    gl = world.get_region("Glitterglaze Glacier Entrance")
    mm = world.get_region("Moodymaze Marsh Entrance")
    cc = world.get_region("Capital Cashino Entrance")
    ga = world.get_region("Galleon Galaxy Entrance")

    ht.connect(tt, "Hivory Towers to Tribalstack")
    ht.connect(hub_b, "Hivory Towers to Hub B")
    hub_b.connect(gl, "Hivory Towers Hub B to Glitterglaze")
    hub_b.connect(hub_b2, "Hivory Towers Hub B to Hub B Part 2")
    hub_b2.connect(mm, "Hivory Towers Hub B Part 2 to Moodymaze")
    hub_b2.connect(hub_c, "Hivory Towers Hub B Part 2 to Hub C")
    hub_c.connect(cc, "Hivory Towers Hub C to Cashino")
    hub_c.connect(ga, "Hivory Towers Hub C to Galleon")
