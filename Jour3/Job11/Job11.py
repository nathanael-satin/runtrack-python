def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60

    temps_texte = f"{heures} heures et {minutes_restantes} minutes"
    print(temps_texte)


nombre_de_minutes = 133
time_to_text(nombre_de_minutes)
