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
          4
          >>> WallAnt.food_cost
          4
          """,
          'hidden': False,
          'locked': False
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
          True
          """,
          'hidden': False,
          'locked': False
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
