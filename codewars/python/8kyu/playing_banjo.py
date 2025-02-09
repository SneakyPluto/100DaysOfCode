def are_you_playing_banjo(name):
    # Implement me!
    if name.startswith("R") or name.startswith("r"):
        return name + " plays banjo"
    else:
        return name +  " does not play banjo"
    
#You have passed all of the tests! :)

#Alternative solution
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
