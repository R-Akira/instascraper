from igcleaner2 import f_clean
import os


os.chdir("/Users/user/Desktop/Belift/csv")

lst = [
    'adelleodelia',
    'agatha_chelsea',
    'angelinengel',
    'ariefmuhammad',
    'celinesutedja',
    'claurakiehl',
    'elizabethkasai',
    'ernestprakasa',
    'gitagut',
    'jessicatanoe',
    'jovialdalopez',
    'karbearv',
    'latashasafira',
    'marioatmadji',
    'mikhelia',
    'muhammadaga',
    'olvaholvah',
    'rhenopoetiray',
    'ryanwibawa',
    'tasyakamila',
    'vaelovexia'
]

for i in lst:
    f_clean(i)

    print(f"""cleaning {i} completed!""")
