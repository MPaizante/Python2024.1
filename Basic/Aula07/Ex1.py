olympics = ('Beijing','London','Rio','Tokyo')

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = []
for i in tuples_lst:
    country.append(i[1])

olymp = ('Rio', 'Brazil', 2016)
city , country , year =olymp[0],olymp[1],olymp[2]


def info(name, gender, age, bday_month,hometown):
    return name, gender, age, bday_month,hometown


gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals = []

for i,k in gold.items():
    num_medals.append(k)

