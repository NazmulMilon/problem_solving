
# Efficiency= O(n)
def example1(manatees):
    for manatee in manatees:
        print(manatee['name'])

# Efficiency= O(1)
def example2(manatees):
    print(manatees[0]['name'])
    print(manatees[0]['age'])

# Efficiency= O(n*m)
def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print(manatee_property, ": ", manatee[manatee_property])

# Efficiency= O(n^2)
def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print(oldest_manatee)