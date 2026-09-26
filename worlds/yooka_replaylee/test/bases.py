from test.bases import WorldTestBase

from ..world import ReplayleeWorld


class ReplayleeTestBase(WorldTestBase):
    game = "Yooka-Replaylee"
    world: ReplayleeWorld
