test = {
  'name': 'Problem 14',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((> 2 3) 5)
          ....       ((> 2 4) 6)
          ....       ((< 2 5) 7)
          ....       (else 8))
          7
          scm> (cond ((> 2 3) 5)
          ....       ((> 2 4) 6)
          ....       (else 8))
          8
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
          scm> (cond (0 'yea)
          ....       (else 'nay))
          yea
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (define y 0)
          y
          scm> (define z 0)
          z
          scm> (cond (#t
          ....        (define x (+ x 1))
          ....        (define y (+ y 1))
          ....        (define z (+ z 1)))
          ....       (else
          ....        (define x (- x 5))
          ....        (define y (- y 5))
          ....        (define z (- z 5))))
          z
          scm> (list x y z)
          (1 1 1)
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
