
# ({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
# ('player3', 100)



def orangecap(d):
    players = {"topscorer":["",0]}
    t = [0]
    for i in d:
        for j  in d[i]:
            if j in players:
                players[j] = players[j]+d[i][j]
                if players[j]+d[i][j]>max(t):
                    players["topscorer"][0] = j
                    players["topscorer"][1] = players[j]
            else:
                players[j] = d[i][j]
    return tuple(players["topscorer"])
                
print(orangecap({'test1':{'Pant':84, 'Kohli':120}, 'test2':{'Pant':59, 'Gill':42}}))

