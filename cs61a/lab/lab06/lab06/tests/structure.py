test = {
  'name': 'Structure',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'fb6c2a416527c8ef3b7464feb1febb77',
          'choices': [
            'tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])',
            'tree(1, (tree(2), tree(3, (tree(5))), tree(5)))',
            'tree(2, [tree(1, tree(3, tree(5)))], tree(4))',
            'tree(1, [tree(2), tree(3), tree(4)], tree(5))'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Which constructor call creates the following tree structure?
              1
            / | \
           2  3  4
             /
            5
          """
        },
        {
          'answer': '950a8ab058ee078b8da4d75e4937cabb',
          'choices': [
            'tree(3, [tree(6, [tree(2), tree(1)]), tree(2), tree(7)])',
            'tree(3, tree(6, [tree(2), tree(1)]), tree(2), tree(7))',
            'tree(3, [tree(6), [tree(2), tree(1)], tree(2), tree(7)])',
            'tree(3, tree(6), [tree(2), tree(1)], [tree(2), tree(7)])'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Which constructor call creates the following tree structure?
                3
              / | \
             6  2  7
            / \
           2   1
          """
        },
        {
          'answer': 'd05bc830613dfa69ef96df4f94a8da70',
          'choices': [
            '2',
            '3',
            '6',
            '7'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many children does the following tree have?
                7
               / \
              2  4
             /|  |
            1 5  2
              |
              3
          """
        },
        {
          'answer': '484a98b7eb7b0faee7d203e50e8afa7c',
          'choices': [
            '1, 6, 5',
            '1, 6, 5, 4',
            '7, 6, 1, 5, 4',
            'None of the above'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Given the following tree structure, what are all the leaves?
                7
              / | \
             3  2  4
            /  /|
           6  1 5
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
