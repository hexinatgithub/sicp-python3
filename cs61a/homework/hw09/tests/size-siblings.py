test = {
  'name': 'size-siblings',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from sentences;
          barack and clinton are standard siblings
          abraham and grover are toy siblings
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw09.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
