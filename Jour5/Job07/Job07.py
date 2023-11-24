def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40:
            multiple_de_5_superieur = ((note + 2) // 5) * 5  
            if multiple_de_5_superieur - note < 3: 
                notes_arrondies.append(multiple_de_5_superieur) 
            else:
                notes_arrondies.append(note) 
        else:
            notes_arrondies.append(note)  
    return notes_arrondies
liste_notes = [83, 62, 45, 37, 90, 29]
notes_arrondies = arrondir_notes(liste_notes)
print("Notes initiales :", liste_notes)
print("Notes arrondies :", notes_arrondies)