from biautom.game.chip import GameChip


grass_chip: GameChip = GameChip("grass")


print(grass_chip.data.placement.me.loop[0].fails)
print(grass_chip.condition_check(grass_chip.data.placement.me.loop[0].holds, grass_chip))
