test = {
  'name': 'Problem 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (f x y) (+ x y))
          17c5c9131eea78a6dfb3175a8e97e160
          # locked
          scm> f
          d579a305762000c8ae036c510fb2baf6
          # locked
          # choice: (lambda (x y) (+ x y))
          # choice: (lambda (f x y) (+ x y))
          # choice: (f (x y) (+ x y))
          # choice: (define f (lambda (x y) (+ x y)))
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define (f) (+ 2 2))
          f
          scm> f
          (lambda () (+ 2 2))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (f x) (* x x))
          f
          scm> f
          (lambda (x) (* x x))
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
