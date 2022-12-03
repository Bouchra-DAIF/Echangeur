print("L'échangeur")
Tce=input("Entrez la température chaud d'entrer: ")
Tcs=input("Entrez la température chaud de sorter: ")
Tfe=input("Entrez la température froid d'entre: ")
Tfs=input("Entrez la température froid de sorter: ")
try:
    Tce=float(Tce)
    Tcs=float(Tcs)
    Tfe=float(Tfe)
    Tfs=float(Tfs)
    DeltaT1 = ((Tcs - Tfs) - (Tce - Tfe)) / (ln((Tcs - Tfs) / (Tce - Tfe)))
    print("Le DLTM DANS LE CAS DE CO-COURANT EST ", DeltaT1)
    DeltaT2 = ((Tcs - Tfe) - (Tce - Tfs)) / (ln((Tcs - Tfe) / (Tce - Tfs)))
    print("Le DLTM DANS LE CAS DE CONTRE-COURANT EST ", DeltaT2)
except:
    print("erreur")

