test = {
  'name': 'Problem 7B',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing HungryAnt parameters
          >>> hungry = HungryAnt()
          >>> HungryAnt.food_cost
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          >>> hungry.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing HungryAnt eats and digests
          >>> hungry = HungryAnt()
          >>> super_bee, wimpy_bee = Bee(1000), Bee(1)
          >>> place = colony.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> place.add_insect(super_bee)
          >>> hungry.action(colony)   # super_bee is no match for HungryAnt!
          >>> super_bee.armor
          73b94a1326ae2e803c3421016112207b
          # locked
          >>> place.add_insect(wimpy_bee)
          >>> for _ in range(3):
          ...     hungry.action(colony)  # digesting...not eating
          >>> wimpy_bee.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> hungry.action(colony)    # back to eating!
          >>> wimpy_bee.armor
          73b94a1326ae2e803c3421016112207b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing HungryAnt only waits when digesting
          >>> hungry = HungryAnt()
          >>> place = colony.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> # Wait a few turns before adding Bee
          >>> for _ in range(5):
          ...     hungry.action(colony)  # shouldn't be digesting
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> hungry.action(colony)  # Eating time!
          >>> bee.armor
          73b94a1326ae2e803c3421016112207b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing HungryAnt digest time looked up on instance
          >>> very_hungry = HungryAnt()  # Add very hungry caterpi- um, ant
          >>> very_hungry.time_to_digest = 0
          >>> place = colony.places["tunnel_0_0"]
          >>> place.add_insect(very_hungry)
          >>> for _ in range(100):
          ...     place.add_insect(Bee(3))
          >>> for _ in range(100):
          ...     very_hungry.action(colony)   # Eat all the bees!
          >>> len(place.bees)
          73b94a1326ae2e803c3421016112207b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing HungryAnt dies while eating
          >>> hungry = HungryAnt() 
          >>> place = colony.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> place.add_insect(Bee(3))
          >>> hungry.action(colony)
          >>> len(place.bees)
          73b94a1326ae2e803c3421016112207b
          # locked
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> bee.action(colony) # Bee kills digesting ant
          >>> place.ant
          >>> len(place.bees)
          d89cf7c79d5a479b0f636734143ed5e6
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