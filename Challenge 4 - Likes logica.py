theseNames1 = []
theseNames2 = ['Jeroen']
theseNames3 = ['Jan','Lars']
theseNames4 = ['Kees','Beth','Joris']
theseNames5 = ['Hans','Ivan','Sara', 'Hamid', 'Omar', 'Demiën']
theseNames6 = [] 
for i in range(1,41): theseNames6.append(f'name{i}')

def likes(names):
    if not names:
        return "no one likes it"
    elif len(names) == 1:
        return f"{names[0]} likes it"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like it"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like it"
    elif len(names) < 20:
        return f"{', '.join(names[:-1])} and {names[-1]} like it"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like it"

print(likes(theseNames1))
print(likes(theseNames2))
print(likes(theseNames3))
print(likes(theseNames4))
print(likes(theseNames5))
print(likes(theseNames6))



