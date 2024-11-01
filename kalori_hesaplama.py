# Erkekler için bazal metabolizma hızı = 66.5 + (13.75 x vücut ağırlığınız (kg)) + (5 x boyunuz (cm.)) - (6.77 x yaş)
# Kadınlar için bazal metabolizma hızı = 655.1 + (9.56 x vücut ağırlığınız (kg)) + (1.85 x boyunuz (cm.)) - (4.67 x yaş)

cinsiyet = input("Cinsiyetinizi Kadın ise K  Erkek İse E olarak giriniz")
kilo = int(input("Kilonuzu Giriniz"))
boy = int(input("Boyunuzu cm olarak giriniz"))
yas = int(input("Yaşınızı giriniz"))
bazal_erkek = 66 + (13.75 * kilo) + (5 * boy) - (6.77 * yas)
bazal_kadin = 655 + (9.56 * kilo) + (1.85 * boy) - (4.67 * yas)
if cinsiyet == "E":
    print(f"Bazal Kaloriniz {bazal_erkek}")
else:
    print(f"Bazal Kaloriniz {bazal_kadin}")
    