test = {
  'name': 'Problem 18',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (list-change 10 '(25 10 5 1))
          ((10) (5 5) (5 1 1 1 1 1) (1 1 1 1 1 1 1 1 1 1))
          scm> (list-change 5 '(4 3 2 1))
          ((4 1) (3 2) (3 1 1) (2 2 1) (2 1 1 1) (1 1 1 1 1))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': "scm> (load 'questions)",
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
