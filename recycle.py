## Ruins of Chaos Recycle Calculator ##

## Example Calculation: 
# SoV: 101104137750
# Max AAT: (SoV * 0.002) -> (101104137750 * 0.002)
# AAT %: 0.44 (1 Spy)
# Weapon Category: Sentry (4)
# Number of Successes: 6
# Weapon Cost: Guard Dog #13 -> (100000)
# ((((101104137750 * 0.002) * 0.44) * 0.6) * 6) / 100000 
# Result = 3202.97908392 => 3203

# Calculate % AAT based on # of spies.


def calc_aat_percent(spies):
    if 0 < spies < 4:
        return 0.44
    elif 3 < spies < 10:
        return 0.5
    elif 9 < spies < 15:
        return 0.6
    elif 14 < spies < 21:
        return 0.7
    elif 20 < spies < 24:
        return 0.9
    elif spies == 25:
        return 1

## Weapon Type Multiplier:
# 1 = SA, 2 = DA, 3 = SP, 4 = SE
def weapon_type(num):
    if num == 1:
        return 1
    elif num == 2 or num == 3:
        return 0.8
    elif num == 4:
        return 0.6

## Weapon Cost
# 1 = Dagger
# 2 = Maul 
# 3 = Blade 
# 4 = Excalibur 
# 5 = Sai 
# 6 = Shield 
# 7 = Mithril 
# 8 = Dragonskin 
# 9 = Cloak 
# 10 = Hook 
# 11 = Pickaxe 
# 12 = Horn 
# 13 = Guard Dog 
# 14 = Torch
def weapon_cost(num):
    if num == 1 or num == 5:
        return 1000
    if num == 2 or num == 6:
        return 15000
    if num == 3 or num == 7:
        return 200000
    if num == 4 or num == 8:
        return 1000000
    if num == 9 or num == 12:
        return 50000
    if num == 10 or num == 13:
        return 100000
    if num == 11 or num == 14:
        return 300000


sov = int(input("Enter Sell Off Value (SoV) here: "))
print("SoV:", sov)
num_spies = int(input("# of spies enemy sabber used (1-25): "))
print("# of spies:", num_spies)
pct_aat = float(calc_aat_percent(int(num_spies)))
print("% AAT:", pct_aat)
in_type = int(input("Input weapon type: "))
wpn_mult = float(weapon_type(in_type))
print("Weapon Type Multiplier: ", wpn_mult)
in_success = int(input("# successes: "))
print("The enemy sabber succeeded", in_success, "times.")
in_cost = int(input("Input weapon cost: "))
wpn_cost = int(weapon_cost(in_cost))
print("Weapon costs", wpn_cost, "gold")
result = (((((sov * 0.002) * pct_aat) * wpn_mult) * in_success) / wpn_cost)
print("RESULT: Recycle", round(result), "weapons.")