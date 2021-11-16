label after_load:

    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("stopAllMusic()")
        $ emscripten.run_script("music_stage_preload = \"" + music_stage_preload + "\"")
        $ emscripten.run_script("currentPlaySong = \"\"")
        $ emscripten.run_script("clearAllMusicExceptPreload()")
        $ emscripten.run_script("PreloadRequiredTracksAfterLoadGame(" + last_playing_music +")")
        #if last_playing_music != "":
        #    $ emscripten.run_script(last_playing_music)

    return
