# SquareWorld
Simple 2d sandbox game

# Made
- World and entity system, similar to Minecraft
- Block placement/breaking system
- Command system/Command parser
- Time system
- Text input system
- Nextbot AI and ambience

# Controls
- WASD - move
- IJKL - move camera
- H - lock camera on player
- TAB - open debug menu and show hitboxes
- / - open console
- Enter - switch main menu/game menu
- Enter (while typing command) - run command
- 1/2/3 - chose building blocks
- Left mouse click - place block
- Right mouse click - damage block (destroy if in god mode)

# Commands
Press / to enter commands

- hp heal value - heals player
- hp heal + - fully heals player
- hp damage value - damages player
- hp damage kill - kills player
- maxhealth value - sets player max health
- tp value value - teleports player
- spawn entity value value {} - spawn an entity with chosen creation params
- god true/false - Enables/Disables god mode
- time value - 1 base time, 2 2x faster, 0.5 2x slower and e.t.c
- clear entity - removes all entities (except player)
- clear block - removes all blocks 
- spawnpoint value value - sets player spawnpoint
- speed value - sets players speed, type default to set default speed
- nextbot ai True/False - turn on/off nextbot ai
- nextbot sound True/False - turn on/off nextbot sound

# Look at this
- [World](src/world/world.py)
- [Entity](src/world/entity.py)
- [Block](src/world/block/entity_block.py)
- [Timer](src/core/timer.py)
- [Typing field](src/command/typing_field.py)
- [HpBar](src/graphics/hp_bar.py)
- [Nextbot](src/world/nextbot/entity_nextbot.py)
- [Commands](src/command/commands.py)