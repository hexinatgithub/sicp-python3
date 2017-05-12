test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sign -42)
          -1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (sign 0)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (sign 42)
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw07)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
