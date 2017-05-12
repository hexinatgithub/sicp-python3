test = {
  'name': 'Problem 19',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (let-to-lambda 1)
          1d6ef7880cd9b59b64a1f4e1a1e35a12
          # locked
          scm> (let-to-lambda 'a)
          771dfeac5012b5d36a606ee5b8f55c7f
          # locked
          scm> (let-to-lambda '(+ 1 2))
          7dffb54d077c0d96ba862301c9b369d2
          # locked
          scm> (let-to-lambda '(let ((a 1)
          ....                 (b 2))
          ....                (+ a b)))
          6d9be4ba540c7e358e06767ffa2ff5fb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(quoted expressions remain the same)
          (quoted expressions remain the same)
          scm> (let-to-lambda '(quote (let ((a 1) (b 2)) (+ a b))))
          (quote (let ((a 1) (b 2)) (+ a b)))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> '(lambda parameters not affected but body affected)
          (lambda parameters not affected but body affected)
          scm> (let-to-lambda '(lambda (let a b) (+ let a b)))
          (lambda (let a b) (+ let a b))
          scm> (let-to-lambda '(lambda (x) a (let ((a x)) a)))
          (lambda (x) a ((lambda (a) a) x))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
