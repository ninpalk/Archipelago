from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule

from . import items

if TYPE_CHECKING:
    from .world import ReplayleeWorld
    
def set_all_rules(world: ReplayleeWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def has_move(state, move: str, player: int) -> bool:
    return state.has(move, player)


def has_all_moves(state, moves: list[str], player: int) -> bool:
    return state.has_all(moves, player)


def has_any_move(state, moves: list[str], player: int) -> bool:
    return state.has_any(moves, player)


# ============================================================
# REGION / ENTRANCE LOGIC
# ============================================================

def set_all_entrance_rules(world: ReplayleeWorld) -> None:

    # --------------------------------------------------------
    # Hivory Towers -> Bypass 15 Door
    # --------------------------------------------------------

    set_rule(
        world.get_entrance("Hivory Towers to Hub B"),
        lambda state: state.has("Roll", world.player)
        and state.has("Progressive Pagie Door", world.player, 1),
    )

    # --------------------------------------------------------
    # Bypass 15 -> Bypass 35
    # --------------------------------------------------------

    set_rule(
        world.get_entrance("Hivory Towers Hub B to Hub B Part 2"),
        lambda state: state.has("Air Bubble", world.player)
        and state.has("Progressive Pagie Door", world.player, 2),
    )

    # --------------------------------------------------------
    # Bypass 35 -> Moodymaze Marsh
    # --------------------------------------------------------
    set_rule(
        world.get_entrance("Hivory Towers Hub B Part 2 to Moodymaze"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
    )
    # --------------------------------------------------------
    # Bypass 35 -> Bypass 55
    # --------------------------------------------------------
    set_rule(
        world.get_entrance("Hivory Towers Hub B Part 2 to Hub C"),
        lambda state: state.has("Tongue Grapple Hook", world.player)
        and state.has("Progressive Pagie Door", world.player, 3),
    )

    # --------------------------------------------------------
    # Bypass 55 -> Capital Cashino
    # --------------------------------------------------------

    set_rule(
        world.get_entrance("Hivory Towers Hub C to Cashino"),
        lambda state: state.has("Invisibility", world.player)
        and state.has("Progressive Pagie Door", world.player, 3),
    )  
    # --------------------------------------------------------
    # Bypass 55 -> Galleon Galaxy
    # --------------------------------------------------------

    set_rule(
        world.get_entrance("Hivory Towers Hub C to Galleon"),
        lambda state: state.has("Cloud Yooka", world.player)
        and state.has("Progressive Pagie Door", world.player, 4),
    )

# ============================================================
# INDIVIDUAL LOCATION LOGIC
# ============================================================

def set_all_location_rules(world: ReplayleeWorld) -> None:

    # --------------------------------------------------------
    # Hivory Towers
    # --------------------------------------------------------

    if world.options.goal.value == 2:
        set_rule(
            world.get_location("HT - Capital Beaten"),
            lambda state: state.has("Progressive Pagie Door", world.player, 4)
            and state.has("Tail Twirl", world.player)
            and state.has("Glide", world.player)
            and state.has("Cloud Yooka", world.player)
            and state.has("Tongue Grapple Hook", world.player)
            and state.has("Air Bubble", world.player)
            and state.has("Roll", world.player)
            and state.has("Capital Key", world.player, world.options.capital_key_goal.value),
        )


    set_rule(
        world.get_location("HT - Aquatic Circuit"),
        lambda state: state.has("Air Bubble", world.player),
    )
    set_rule(
        world.get_location("HT - Briney Box"),
        lambda state: state.has("Tail Twirl", world.player),
    )
    set_rule(
        world.get_location("HT - Bunged Up Buddy"),
        lambda state: state.has("Ground Pound", world.player),
    )
    set_rule(
        world.get_location("HT - Butterfright!"),
        lambda state: state.has("Ground Pound", world.player),
    )
    set_rule(
        world.get_location("HT - Downwards Dash"),
        lambda state: state.has("Roll", world.player),
    )
    set_rule(
        world.get_location("HT - Mastered"),
        lambda state: state.has("High Jump", world.player),
    )
    set_rule(
        world.get_location("HT - Bonanza Bridge"),
        lambda state: has_all_moves(state, ["Roll", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("HT - Gold Standard"),
        lambda state: state.has("Glide", world.player),
    )
    set_rule(
        world.get_location("HT - Firefighter"),
        lambda state: has_all_moves(state, ["Elemental Fruits", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("HT - P.A.G.I.E"),
        lambda state: has_all_moves(state, ["Elemental Fruits", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("HT - Pipe Panes"),
        lambda state: has_all_moves(state, ["Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("HT - Sunken Salvage"),
        lambda state: state.has("Tail Twirl", world.player),
    )
    set_rule(
        world.get_location("HT - Fixer Upper"),
        lambda state: has_all_moves(state, ["High Jump", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("HT - Plumbing Plunder"),
        lambda state: state.has("Ground Pound", world.player),
    )
    set_rule(
        world.get_location("HT - Picture Perfect"),
        lambda state: state.has("Tail Twirl", world.player),
    )
    set_rule(
        world.get_location("HT - Busted Barrel"),
        lambda state: state.has("Tail Twirl", world.player),
    )
    set_rule(
        world.get_location("HT - Treasure Trouble"),
        lambda state: state.has("Tail Twirl", world.player),
    )
    set_rule(
        world.get_location("HT - Curious Cap"),
        lambda state: state.has("High Jump", world.player),
    )
    set_rule(
        world.get_location("HT - Cool and Collected"),
        lambda state: state.has("High Jump", world.player),
    )
    set_rule(
        world.get_location("HT - Shrubbery Sneak"),
        lambda state: state.has("Tail Twirl", world.player),
    )
    set_rule(
        world.get_location("HT - Wind Test"),
        lambda state: has_all_moves(state, ["Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("HT - Slide Ride"),
        lambda state: state.has("Ground Pound", world.player),
    )
    set_rule(
        world.get_location("HT - Page Turner"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
    )
    set_rule(
        world.get_location("HT - Booksmart"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
    )
    set_rule(
        world.get_location("HT - Sentry Skipper"),
        lambda state: state.has("Cloud Yooka", world.player),
    )
    set_rule(
        world.get_location("HT - Container Tower"),
        lambda state: state.has("Tail Twirl", world.player),
    )
    set_rule(
        world.get_location("HT - Poison Protection"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka"], world.player),
    )
    set_rule(
        world.get_location("HT - Rocky Rumble"),
        lambda state: state.has("Ground Pound", world.player),
    )
    set_rule(
        world.get_location("HT - Maestro Managed"),
        lambda state: state.has("Ground Pound", world.player),
    )
    set_rule(
        world.get_location("HT - Camera Shy"),
        lambda state: state.has("Invisibility", world.player),
    )
    set_rule(
        world.get_location("HT - Wind Test"),
        lambda state: has_all_moves(state, ["Roll", "Wheel Spin Attack"], world.player),
    )
    # --------------------------------------------------------
    # Tribalstack Tropics
    # --------------------------------------------------------
    set_rule(
        world.get_location("TT - Pagie Piece 4"),
        lambda state: state.has("Tail Twirl", world.player),
    )
    set_rule(
        world.get_location("TT - Pagie Piece 2"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
    )
    set_rule(
        world.get_location("TT - Pagie Piece 6"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
    )
    set_rule(
        world.get_location("TT - Pagie Piece 7"),
        lambda state: state.has("Elemental Fruits", world.player),
    )
    set_rule(
        world.get_location("TT - Pagie Piece 3"),
        lambda state: state.has("Roll", world.player),
    )
    set_rule(
        world.get_location("TT - Pagie Piece 1"),
        lambda state: has_all_moves(state, ["High Jump", "Glide"], world.player),
    )
    set_rule(
        world.get_location("TT - Pagie Piece 5"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("TT - Pagie Piece 8"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka", "Sonar Shot"], world.player),
    )
    set_rule(
        world.get_location("TT - Dino Score"),
        lambda state: state.has("Roll", world.player),
    )
    set_rule(
        world.get_location("TT - Wild Hog Chase"),
        lambda state: state.has("High Jump", world.player),
    )
    set_rule(
        world.get_location("TT - Get It Together"),
        lambda state: state.has("Tail Twirl", world.player),
    )
    set_rule(
        world.get_location("TT - Temple Treasure"),
        lambda state: state.has("Roll", world.player),
    )
    set_rule(
        world.get_location("TT - Rolling Goaling"),
        lambda state: state.has("Roll", world.player),
    )
    set_rule(
        world.get_location("TT - Duke It Out!"),
        lambda state: state.has("Elemental Fruits", world.player),
    )
    set_rule(
        world.get_location("TT - Seeing Green"),
        lambda state: state.has("Roll", world.player),
    )
    set_rule(
        world.get_location("TT - Tile Wiles"),
        lambda state: state.has("Ground Pound", world.player),
    )
    set_rule(
        world.get_location("TT - Kartos (Bronze)"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
    )
    set_rule(
        world.get_location("TT - Kartos (Silver)"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
    )
    set_rule(
        world.get_location("TT - Kartos (Gold)"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
    )
    set_rule(
        world.get_location("TT - Hidden High-jinks!"),
        lambda state: state.has("Sonar Shot", world.player),
    )
    # set_rule(
    #    world.get_location("TT - Flower Shower"),
    #    lambda state: has_all_moves(state, ["Sonar Shot", "Glide", "High Jump"], world.player),
    #)
    set_rule(
        world.get_location("TT - Riverbed Race"),
        lambda state: has_all_moves(state, ["Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("TT - Chilled Out Contest"),
        lambda state: has_all_moves(state, ["Roll", "Wheel Spin Attack", "Elemental Fruits", "High Jump", "Cloud Yooka"], world.player),
    )
    set_rule(
        world.get_location("TT - Sonar So Good"),
        lambda state: state.has("Sonar Shot", world.player),
    )
    set_rule(
        world.get_location("TT - Scorching Shuffle"),
        lambda state: has_all_moves(state, ["Roll", "Glide", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("TT - Soaring Success"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("TT - Hot Water"),
        lambda state: state.has("Elemental Fruits", world.player),
    )
    set_rule(
        world.get_location("TT - Target Time"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("TT - Sideways Shuffle"),
        lambda state: has_all_moves(state, ["Sonar Shot", "Glide", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("TT - Noisy Note"),
        lambda state: has_all_moves(state, ["Roll", "High Jump", "Cloud Yooka"], world.player),
    )
    set_rule(
        world.get_location("TT - Suspicious Summit"),
        lambda state: has_all_moves(state, ["Roll", "High Jump", "Cloud Yooka"], world.player),
    )
    set_rule(
        world.get_location("TT - Up and Down Showdown"),
        lambda state: has_all_moves(state, ["Roll", "High Jump", "Cloud Yooka", "Glide"], world.player),
    )
    set_rule(
        world.get_location("TT - Basement Bother"),
        lambda state: has_all_moves(state, ["Roll", "Ground Pound", "Invisibility"], world.player),
    )
    set_rule(
        world.get_location("TT - Feeling Thirsty"),
        lambda state: has_all_moves(state, ["Roll", "High Jump", "Cloud Yooka", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("TT - Blastooie Buddy-up"),
        lambda state: has_all_moves(state, ["Roll", "High Jump", "Cloud Yooka", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("TT - Submerged Souvenir"),
        lambda state: state.has("Air Bubble", world.player),
    )
    set_rule(
        world.get_location("TT - Weighting It Out"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka"], world.player),
    )
    set_rule(
        world.get_location("TT - Underwater Maze"),
        lambda state: state.has("Air Bubble", world.player),
    )
    set_rule(
        world.get_location("TT - Cameo Quest"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Elemental Fruits", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("TT - Idol Ascent"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Elemental Fruits", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("TT - Rampo's Rampagie"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Boom"], world.player),
    )
    set_rule(
        world.get_location("TT - Grand Tome Ghosts"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Glide", "Elemental Fruits", "Tongue Grapple Hook", "High Jump", "Cloud Yooka"], world.player),
    )
    # --------------------------------------------------------
    # Glitterglaze Glacier
    # --------------------------------------------------------
    set_rule(
        world.get_location("GlGl - Pagie Piece 7"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Glide", "Tongue Grapple Hook"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Pagie Piece 5"),
        lambda state: has_all_moves(state, ["Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Pagie Piece 2"),
        lambda state: has_all_moves(state, ["Roll", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Pagie Piece 4"),
        lambda state: has_all_moves(state, ["Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Pagie Piece 3"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Pagie Piece 8"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Pagie Piece 6"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Haggard Headwear"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Herding Hat"),
        lambda state: has_all_moves(state, ["Roll", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Awesome Arrr-tefact"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Pants, Very Much"),
        lambda state: has_all_moves(state, ["Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Freezing Flight"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Crystal Clear"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Burning Beacons"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Glacial Glide"),
        lambda state: has_all_moves(state, ["Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Blowie Bother"),
        lambda state: has_all_moves(state, ["Roll", "Glide", "High Jump", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Bombs Away"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Capital Block"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Artic Artist"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Grotto Winner"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Coin Clearer"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Cliffside Chest"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Tail Twirl", "Cloud Yooka"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Village Snowdown"),
        lambda state: has_all_moves(state, ["Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Moving Mayhem"),
        lambda state: has_all_moves(state, ["Roll", "High Jump", "Sonar Shot"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Rextro (Bronze)"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Rextro (Silver)"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Rextro (Gold)"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Jellyfishtery"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound", "Air Bubble", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Fizzics Puzzle"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound", "Air Bubble", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Chilly Target"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Incredible Quiz"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Ice-Scape"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Worrying Walls"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Toxic Trouble"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Keepy Uppy"),
        lambda state: has_all_moves(state, ["Roll", "Glide", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Chilly Combat"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Snowball Scramble"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound", "Sonar Shot"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Precarious Pipes"),
        lambda state: has_all_moves(state, ["Roll", "Glide", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Brrreeze Blocked"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits", "Ground Pound", "Sonar Shot"], world.player),
    )
    set_rule(
        world.get_location("GlGl - Grand Tome Ghosts"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Glide", "Elemental Fruits"], world.player),
    )
    # --------------------------------------------------------
    # Moodymaze Marsh
    # --------------------------------------------------------
    set_rule(
        world.get_location("MM - Pagie Piece 2"),
        lambda state: has_all_moves(state, ["Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("MM - Pagie Piece 3"),
        lambda state: has_all_moves(state, ["Roll", "Ground Pound", "Glide"], world.player),
    )
    set_rule(
        world.get_location("MM - Pagie Piece 4"),
        lambda state: has_all_moves(state, ["Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("MM - Pagie Piece 5"),
        lambda state: has_all_moves(state, ["Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("MM - Pagie Piece 6"),
        lambda state: has_all_moves(state, ["Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("MM - Pagie Piece 7"),
        lambda state: has_all_moves(state, ["Roll", "Ground Pound", "Glide"], world.player),
    )
    set_rule(
        world.get_location("MM - Pagie Piece 8"),
        lambda state: has_all_moves(state, ["Roll", "Ground Pound", "Glide"], world.player),
    )
    set_rule(
        world.get_location("MM - Curled Up Course"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Off-Road Reward"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Floating Folly"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("MM - Kartos (Bronze)"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Kartos (Silver)"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Kartos (Gold)"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Rextro (Bronze)"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Rextro (Silver)"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Rextro (Gold)"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Maze Up!"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Tongue Grapple Hook"], world.player),
    )
    set_rule(
        world.get_location("MM - Ollie's Moving Maze"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Letting Off Steam"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Toadstool Destruction"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Marsh Match"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Tongue Grapple Hook"], world.player),
    )
    set_rule(
        world.get_location("MM - Lash Chance"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Tongue Grapple Hook"], world.player),
    )
    set_rule(
        world.get_location("MM - Incredibubble!"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Current Commotion"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    #set_rule(
    #    world.get_location("MM - An A-maze-ing Time"),
    #    lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    #)
    set_rule(
        world.get_location("MM - Toasty Traversal"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Tongue Grapple Hook"], world.player),
    )
    set_rule(
        world.get_location("MM - Pressure Timer"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Jack's Jaunt"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Tongue Grapple Hook"], world.player),
    )
    set_rule(
        world.get_location("MM - Jack Again"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Tongue Grapple Hook"], world.player),
    )
    set_rule(
        world.get_location("MM - Fog-otten Treasure"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Fungi Fun"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Cephalopod Circuit"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Hardheaded"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("MM - Fairy Ring Fun"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Glide"], world.player),
    )
    set_rule(
        world.get_location("MM - Suspicious Stone"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("MM - Pipe Down"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Lantern Lark"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Aerial Tail Twirl", "Glide"], world.player),
    )
    set_rule(
        world.get_location("MM - Thorn Free"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Sunken Sewer"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Shoal Business"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Aerial Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("MM - Emergency Stash"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("MM - Swamp Station Situation"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("MM - Rope Burn"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("MM - Tentacle Test"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("MM - Grand Tome Ghosts"),
        lambda state: has_all_moves(state, ["Tail Twirl", "Air Bubble", "Sonar Boom", "Roll", "Glide", "Elemental Fruits"], world.player),
    )
    # --------------------------------------------------------
    # Capital Cashino
    # -------------------------------------------------------- 
    set_rule(
        world.get_location("CC - Casino Token 101"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 102"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 103"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 104"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 105"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 21"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 22"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 23"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 24"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 25"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 26"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 27"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 28"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 29"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 30"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 66"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 67"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 68"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 69"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 70"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 71"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 72"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 73"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 74"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 75"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 76"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 77"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 78"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 79"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 80"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 1"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 2"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 3"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 4"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 5"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 81"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 82"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 83"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 84"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 85"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 51"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 52"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 53"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 54"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 55"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 56"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 57"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 58"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 59"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 60"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 105"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 106"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 107"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 108"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 109"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 110"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 111"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 112"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 113"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 114"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 115"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 116"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 117"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 118"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 119"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 120"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 121"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 122"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 123"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 124"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 125"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 126"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 127"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 128"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 129"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 130"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 131"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 132"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 133"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 134"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 135"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 10"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 11"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 12"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 13"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 14"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 15"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 16"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 17"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 18"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 19"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 20"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 96"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 97"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 98"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 99"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 100"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "High Jump", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 6"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 7"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 8"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 9"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 10"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 141"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 142"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 143"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 144"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 145"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 36"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Tail Twirl", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 37"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Tail Twirl", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 38"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Tail Twirl", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 39"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Tail Twirl", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Casino Token 40"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Tail Twirl", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Pagie Piece 1"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide"], world.player),
    )
    set_rule(
        world.get_location("CC - Pagie Piece 3"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Glide", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Pagie Piece 4"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Pagie Piece 8"),
        lambda state: has_all_moves(state,["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("CC - Kartos (Bronze)"),
        lambda state: has_all_moves(state,["Invisibility", "Ground Pound", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Kartos (Silver)"),
        lambda state: has_all_moves(state,["Invisibility", "Ground Pound", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Kartos (Gold)"),
        lambda state: has_all_moves(state,["Invisibility", "Ground Pound", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Rextro (Bronze)"),
        lambda state: has_all_moves(state,["Invisibility", "Ground Pound", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Rextro (Silver)"),
        lambda state: has_all_moves(state,["Invisibility", "Ground Pound", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Rextro (Gold)"),
        lambda state: has_all_moves(state,["Invisibility", "Ground Pound", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - I.N.E.P.T. Derailed"),
        lambda state: has_all_moves(state, ["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("CC - Grand Tome Ghosts"),
        lambda state: has_all_moves(state, ["Invisibility", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump", "Wheel Spin Attack", "Elemental Fruits"], world.player),
    )
    # --------------------------------------------------------
    # Galleon Galaxy
    # --------------------------------------------------------  
    set_rule(
        world.get_location("GaGa - Pagie Piece 4"),
        lambda state: has_all_moves(state,["Sonar Shot", "Tongue Grapple Hook", "Air Bubble", "Roll", "Cloud Yooka"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Pagie Piece 5"),
        lambda state: has_all_moves(state,["Tongue Grapple Hook", "Air Bubble", "Roll", "Cloud Yooka", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Pagie Piece 2"),
        lambda state: has_all_moves(state,["Tongue Grapple Hook", "Air Bubble", "Roll", "Cloud Yooka", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Pagie Piece 6"),
        lambda state: has_all_moves(state,["Tongue Grapple Hook", "Air Bubble", "Roll", "Cloud Yooka", "Sonar Shot"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Pagie Piece 3"),
        lambda state: has_all_moves(state,["Tongue Grapple Hook", "Air Bubble", "Roll", "Cloud Yooka", "Tail Twirl", "Elemental Fruits"], world.player),
    )        
    set_rule(
        world.get_location("GaGa - Calcified Castaway"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Galactic Gold"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GaGa - A Race in Space"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Tidal Targets"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Galactic Golfing"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Ground Pound", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Ramped Up Rock"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Lightspeed Clamber"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Return Orbit"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Unstable Station"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Fish in a Barrel"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Defrost Flight"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Balloon Bust"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Sonar Shot"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Strongman Slam"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Island Hoop Hop"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Castaway Treasure"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Piggy Bank Yank"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Invisibility", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Rextro (Bronze)"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Rextro (Silver)"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Rextro (Gold)"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Kartos (Bronze)"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Kartos (Silver)"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Kartos (Gold)"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Gravity Grab"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Cowardly Captain"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Tail Twirl"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Shipshape"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Robot Robbery"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Anti-gravity Antics"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Superspeed Slide"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Superspeed Special"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Ground Pound"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Star Fishing"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Star Fish Flash"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Charged Up Colossus"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "High Jump", "Cloud Yooka", "Elemental Fruits"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Schell Game"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Cloud Yooka", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Raising Schell"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Cloud Yooka", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Toilet Trouble"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Cloud Yooka", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Shockball Shuffle"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Cloud Yooka", "Wheel Spin Attack"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Malicious Moon"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll"], world.player),
    )
    set_rule(
        world.get_location("GaGa - Grand Tome Ghosts"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Tongue Grapple Hook", "Air Bubble", "Sonar Boom", "Roll", "Elemental Fruits", "Tail Twirl", "High Jump"], world.player),
    )
    # --------------------------------------------------------
    # Quillsanity - Tribalstack Tropics
    # --------------------------------------------------------
    # These are the original individually-authored TT Quill rules.
    # They are only installed when Quillsanity is enabled.
    if world.options.quillsanity.value:
        set_rule(
        world.get_location("TT - Shop 1"),
        lambda state: state.has("TT Quill", world.player, 15),
        )
        set_rule(
        world.get_location("TT - Shop 2"),
        lambda state: state.has("TT Quill", world.player, 40),
        )
        set_rule(
        world.get_location("TT - Shop 3"),
        lambda state: state.has("TT Quill", world.player, 65),
        )
        set_rule(
        world.get_location("TT - Shop 4"),
        lambda state: state.has("TT Quill", world.player, 90),
        )
        set_rule(
        world.get_location("TT - Shop 5"),
        lambda state: state.has("TT Quill", world.player, 130),
        )
        set_rule(
        world.get_location("TT - Shop 6"),
        lambda state: state.has("TT Quill", world.player, 150),
        )
        set_rule(
        world.get_location("TT - Collect all the Quills"),
        lambda state: state.has("TT Quill", world.player, 150),
        )
        set_rule(
        world.get_location("TT - Quill 122"),
        lambda state: state.has("Roll", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 135"),
        lambda state: state.has("Roll", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 13"),
        lambda state: state.has("Roll", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 127"),
        lambda state: state.has("Roll", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 130"),
        lambda state: state.has("Roll", world.player),
        )    
        set_rule(
        world.get_location("TT - Quill 57"),
        lambda state: state.has("Roll", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 40"),
        lambda state: state.has("Roll", world.player),
        )    
        set_rule(
        world.get_location("TT - Quill 62"),
        lambda state: state.has("Roll", world.player),
        )    
        set_rule(
        world.get_location("TT - Quill 5"),
        lambda state: state.has("Glide", world.player),
        )      
        set_rule(
        world.get_location("TT - Quill 61"),
        lambda state: state.has("Glide", world.player),
        )      
        set_rule(
        world.get_location("TT - Quill 145"),
        lambda state: state.has("Glide", world.player),
        )   
        set_rule(
        world.get_location("TT - Quill 55"),
        lambda state: state.has("Glide", world.player),
        )          
        set_rule(
        world.get_location("TT - Quill 23"),
        lambda state: state.has("Glide", world.player),
        )          
        set_rule(
        world.get_location("TT - Quill 43"),
        lambda state: state.has("Glide", world.player),
        )          
        set_rule(
        world.get_location("TT - Quill 2"),
        lambda state: state.has("Glide", world.player),
        )      
        set_rule(
        world.get_location("TT - Quill 1"),
        lambda state: state.has("Elemental Fruits", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 114"),
        lambda state: state.has("Elemental Fruits", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 27"),
        lambda state: state.has("Elemental Fruits", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 39"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 92"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 120"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
        )    
        set_rule(
        world.get_location("TT - Quill 103"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 124"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 58"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
        )    
        set_rule(
        world.get_location("TT - Quill 21"),
        lambda state: state.has("Tongue Grapple Hook", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 107"),
        lambda state: state.has("Air Bubble", world.player),
        )    
        set_rule(
        world.get_location("TT - Quill 90"),
        lambda state: state.has("Air Bubble", world.player),
        )      
        set_rule(
        world.get_location("TT - Quill 34"),
        lambda state: state.has("Air Bubble", world.player),
        ) 
        set_rule(
        world.get_location("TT - Quill 109"),
        lambda state: state.has("Elemental Fruits", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 134"),
        lambda state: state.has("Elemental Fruits", world.player),
        )
        set_rule(
        world.get_location("TT - Quill 147"),
        lambda state: state.has("Elemental Fruits", world.player),
        )         
        set_rule(
        world.get_location("TT - Quill 29"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Boom"], world.player),
        ) 
        set_rule(
        world.get_location("TT - Quill 149"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Boom"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 41"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Boom"], world.player),
        )     
        set_rule(
        world.get_location("TT - Quill 94"),
        lambda state: has_all_moves(state, ["High Jump", "Glide"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 65"),
        lambda state: has_all_moves(state, ["High Jump", "Glide"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 125"),
        lambda state: has_all_moves(state, ["High Jump", "Glide"], world.player),
        )     
        set_rule(
        world.get_location("TT - Quill 81"),
        lambda state: has_all_moves(state, ["High Jump", "Glide"], world.player),
        )  
        set_rule(
        world.get_location("TT - Quill 33"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )     
        set_rule(
        world.get_location("TT - Quill 50"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 4"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 73"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 85"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 31"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 44"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 52"),
        lambda state: has_all_moves(state, ["Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 142"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 140"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 12"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 112"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 99"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 67"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 7"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 123"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 101"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 102"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 46"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 141"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 133"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 47"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 18"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 74"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 89"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 139"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 110"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 8"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 30"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka", "Ground Pound"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 3"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka", "Ground Pound"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 42"),
        lambda state: has_all_moves(state, ["High Jump", "Cloud Yooka", "Ground Pound"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 15"),
        lambda state: has_all_moves(state, ["High Jump", "Elemental Fruits"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 70"),
        lambda state: has_all_moves(state, ["High Jump", "Elemental Fruits"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 76"),
        lambda state: has_all_moves(state, ["High Jump", "Elemental Fruits"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 83"),
        lambda state: has_all_moves(state, ["High Jump", "Elemental Fruits"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 78"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Sonar Shot"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 115"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Sonar Shot"], world.player),
        )
        set_rule(
        world.get_location("TT - Quill 116"),
        lambda state: has_all_moves(state, ["Cloud Yooka", "Sonar Shot"], world.player),
        )    
        # --------------------------------------------------------
        # Glitterglaze Glacier - Quills 0-149
        # --------------------------------------------------------
        set_rule(
        world.get_location("GlGl - Shop 1"),
        lambda state: state.has("GlGl Quill", world.player, 15),
    )
        set_rule(
        world.get_location("GlGl - Shop 2"),
        lambda state: state.has("GlGl Quill", world.player, 40),
    )
        set_rule(
        world.get_location("GlGl - Shop 3"),
        lambda state: state.has("GlGl Quill", world.player, 65),
    )
        set_rule(
        world.get_location("GlGl - Shop 4"),
        lambda state: state.has("GlGl Quill", world.player, 100),
    )
        set_rule(
        world.get_location("GlGl - Shop 5"),
        lambda state: state.has("GlGl Quill", world.player, 130),
    )
        set_rule(
        world.get_location("GlGl - Shop 6"),
        lambda state: state.has("GlGl Quill", world.player, 150),
    )
        set_rule(
        world.get_location("GlGl - Collect all the Quills"),
        lambda state: state.has("GlGl Quill", world.player, 150),
    )
        set_rule(
        world.get_location("GlGl - Quill 0"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 1"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 2"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 3"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 8"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )      
        set_rule(
        world.get_location("GlGl - Quill 10"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 13"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 14"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 15"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound", "Air Bubble"], world.player),
    )     
        set_rule(
        world.get_location("GlGl - Quill 18"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 19"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 20"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Elemental Fruits", "Sonar Shot", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 22"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound", "Air Bubble"], world.player),
    )     
        set_rule(
        world.get_location("GlGl - Quill 26"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 27"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 32"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 33"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 35"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 37"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 39"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 41"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 42"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 47"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 52"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 53"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 54"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Elemental Fruits", "Sonar Shot", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 55"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 56"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka", "Tongue Grapple Hook"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 59"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 60"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 61"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka", "Tongue Grapple Hook"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 62"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 63"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 66"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka", "Tongue Grapple Hook"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 67"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 72"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 73"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 74"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 75"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )   
        set_rule(
        world.get_location("GlGl - Quill 80"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )    
        set_rule(
        world.get_location("GlGl - Quill 81"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 84"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka", "Tongue Grapple Hook"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 86"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 88"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 91"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 94"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 95"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 97"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 99"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 101"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 102"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 103"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 104"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 106"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 107"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 109"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 110"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 113"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 116"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 117"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 1"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 122"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 123"),
        lambda state: has_all_moves(state, ["Roll", "Cloud Yooka"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 124"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 126"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 128"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 129"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 130"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 131"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 133"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 134"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 138"),
        lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Elemental Fruits", "Sonar Shot", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 141"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 142"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 145"),
        lambda state: has_all_moves(state, ["Roll", "Tongue Grapple Hook"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 147"),
        lambda state: has_all_moves(state, ["Roll", "Elemental Fruits"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 148"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
    )
        set_rule(
        world.get_location("GlGl - Quill 149"),
        lambda state: has_all_moves(state, ["Roll", "Sonar Shot"], world.player),
    )    
        # --------------------------------------------------------
        # Moodymaze Marsh - Quills 0-149
        # --------------------------------------------------------
        set_rule(
            world.get_location("MM - Shop 1"),
            lambda state: state.has("MM Quill", world.player, 15),
        )
        set_rule(
            world.get_location("MM - Shop 2"),
            lambda state: state.has("MM Quill", world.player, 45),
        )
        set_rule(
            world.get_location("MM - Shop 3"),
            lambda state: state.has("MM Quill", world.player, 70),
        )
        set_rule(
            world.get_location("MM - Shop 4"),
            lambda state: state.has("MM Quill", world.player, 95),
        )
        set_rule(
            world.get_location("MM - Shop 5"),
            lambda state: state.has("MM Quill", world.player, 130),
        )
        set_rule(
            world.get_location("MM - Shop 6"),
            lambda state: state.has("MM Quill", world.player, 150),
        )
        set_rule(
            world.get_location("MM - Collect all the Quills"),
            lambda state: state.has("MM Quill", world.player, 150),
        )
        set_rule(
            world.get_location("MM - Quill 0"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 1"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 2"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 3"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 4"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 5"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 6"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 7"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 8"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 9"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 10"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 11"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 12"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 13"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 14"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 15"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 16"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 17"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 18"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 19"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 20"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 21"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 22"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 23"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 24"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 25"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 26"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 27"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 28"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 29"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 30"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 31"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 32"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 33"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 34"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 35"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 36"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 37"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 38"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 39"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 40"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 41"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 42"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 43"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 44"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tail Twirl"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 45"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 46"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 47"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 48"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 49"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 50"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 51"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 52"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 53"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 54"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 55"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 56"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 57"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 58"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 59"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 60"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 61"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 62"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 63"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 64"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 65"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 66"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 67"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 68"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 69"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 70"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 71"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 72"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 73"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 74"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tail Twirl"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 75"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 76"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 77"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 78"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 79"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 80"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 81"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 82"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 83"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 84"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 85"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 86"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 87"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 88"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 89"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 90"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 91"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 92"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 93"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 94"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 95"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Sonar Shot", "Elemental Fruits", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 96"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 97"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 98"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 99"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 100"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 101"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 102"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 103"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 104"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 105"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 106"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 107"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 108"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 109"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 110"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 111"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 112"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 113"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 114"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 115"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 116"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 117"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 118"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 119"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tail Twirl"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 120"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 121"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 122"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tail Twirl"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 123"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 124"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 125"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 126"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 127"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 128"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 129"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 130"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 131"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide", "Tongue Grapple Hook"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 132"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 133"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 134"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 135"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 136"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 137"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 138"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 139"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 140"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 141"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 142"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 143"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 144"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 145"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 146"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 147"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 148"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )
        set_rule(
            world.get_location("MM - Quill 149"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Glide"], world.player),
        )

        # --------------------------------------------------------
        # Capital Cashino - Quills 0-149
        # --------------------------------------------------------
        set_rule(
            world.get_location("CC - Shop 1"),
            lambda state: state.has("CC Quill", world.player, 15),
        )
        set_rule(
            world.get_location("CC - Shop 2"),
            lambda state: state.has("CC Quill", world.player, 45),
        )
        set_rule(
            world.get_location("CC - Shop 3"),
            lambda state: state.has("CC Quill", world.player, 70),
        )
        set_rule(
            world.get_location("CC - Shop 4"),
            lambda state: state.has("CC Quill", world.player, 90),
        )
        set_rule(
            world.get_location("CC - Shop 5"),
            lambda state: state.has("CC Quill", world.player, 130),
        )
        set_rule(
            world.get_location("CC - Shop 6"),
            lambda state: state.has("CC Quill", world.player, 150),
        )
        set_rule(
            world.get_location("CC - Collect all the Quills"),
            lambda state: state.has("CC Quill", world.player, 150),
        )            
        set_rule(
            world.get_location("CC - Quill 0"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 1"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 2"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 3"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 4"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 5"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 6"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 7"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 8"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 9"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 10"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 11"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 12"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 13"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 14"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 15"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Wheel Spin Attack"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 16"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 17"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 18"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 19"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 20"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 21"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 22"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 23"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 24"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 25"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 26"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 27"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 28"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 29"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 30"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 31"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 32"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 33"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 34"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 35"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 36"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 37"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 38"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Wheel Spin Attack"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 39"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 40"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 41"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 42"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 43"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 44"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 45"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 46"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 47"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 48"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 49"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 50"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 51"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 52"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 53"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 54"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 55"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 56"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 57"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 58"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 59"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 60"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 61"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 62"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 63"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 64"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 65"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 66"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 67"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 68"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 69"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 70"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 71"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 72"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 73"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 74"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 75"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 76"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 77"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 78"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 79"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 80"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 81"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 82"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 83"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 84"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 85"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 86"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 87"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 88"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 89"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 90"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 91"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 92"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 93"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 94"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 95"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 96"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 97"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 98"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 99"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 100"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 101"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 102"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Wheel Spin Attack"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 103"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 104"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 105"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 106"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 107"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 108"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 109"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 110"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 111"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 112"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 113"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 114"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 115"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 116"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 117"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 118"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 119"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 120"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 121"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 122"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 123"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 124"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 125"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 126"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 127"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 128"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 129"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 130"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 131"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 132"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 133"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 134"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 135"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 136"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 137"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 138"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 139"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 140"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 141"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 142"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 143"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 144"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 145"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Ground Pound"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 146"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 147"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "High Jump", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 148"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility", "Glide"], world.player),
        )
        set_rule(
            world.get_location("CC - Quill 149"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Invisibility"], world.player),
        )     
        # --------------------------------------------------------
        # Galleon Galaxy - Quills 0-149
        # --------------------------------------------------------
        set_rule(
            world.get_location("GaGa - Shop 1"),
            lambda state: state.has("GaGa Quill", world.player, 15),
        )
        set_rule(
            world.get_location("GaGa - Shop 2"),
            lambda state: state.has("GaGa Quill", world.player, 45),
        )
        set_rule(
            world.get_location("GaGa - Shop 3"),
            lambda state: state.has("GaGa Quill", world.player, 65),
        )
        set_rule(
            world.get_location("GaGa - Shop 4"),
            lambda state: state.has("GaGa Quill", world.player, 85),
        )
        set_rule(
            world.get_location("GaGa - Shop 5"),
            lambda state: state.has("GaGa Quill", world.player, 130),
        )
        set_rule(
            world.get_location("GaGa - Shop 6"),
            lambda state: state.has("GaGa Quill", world.player, 150),
        )
        set_rule(
            world.get_location("GaGa - Collect all the Quills"),
            lambda state: state.has("GaGa Quill", world.player, 150),
        )
        set_rule(
            world.get_location("GaGa - Quill 0"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 1"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 2"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 3"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 4"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 5"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 6"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 7"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 8"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 9"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 10"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 11"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 12"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 13"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 14"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 15"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 16"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 17"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 18"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 19"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 20"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 21"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 22"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 23"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka", "Elemental Fruits", "Invisibility", "Wheel Spin Attack"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 24"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 25"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 26"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 27"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 28"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 29"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 30"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 31"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 32"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 33"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 34"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 35"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 36"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 37"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 38"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 39"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 40"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 41"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 42"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 43"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 44"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 45"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 46"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 47"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 48"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 49"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 50"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 51"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 52"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 53"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 54"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 55"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 56"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 57"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 58"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 59"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 60"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 61"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 62"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 63"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 64"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 65"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 66"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 67"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 68"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 69"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 70"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 71"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 72"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 73"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 74"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 75"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 76"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 77"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 78"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 79"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 80"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 81"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 82"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 83"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 84"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 85"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 86"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 87"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 88"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 89"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 90"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 91"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 92"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 93"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 94"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 95"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 96"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 97"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 98"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka", "Elemental Fruits", "Invisibility", "Wheel Spin Attack"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 99"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 100"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 101"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 102"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 103"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 104"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 105"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 106"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 107"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 108"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 109"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 110"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 111"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 112"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 113"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 114"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 115"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 116"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 117"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 118"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 119"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 120"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 121"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 122"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 123"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 124"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 125"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 126"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 127"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 128"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 129"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka", "Elemental Fruits", "Invisibility", "Wheel Spin Attack"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 130"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 131"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 132"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 133"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 134"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 135"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 136"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 137"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 138"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 139"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 140"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 141"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 142"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 143"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 144"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 145"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka", "Elemental Fruits", "Invisibility", "Wheel Spin Attack"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 146"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 147"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 148"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )
        set_rule(
            world.get_location("GaGa - Quill 149"),
            lambda state: has_all_moves(state, ["Roll", "Air Bubble", "Tongue Grapple Hook", "Cloud Yooka"], world.player),
        )

# ---------------------------------------------------------------------------
# Victory Condition
# ---------------------------------------------------------------------------

def set_completion_condition(world: ReplayleeWorld) -> None:
    """Set victory from the selected hunt goal."""

    if world.options.goal.value == 2:  # defeat_capital_b
        world.multiworld.completion_condition[world.player] = (
            lambda state: state.has("Victory", world.player)
        )
    elif world.options.goal.value == 1:  # golden_pagie_hunt
        goal_amount = world.options.golden_pagie_goal.value
        world.multiworld.completion_condition[world.player] = (
            lambda state: state.has("Golden Pagie", world.player, goal_amount)
        )
    else:  # triple_pagie_medal_hunt
        goal_amount = world.options.triple_pagie_medal_goal.value
        world.multiworld.completion_condition[world.player] = (
            lambda state: state.has("Triple Pagie Medal", world.player, goal_amount)
        )
