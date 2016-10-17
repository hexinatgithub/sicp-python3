info = {
  'hidden_params': {
    'doctest': {
      'cache': """
      from ants import *
      import ants
      import imp
      import ants_sol
      """,
      'setup': """
      hive, layout = Hive(make_test_assault_plan()), test_layout
      colony = AntColony(None, hive, ant_types(), layout)
      """
    }
  },
  'name': 'cal/61A/fa14/proj3',
  'params': {
    'doctest': {
      'cache': """
      from ants import *
      import ants
      import imp
      """,
      'setup': """
      hive, layout = Hive(make_test_assault_plan()), test_layout
      colony = AntColony(None, hive, ant_types(), layout)
      """
    }
  },
  'src_files': [
    'ants.py'
  ],
  'version': '1.0'
}
