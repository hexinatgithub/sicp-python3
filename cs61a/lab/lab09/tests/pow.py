test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow 4 0)
          7cd20da6435c318b417f99ab831ac85e
          # locked
          scm> (pow 10 3)
          b94ade7857287ba74ddc9cc81d972eff
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 2 3)
          2bfcd627609c82ebd017c2edfad00c89
          # locked
          scm> (pow 2 5)
          a37ba38979e27e6a8fe0387af20430ca
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 3 3)
          748461e5d70d2d34436c8d3c5a04855e
          # locked
          scm> (pow 3 4)
          aaf3851361cb53b0539dd66efd432857
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
