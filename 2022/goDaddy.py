""" GoDaddy makes a lot of different top-level domains available to its customers. A top-level domain is one that goes directly after the last dot ('.') in the domain name, for example .com in example.com. To help the users choose from available domains, GoDaddy is introducing a new feature that shows the type of the chosen top-level domain. You have to implement this feature.
To begin with, you want to write a function that labels the domains as "commercial", "organization", "network" or "information" for .com, .org, .net or .info respectively.
For the given list of domains return the list of their labels. """

def solution(domains):
    res = []
    topLevelDoms = {"com" : "commercial", "org":"organization", "net":"network", "info":"information"}
    for i in domains:
        temp = i.split('.')
        dom = temp[len(temp)-1]
        if dom in topLevelDoms:
                res.append(topLevelDoms[dom])
    return res

domains = ["en.wiki.org", "codesignal.com", "happy.net", "code.info"]

print(solution(domains))
