test = {
  'name': 'greatstudents',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM greatstudents;
          12/31|blue|dog|50|42
          12/25|blue|wolf|5|4
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
