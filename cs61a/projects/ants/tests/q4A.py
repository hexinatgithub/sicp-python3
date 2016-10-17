test = {
  'name': 'Problem 4A',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'd21f3a6075cc741a42d6d6ce12e5aed9',
          'choices': [
            'Always; after adding the insect, reduce its armor to 0 if it is not watersafe',
            'Only if the insect is watersafe; if it is not watersafe, reduce its armor to 0',
            'Only if the insect is watersafe; if it is not watersafe, remove the insect from the place',
            'Never; no insect can be placed in a Water Place'
          ],
          'hidden': False,
          'locked': True,
          'question': 'When should an insect be added to a Water Place?'
        },
        {
          'answer': 'fae228bbdefaf89611ef0df5ee7e8225',
          'choices': [
            'class attribute',
            'instance attribute',
            'local attribute',
            'global attribute'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What type of attribute should "watersafe" be?'
        },
        {
          'answer': '127cd87858e6c0a9f29f199fb2e2be0a',
          'choices': [
            'reduce_armor, in the Insect class',
            'remove_insect, in the Place class',
            'sting, in the Bee class',
            'action, in the Insect class',
            'remove_ant, in the AntColony class'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What method deals damage to an Insect and removes it from
          its Place? (You should use this method in your code.)
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing water with soggy (non-watersafe) bees
          >>> test_ants = [Bee(1000000), HarvesterAnt(), Ant(), ThrowerAnt()]
          >>> test_ants[0].watersafe = False # Make Bee non-watersafe
          >>> test_water = Water('Water Test1')
          >>> passed = True
          >>> for test_ant in test_ants:
          ...    test_water.add_insect(test_ant)
          ...    passed = passed and \
          ...             test_ant is not test_water.ant and \
          ...             test_ant.armor == 0
          >>> passed
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing water with watersafe bees
          >>> test_bee = Bee(1)
          >>> test_water = Water('Water Test2')
          >>> test_water.add_insect(test_bee)
          >>> test_bee.armor
          1
          >>> test_bee in test_water.bees
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing water inheritance
          >>> old_add_insect = Place.add_insect
          >>> def new_add_insect(self, insect):
          ...     raise NotImplementedError()
          
          >>> Place.add_insect = new_add_insect
          >>> test_bee = Bee(1)
          >>> test_water = Water('Water Test3')
          >>> passed = False
          >>> try:
          ...     test_water.add_insect(test_bee)
          ... except NotImplementedError:
          ...     passed = True
          >>> passed
          True
          # explanation: Make sure to use inheritance!
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ### Make sure to place the ant before watering it!
          >>> old_add_insect = Place.add_insect
          >>> def new_add_insect(self, insect):
          ...     raise NotImplementedError()
          
          >>> Place.add_insect = new_add_insect
          >>> test_ant = HarvesterAnt()
          >>> test_water = Water('Water Test4')
          >>> passed = False
          >>> try:
          ...     test_water.add_insect(test_ant)
          ... except NotImplementedError:
          ...     passed = True
          
          >>> passed
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
      'teardown': r"""
      >>> Place.add_insect = old_add_insect
      """,
      'type': 'doctest'
    }
  ]
}