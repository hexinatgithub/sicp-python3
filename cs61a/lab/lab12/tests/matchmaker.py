test = {
  'name': 'matchmaker',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          dragon|Closer|blue|blue
          dragon|Closer|blue|gold
          dog|Hello|blue|mint
          dog|Hello|blue|blue
          dragon|Fur Elise|orange|blue
          dragon|Fur Elise|orange|blue
          dragon|Fur Elise|orange|black
          hippogriff|That Way|orange|purple
          dragon|Closer|blue|gold
          dragon|Hello|blue|red
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
