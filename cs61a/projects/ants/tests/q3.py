test = {
  'name': 'Problem 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Simple test for Place
          >>> exit = Place('Test Exit')
          >>> exit.exit
          >>> exit.entrance
          >>> place = Place('Test Place', exit)
          >>> place.exit is exit
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> exit.entrance is place
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing if entrances are properly initialized
          >>> passed = True
          >>> for entrance in colony.bee_entrances:
          ...     place = entrance
          ...     while place:
          ...         passed = passed and (place.entrance is not None)
          ...         place = place.exit
          >>> passed
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if exits and entrances are different
          >>> passed = True
          >>> for place in colony.places.values():
          ...     passed = passed and \
          ...              (place is not place.exit) and \
          ...              (place is not place.entrance)
          ...     if place.exit and place.entrance:
          ...         passed = passed and (place.exit is not place.entrance)
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
      'teardown': '',
      'type': 'doctest'
    }
  ]
}