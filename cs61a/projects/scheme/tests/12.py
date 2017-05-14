test = {
  'name': 'Problem 12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (square x) (* x x))
          square
          scm> square
          (lambda (x) (* x x))
          scm> (square 21)
          441
          scm> square ; check to make sure lambda body hasn't changed
          (lambda (x) (* x x))
          scm> (define square (lambda (x) (* x x)))
          square
          scm> (square (square 21))
          194481
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define (outer x y)
          ....   (define (inner z x)
          ....     (+ x (* y 2) (* z 3)))
          ....   (inner x 10))
          outer
          scm> (outer 1 2)
          17
          scm> (define (outer-func x y)
          ....   (define (inner z x)
          ....     (+ x (* y 2) (* z 3)))
          ....   inner)
          outer-func
          scm> ((outer-func 1 2) 1 10)
          17
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
