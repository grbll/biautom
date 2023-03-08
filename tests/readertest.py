from biautom.game.chip_reader import ChipReader


default_string = """
{
  "family": [
    "poacea"
  ],
  "role": [
    "producer"
  ],
  "placement": {
    "me": {
      "holds": {},
      "fails": {},
      "value": {
        "operation": "maximum"
      },
      "positions": {
        "origin": [
          [
            0,
            0
          ]
        ],
        "span": [
          [
            1,
            0
          ]
        ]
      },
      "loop": [
        {
          "holds": {
            "initial": true
          },
          "fails": {},
          "value": {
            "base": 0,
            "operation": "sum"
          },
          "positions": {},
          "loop": []
        }
      ]
    }
  }
}
"""

test = ChipReader(
    ["json/chip_data"],
    ["json/schemata"],
    ["json/schemata/chip_schema/chip_data.json"],
    default_string,
)

print(test.default.placement.me.loop[0].fails)
