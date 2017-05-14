test = {
  'name': 'Problem 16',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define y 1)
          y
          scm> (define f (mu (x) (+ x y)))
          f
          scm> (define g (lambda (x y) (f (+ x x))))
          g
          scm> (g 3 7)
          13
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
