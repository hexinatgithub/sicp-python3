test = {
  'name': 'Understanding scheme.py',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '5fbed1a40cd7ce16bb2023abd64fe11e',
          'choices': [
            'For a user-defined procedure only',
            'For a primitive procedure only',
            'For a either a user-defined or primitive procedure'
          ],
          'hidden': False,
          'locked': True,
          'question': 'When does scheme_apply call scheme_eval?'
        },
        {
          'answer': 'a91b8f3bb18e60810571c032e56f48fa',
          'choices': [
            'env.lookup(expr)',
            'expr.first',
            'scheme_symbolp(expr)',
            'SPECIAL_FORMS[first](rest, env)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What expression in the body of scheme_eval computes
          the value of a symbol?
          """
        },
        {
          'answer': '58f1effaf88582477cf57f2665e1247b',
          'choices': [
            'SchemeError("malformed list: (1)")',
            'SchemeError("cannot call: 1")',
            'AssertionError',
            'SchemeError("unknown identifier: 1")'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What exception should be raised for the expression (1)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
