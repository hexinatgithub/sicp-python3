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
          7ce2b04ec7f8fa8a455fbb329f74fb03
          # locked
          scm> (outer 1 2)
          8b11371e85a480991b3b0c53fdb78a61
          # locked
          scm> (define (outer-func x y)
          ....   (define (inner z x)
          ....     (+ x (* y 2) (* z 3)))
          ....   inner)
          0fadc0a449c448871ff180a4a8209283
          # locked
          scm> ((outer-func 1 2) 1 10)
          8b11371e85a480991b3b0c53fdb78a61
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
