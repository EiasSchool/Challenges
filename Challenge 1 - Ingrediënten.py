aantalpersonnen = int(input('Hoeveel personnen?\n'))

#per persoon
komkommer = 1 / 4
fijn_zeezout = 1 / 4
knoflook = 1 / 2
verse_dille = 3.75
griekse_yoghurt = 125
wittewijnazijn = 1 / 4
extra_vierge_olijfolie = 3 / 4

#berekeningen
totaal_komkommer = aantalpersonnen * komkommer
totaal_fijn_zeezout = aantalpersonnen * fijn_zeezout
totaal_knoflook = aantalpersonnen * knoflook
totaal_verse_dille = aantalpersonnen * verse_dille
totaal_griekse_yoghurt = aantalpersonnen * griekse_yoghurt
totaal_wittewijnazijn = aantalpersonnen * wittewijnazijn
totaal_extra_vierge_olijfolie = aantalpersonnen * extra_vierge_olijfolie

print(f'''
{aantalpersonnen} Personen
{totaal_komkommer} komkommer
{totaal_fijn_zeezout} mespunt fijn zeezout
{totaal_knoflook} knoflook
{totaal_verse_dille}g verse dille
{totaal_griekse_yoghurt}ml Griekse yoghurt 10%
{totaal_wittewijnazijn}el wittewijnazijn
{totaal_extra_vierge_olijfolie}el extra vierge olijfolie
''')