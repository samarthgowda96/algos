def HA(activity):
    loginSum=0
    logoutSum=0
    startVideoSum=0
    stopVideoSum=0
    for i in activity:
        if(i[1]=="@login"):
            loginSum+=i[0]
        elif(i[1]=="@logout"):
            logoutSum+=i[0]
        elif(i[1]=="@startVideo"):
            startVideoSum+=i[0]
           
        else:
            stopVideoSum+=i[0]

        
    loggedTime= abs(logoutSum-loginSum)
    streamedTime=abs(stopVideoSum-startVideoSum)
    print("the duration of this example HA's logged in time is",loggedTime)
    print("the duration of this example HA's time spent simultaneously streaming video with two clients is",streamedTime)

activity = [(1, '@login', None),
(5, '@startVideo', 'Bob'),
(20, '@startVideo', 'Thomas'),
(66, '@stopVideo', 'Thomas'),
(70, '@startVideo', 'Lily'),
(75, '@stopVideo', 'Bob'),
(78, '@stopVideo', 'Lily'),
(100, '@logout', None),
(150, '@login', None),
(160, '@startVideo', 'Thomas'),
(205, '@stopVideo', 'Thomas'),
(210, '@logout', None) ]
HA(activity)