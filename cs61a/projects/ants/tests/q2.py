test = {
  'name': 'Question 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> HarvesterAnt.food_cost
          20d533d3e06345c8bd7072212867f2d1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ThrowerAnt.food_cost
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing HarvesterAnt action
          >>> colony.food = 4
          >>> HarvesterAnt().action(colony)
          >>> colony.food
          62674984f877ec783f37e8b8b9c264d0
          # locked
          >>> HarvesterAnt().action(colony)
          >>> colony.food
          50ae32be3e31df6c59633df7fdfb3a72
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