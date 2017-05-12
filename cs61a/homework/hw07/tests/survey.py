test = {
  'name': 'survey',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (survey)
          7c0334a0b53ffeaf7bfb9468e5a2931f
          # locked
          """,
          'hidden': False,
          'locked': True
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
