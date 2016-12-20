#! /usr/bin/env python

import random

gamemodes={"Deathmatch":0, "Team deathmatch":3, "CTF":4, "Elimination":8, "Last man standing":10}
weaponres=["weapon_shotgun","weapon_grenadelauncher","weapon_rocketlauncher","weapon_lightning","weapon_railgun","weapon_plasmagun","weapon_bfg","weapon_grapplinghook","ammo_shells","ammo_bullets","ammo_grenades","ammo_cells","ammo_lightning","ammo_rockets","ammo_slugs","ammo_bfg","item_armor_shard ","item_armor_combat","item_armor_body","item_health_small","item_health","item_health_large","item_health_mega ","holdable_teleporter","holdable_medkit","item_quad","item_enviro","item_haste","item_invis","item_regen","item_flight"]
yesno=lambda:random.choice([0,1])

configfile=open("./out.cfg","w+")

# Fixed settings
configfile.write("sets sv_hostname 'Servidor Achifaifantastico' \n")
configfile.write("sv_pure 1\n")
configfile.write("seta timelimit 0\n")
configfile.write("seta fraglimit %s\n"%raw_input("Fraglimit?\n>"))

# Vampire and health settings
if raw_input("Randomize vampire and health settings? (y/n)\n>")=="y":
  configfile.write("seta g_vampire %i\n"%yesno())
  configfile.write("seta g_vampire_max_health %i\n"%random.randint(200,600))
  configfile.write("seta g_regen %f\n"%(random.randint(0,50)/10.))
  configfile.write("seta g_quadfactor %f\n"%(random.randint(10,50)/10.))
  configfile.write("seta g_damagemodifier %i\n"%random.randint(300,700))

# Misc game settings
if raw_input("Randomize misc settings? (y/n)\n>")=="y":
  configfile.write("/g_awardpushing %i\n"%yesno())
  configfile.write("seta g_speed %i\n"%random.randint(220,420))
  configfile.write("seta g_knockback %i\n"%random.randint(800,1200))
  configfile.write("seta g_gravity %i\n"%random.randint(650,950))
  configfile.write("seta g_respawntime %i\n"%random.randint(1,5))

# Game mode setting
print "Pick the game mode"
print "\n".join("%i - %s"%(i,s) for i,s in enumerate(gamemodes.keys()))
configfile.write("/g_gametype %s\n"%gamemodes[gamemodes.keys()[int(raw_input(">"))]]+"\n")

# Randomize removal of items from arena
if raw_input("Randomize item restrictions? (y/n)\n>")=="y":
  for i in weaponres:
    configfile.write("seta disable_%s '%i'\n"%(i,yesno()))

# Select mode
ir=raw_input("Choose [I]nstagib, [R]ockets or [N]one\n>").lower()
if ir=="i": configfile.write("/g_instagib 1")
elif ir=="r": configfile.write("/g_rockets 1")
  



configfile.close()