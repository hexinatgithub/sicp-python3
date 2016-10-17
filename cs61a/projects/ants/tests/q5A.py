test = {
  'name': 'Problem 5A',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing fire parameters
          >>> fire = FireAnt()
          >>> FireAnt.food_cost
          50ae32be3e31df6c59633df7fdfb3a72
          # locked
          >>> fire.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing fire damage
          >>> place = Place('Fire Test1')
          >>> bee = Bee(5)
          >>> place.add_insect(bee)
          >>> place.add_insect(FireAnt())
          >>> bee.action(colony) # attack the FireAnt
          >>> bee.armor
          20d533d3e06345c8bd7072212867f2d1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing fire does damage to all Bees in its Place
          >>> place = Place('Fire Test2')
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> place.add_insect(Bee(3))
          >>> place.add_insect(FireAnt())
          >>> bee.action(colony) # attack the FireAnt
          >>> len(place.bees)  # How many bees are left?
          73b94a1326ae2e803c3421016112207b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing FireAnt dies
          >>> place = Place('Fire Test3')
          >>> bee = Bee(1)
          >>> ant = FireAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> bee.action(colony) # attack the FireAnt
          >>> ant.armor
          73b94a1326ae2e803c3421016112207b
          # locked
          >>> place.ant # The FireAnt should not occupy the place anymore
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing fire damage is instance attribute
          >>> place = Place('Fire Test4')
          >>> bee = Bee(900)
          >>> buffAnt = FireAnt()
          >>> buffAnt.damage = 500   # Feel the burn!
          >>> place.add_insect(bee)
          >>> place.add_insect(buffAnt)
          >>> bee.action(colony) # attack the FireAnt
          >>> bee.armor  # is damage an instance attribute?
          0562206f4949c480df34746f6392dbfb
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