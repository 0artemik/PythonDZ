ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"

shot = input("Введите координату: ")

ship_lower = ship.lower()
shot_lower = shot.lower()

if ship_lower.find(shot_lower) != -1:
    print("Попадание")
else:
    print("Промах")
