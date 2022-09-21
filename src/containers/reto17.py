ACTIONS_ACCEPTED = ["run", "jump"]
TRACK_ACCEPTED = ["_", "|"]

def race(actions: list[str], track: str):
    # Variables
    race_clear = True
    track_ended = ""

    # Si el largo de la pista es 0 y no se tienen acciones, retorna True
    if len(track) == 0 and len(actions) == 0:
        return race_clear

    # En el caso de que exista una pista y no se den acciones, retorna False
    elif len(track) > 0 and len(actions) == 0:
        return not race_clear

    # Itera de acuerdo al largo de la pista
    for i in range(len(track)):
        track_type = track[i]

        # Si la pista es más larga que las acciones utiliza la última acción dada
        if i >= len(actions):
            action_type = actions[-1].lower()
        else:
            action_type = actions[i].lower()


        # Si la acción o el tramo de pista no se encuentra en las opciones disponibles, marca tramo como error.
        if track_type not in TRACK_ACCEPTED or action_type not in ACTIONS_ACCEPTED:
            track_ended += "E"
            race_clear = False

        # En el caso de que se salte en una pista lisa, se marca tramo como "x".
        elif track_type == "_" and action_type == "jump":
            track_ended += "x"
            race_clear = False

        # De correr en un tramo con valla, se marca tramo como "/".
        elif track_type == "|" and action_type == "run":
            track_ended += "/"
            race_clear = False

        # De no ocurrir ningún error en el tramo, se toma como correcto.
        else:
            track_ended += track[i]


    print(f"Track Finished: {track_ended}")

    return race_clear



# Tests
race(["run", "jump", "run"], "_|_")
race(["run", "jump", "run", "jump", "run"], "_|_")
race(["swim", "dance", "correr"], "___")
race(["run", "jump", "run"], "__|_|_|_")
race(["run"], "____________")
race(["jump"], "______|______")