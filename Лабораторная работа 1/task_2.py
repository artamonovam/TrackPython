kol = 100
num_str = 50
kol_smb = 25

inf_ob = 1.44


a = kol * num_str * kol_smb * 4
b = inf_ob * 1024 * 1024 / a

print("Количество книг, помещающихся на дискету:", int(b))
