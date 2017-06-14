test = {
  'name': 'sevens',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sevens;
          Choose this option instead.
          7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
