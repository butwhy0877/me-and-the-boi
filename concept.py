# stats mock-up 

# temporary value
very_low = (20)
low = (40)
medium_low = (60)
medium = (80)
medium_high = (100)
high = (120)
very_high = (140)

# toughness=attack(physical)
# fortitude=recovery+defense/confidence
# intelligence=counterattack/quick reflex(defense)
# charisma=influencial power, support
# wealth=money

# dictionary of aaron's stats

aaron = {
	"toughness": medium_high,
	"fortitude": medium_high,
	"wealth": medium,
	"charisma": medium_high,
	"intelligence": medium
}
print(aaron)
print(aaron["wealth"])
baaron = aaron["wealth"] - 50
print(baaron)

 
# ego system(bullshit system)
# bullshit defense value ranges from (lowest)8-2(highest)
# > avoids very high bullshit character from one shot-ting low value bullshitter
# bullshit result times bullshit attack value is health points
# bullshit health points plus 200 ego points
# lowest possible value= 360
# highest possible value= 480
# *for ego system*(affected by charisma debuff)

	
