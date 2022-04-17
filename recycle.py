## Ruins of Chaos Recycle Calculator ##

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

def weapon_type(num):
    if 1:
        return 1
    elif range(2, 3):
        return 0.8
    elif 4:
        return 0.6

sov = input("Enter Sell Off Value (SoV) here: ")
print("SoV:", int(sov))
num_spies = input("# of spies enemy sabber used (1-25): ")
print("# of spies:", int(num_spies))
aat = calc_aat_percent(int(num_spies))
print("AAT:", aat)