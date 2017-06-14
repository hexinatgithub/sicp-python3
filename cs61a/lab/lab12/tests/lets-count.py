test = {
  'name': 'lets-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from fa16favnum;
          7|29
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    },
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from fa16favpets;
          dog|31
          cat|22
          tiger|18
          panda|10
          penguin|8
          harambe|7
          wolf|7
          elephant|6
          dolphin|5
          dragon|5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    },
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from sp17favpets;
          dragon|20
          dog|14
          cat|8
          unicorn|7
          n/a|6
          panda|5
          dolphin|4
          tiger|4
          7|3
          bear|3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    },
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from sp17dragon;
          dragon|20
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    },
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from sp17alldragons;
          dragon|22
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    },
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from obedienceimage;
          7|Image 1|40
          7|Image 2|11
          7|Image 3|21
          7|Image 4|16
          7|Image 5|11
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
