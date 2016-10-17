test = {
  'name': 'Problem 6A',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing WallAnt parameters
          >>> wall = WallAnt()
          >>> wall.armor
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          >>> WallAnt.food_cost
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing WallAnt stays in place
          >>> wall = WallAnt()
          >>> colony.places["tunnel_0_1"].add_insect(wall)
          >>> bee1 = Bee(1001)
          >>> colony.places["tunnel_0_1"].add_insect(bee1)
          >>> bee1.action(colony)
          >>> bee1.place is wall.place
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(make_test_assault_plan()), test_layout
      >>> colony = AntColony(None, hive, ant_types(), layout)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}