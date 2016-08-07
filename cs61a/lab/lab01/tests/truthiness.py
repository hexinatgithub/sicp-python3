test = {
  'name': 'Truthiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 or True
          5154670fa295caf18cafa4245c1358a9
          # locked
          >>> not '' or not 0 and False
          5154670fa295caf18cafa4245c1358a9
          # locked
          >>> 13 and False
          5dfeeb9ca37d955606d40c6553cd4956
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}