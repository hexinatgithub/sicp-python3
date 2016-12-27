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
          6
          >>> fire.armor
          1
          """,
          'hidden': False,
          'locked': False
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
          2
          """,
          'hidden': False,
          'locked': False
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
          0
          """,
          'hidden': False,
          'locked': False
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
          0
          >>> place.ant # The FireAnt should not occupy the place anymore
          """,
          'hidden': False,
          'locked': False
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
          400
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
