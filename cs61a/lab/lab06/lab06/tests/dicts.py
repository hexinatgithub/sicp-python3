test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          a17840518b709ae719241f1ba8d5cf1e
          # locked
          >>> len(pokemon)
          214f1f0cf62380259278c29f0dd9185d
          # locked
          >>> pokemon['jolteon'] = 135
          >>> pokemon['ditto'] = 25
          >>> len(pokemon)
          73dc0de5202f020182ea500448cc846a
          # locked
          >>> sorted(list(pokemon.keys()))  # Alphabetically sorted list of pokemon's keys
          12803b91b32f548dd8fd19243ea69b0a
          # locked
          >>> 'mewtwo' in pokemon
          a559f517e8f86de30b928d7e29ec2331
          # locked
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> sorted(list(pokemon.keys()))  # Alphabetically sorted list of pokemon's keys
          12803b91b32f548dd8fd19243ea69b0a
          # locked
          >>> pokemon['ditto']
          4c37942662a0872256452f2f43642de6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> letters = {'a': 1, 'b': 2, 'c': 3}
          >>> 2 in letters
          a559f517e8f86de30b928d7e29ec2331
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> food = {'bulgogi': 10, 'falafel': 4, 'ceviche': 7}
          >>> food['ultimate'] = food['bulgogi'] + food['ceviche']
          >>> food['ultimate']
          550523d3ae5773d7cd7415e2c85b2a1f
          # locked
          >>> len(food)
          41cc26e29cc2a9e0b6fb880e349243bb
          # locked
          >>> food['ultimate'] += food['falafel']
          >>> food['ultimate']
          d72a651c8579ddecb99172e2fb455d75
          # locked
          >>> sorted(list(food.keys()))
          550e9377e3f16284a5fd5e9f03daf1a9
          # locked
          >>> food['bulgogi'] = food['falafel']
          >>> len(food)
          41cc26e29cc2a9e0b6fb880e349243bb
          # locked
          >>> 'gogi' in food
          a559f517e8f86de30b928d7e29ec2331
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
