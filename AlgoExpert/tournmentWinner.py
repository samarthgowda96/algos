from collections import Counter 
def tournamentWinner(competitions, results):
    points = {}
    for i in range(len(results)):
        
        if results[i] == 0:
            
            
            if competitions[i][1] not in points:
               
                points[competitions[i][1]] = 3
            else:
                points[competitions[i][1]] += 3

        elif results[i] == 1:
            print(i)
            
            if competitions[i][0] not in points:
                print(competitions[i][0])
                points[competitions[i][0]] = 3
            else:
                points[competitions[i][0]] += 3
    
    highest = dict(sorted(points.items(), key=lambda item: item[1], reverse=True))

    return list(highest.keys())[0]
  

comp = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]
res =  [0, 0, 1]

print(tournamentWinner(comp, res))
