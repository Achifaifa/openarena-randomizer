#! /usr/bin/env python

import random

gamemodes={"Deathmatch":0, "Team deathmatch":3, "CTF":4, "Elimination":8, "Last man standing":10}
weaponres=["weapon_shotgun","weapon_grenadelauncher","weapon_rocketlauncher","weapon_lightning","weapon_railgun","weapon_plasmagun","weapon_bfg","weapon_grapplinghook","ammo_shells","ammo_bullets","ammo_grenades","ammo_cells","ammo_lightning","ammo_rockets","ammo_slugs","ammo_bfg","item_armor_shard ","item_armor_combat","item_armor_body","item_health_small","item_health","item_health_large","item_health_mega ","holdable_teleporter","holdable_medkit","item_quad","item_enviro","item_haste","item_invis","item_regen","item_flight"]
yesno=lambda:random.choice([0,1])

configfile=open("./out.cfg","w+")

# Fixed settings
configfile.write("set sv_hostname ^1Ach^8ifa^3ifa^2nta^4sti^6co!\n")
configfile.write("set sv_motd 'Con 7 portaminas y hierro'")
configfile.write("set sv_maxclients 16\n")
configfile.write("set sv_pure 0\n")
configfile.write("set timelimit 0\n")
configfile.write("set fraglimit %s\n"%raw_input("Fraglimit?\n>"))

# Game mode setting
print "Pick the game mode"
print "\n".join("%i - %s"%(i,s) for i,s in enumerate(gamemodes.keys()))
configfile.write("set g_gametype %s\n"%gamemodes[gamemodes.keys()[int(raw_input(">"))]])

# Select mode
ir=raw_input("Choose [I]nstagib, [R]ockets or [N]one\n>").lower()
if ir=="i": configfile.write("set g_instantgib 1\n")
elif ir=="r": configfile.write("set g_rockets 1\n")
else: configfile.write("set g_rockets 0\nset g_rockets 0\n")

# Vampire and health settings
if raw_input("Randomize vampire and health settings? (y/n)\n>")=="y":
  if yesno(): configfile.write("set g_vampire %f\n"%(random.randint(0,100)/80.))
  configfile.write("set g_vampire_max_health %i\n"%random.randint(100,600))
  if yesno(): configfile.write("set g_regen %f\n"%(random.randint(0,50)/10.))

# Misc game settings
if raw_input("Randomize misc settings? (y/n)\n>")=="y":
  configfile.write("set g_awardpushing %i\n"%yesno())
  configfile.write("set g_speed %i\n"%random.randint(250,420))
  configfile.write("set g_knockback %i\n"%random.randint(700,1200))
  configfile.write("set g_gravity %i\n"%random.randint(650,950))
  configfile.write("set g_respawntime %i\n"%random.randint(1,10))
  configfile.write("set g_quadfactor %f\n"%(random.randint(10,50)/10.))
  configfile.write("set g_damagemodifier %f\n"%(random.randint(5,30)/10. if yesno() else 1.))

# Randomize removal of items from arena
randitems=raw_input("Randomize item restrictions? (y/n)\n>").lower()
for i in weaponres:
  configfile.write("set disable_%s '%i'\n"%(i,yesno() if randitems=="y" else 0))

# Temporary settings (Bots for testing, etc)
configfile.write("set bot_minplayers 4")
configfile.write("set bot_nochat 1")


configfile.close()