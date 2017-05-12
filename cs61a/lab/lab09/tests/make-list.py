test = {
  'name': 'make-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a '(1))
          bd3f05fa4cb9864ae23adf7936df4482
          # locked
          scm> a
          b9d3050f3e734543c211b93d1f4808e8
          # locked
          scm> (define b (cons 2 a))
          90e805b4bb15ef8854fd5ccbb0d9601f
          # locked
          scm> b
          1950181d4be407b7d109809a1722eb97
          # locked
          scm> (define c (list 3 b))
          c7b5a5707e50e9a75b69a2b365646bab
          # locked
          scm> c
          e6692c1ebab7ee77215df9cc0ad3e1e5
          # locked
          scm> (car c)
          7cce957d5689f75737e35919f54283e1
          # locked
          scm> (cdr c)
          3b4e95240ede6a3fa460a5c068893f37
          # locked
          scm> (car (car (cdr c)))
          32cd207d18df99546ca7a56bc36ed715
          # locked
          scm> (cdr (car (cdr c)))
          b9d3050f3e734543c211b93d1f4808e8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> lst  ; type out exactly how Scheme would print the list
          35e62c9d10c3e10bfd3e0fb5d784a70f
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define bees '(knees))
          a113fedc4d4b8de0e7a2de6df3df3ac2
          # locked
          scm> (cons 'cows (cons 3 bees))
          5ac8eeeaafeb2bee70d8295d56272610
          # locked
          scm> (cons 'cows (car bees))
          fcb5d90c5b6cecca2330dcea7d84bb8c
          # locked
          scm> (car (cdr bees))  # Type SchemeError if you think this errors
          03be6c509e835275b4882fdac38b7d9b
          # locked
          scm> (define kfc '((chicks) . (picks . ticks)))
          a1b880d2a6d69ed6a1049fe7bebf6649
          # locked
          scm> kfc
          a34f00a3935526c28a985f8bbf59a1da
          # locked
          scm> (define cfk (list (cdr kfc) (car bees)))
          92747f2ba01d3071a4e21e660b861d82
          # locked
          scm> cfk
          c751a3be99a84413f8f28ad6da6993af
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
