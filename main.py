

def nitro_salt(meat_mass):
    try:
        salt_mass=int(int(meat_mass)/100)
    except:
        salt_mass=0
    return salt_mass
