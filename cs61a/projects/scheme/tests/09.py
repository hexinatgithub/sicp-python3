test = {
  'name': 'Problem 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (lambda (x y) (+ x y))
          d579a305762000c8ae036c510fb2baf6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (lambda (x) (+ x) (+ x x))
          (lambda (x) (+ x) (+ x x))
          scm> (lambda (x))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
