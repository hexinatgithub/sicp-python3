test = {
  'name': 'obedience',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          7|Image 3
          I do what I want.|Image 1
          I do what I want.|Image 5
          7|Image 1
          I do what I want.|Image 4
          I'm a rebel|Image 2
          7|Image 4
          7|Image 5
          I'm a rebel|Image 5
          7|Image 3
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
