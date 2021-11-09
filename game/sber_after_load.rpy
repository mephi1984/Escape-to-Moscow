label after_load:

    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("stopAllMusic()")
        if last_playing_music != "":
            $ emscripten.run_script(last_playing_music)

    return
