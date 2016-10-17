test = {
  'name': 'Problem 7A',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing NinjaAnt parameters
          >>> ninja = NinjaAnt()
          >>> ninja.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> NinjaAnt.food_cost
          50ae32be3e31df6c59633df7fdfb3a72
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing non-NinjaAnts still block bees
          >>> p0 = colony.places["tunnel_0_0"]
          >>> p1 = colony.places["tunnel_0_1"]
          >>> bee = Bee(2)
          >>> p1.add_insect(bee)
          >>> p1.add_insect(ThrowerAnt())
          >>> bee.action(colony)  # attack ant, don't move past it
          >>> bee.place is p0
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> bee.place is p1
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing NinjaAnts do not block bees
          >>> p0 = colony.places["tunnel_0_0"]
          >>> p1 = colony.places["tunnel_0_1"]
          >>> bee = Bee(2)
          >>> p1.add_insect(bee)
          >>> p1.add_insect(NinjaAnt())
          >>> bee.action(colony)  # shouldn't attack ant, move past it
          >>> bee.place is p0
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing NinjaAnt strikes all bees in its place
          >>> test_place = colony.places["tunnel_0_0"]
          >>> for _ in range(3):
          ...     test_place.add_insect(Bee(2))
          >>> ninja = NinjaAnt()
          >>> test_place.add_insect(ninja)
          >>> ninja.action(colony)   # should strike all bees in place
          >>> [bee.armor for bee in test_place.bees]
          7ba130373ce1098e546d938c59eedd24
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing NinjaAnt strikes all bees, even if some expire
          >>> test_place = colony.places["tunnel_0_0"]
          >>> for _ in range(3):
          ...     test_place.add_insect(Bee(1))
          >>> ninja = NinjaAnt()
          >>> test_place.add_insect(ninja)
          >>> ninja.action(colony)   # should strike all bees in place
          >>> len(test_place.bees)
          73b94a1326ae2e803c3421016112207b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing damage is looked up on the instance
          >>> place = colony.places["tunnel_0_0"]
          >>> bee = Bee(900)
          >>> place.add_insect(bee)
          >>> buffNinja = NinjaAnt()
          >>> buffNinja.damage = 500  # Sharpen the sword
          >>> place.add_insect(buffNinja)
          >>> buffNinja.action(colony)
          >>> bee.armor
          0562206f4949c480df34746f6392dbfb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing Ninja ant does not crash when left alone
          >>> ninja = NinjaAnt()
          >>> colony.places["tunnel_0_0"].add_insect(ninja)
          >>> ninja.action(colony)
          >>> ninja.place.bees
          a1218a9cb09e85b249f8863ced8a8dad
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