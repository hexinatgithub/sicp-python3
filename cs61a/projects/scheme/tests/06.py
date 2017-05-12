test = {
  'name': 'Problem 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'fafe1301fe2e206817bdc9dd9e3a389d',
          'choices': [
            r"""
            Pair(A, Pair(B, nil)), where:
                A is the symbol being bound,
                B is an expression whose value should be bound to A
            """,
            r"""
            Pair(A, Pair(B, nil)), where:
                A is the symbol being bound,
                B is the value that should be bound to A
            """,
            r"""
            Pair(A, B), where:
                A is the symbol being bound,
                B is the value that should be bound to A
            """,
            r"""
            Pair(A, B), where:
                A is the symbol being bound,
                B is an expression whose value should be bound to A
            """,
            r"""
            Pair('define', Pair(A, Pair(B, nil))), where:
                A is the symbol being bound,
                B is an expression whose value should be bound to A
            """
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is the structure of the expressions argument to do_define_form?'
        },
        {
          'answer': 'b2dc2d8fc11300d5e68ab1e5dbaef0c4',
          'choices': [
            'make_child_frame',
            'define',
            'lookup',
            'bindings'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What method of a Frame instance will bind
          a value to a symbol in that frame?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define size 2)
          e01d2409c829d607dce70d43078295d4
          # locked
          scm> size
          4b7283d4dfa392633549336acb032de7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define x (+ 2 3))
          c55ea5b1bca40acd76b8c213f8a08f8b
          # locked
          scm> x
          39dba75757e21a295c7803a12e1e5877
          # locked
          scm> (define x (+ 2 7))
          c55ea5b1bca40acd76b8c213f8a08f8b
          # locked
          scm> x
          9cc890fba2180e73142276346c5369b9
          # locked
          scm> (eval (define tau 6.28))
          b3ae0b39b59664b3f22944e323d71e42
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
