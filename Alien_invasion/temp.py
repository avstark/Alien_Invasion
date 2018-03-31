import shelve
shelf=shelve.open('highscore')
shelf['score']=str(0)
shelf.close()
