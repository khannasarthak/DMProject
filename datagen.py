# coding=utf-8
from faker import Factory
import pandas as pd
import random
fake = Factory.create()

def createNames(n):
    names = []
    for _ in range(0,n):
        names.append(str(fake.name()))
    return names
def createProfile(n):
    customer = []
    for _ in range(0,n):
        customer.append(fake.profile(fields=None, sex=None))
    return customer
def cc(n):
    cc = []
    for _ in range(0, n):
        cc.append(fake.credit_card_number(card_type=None))
    return cc

def location(n):
    loc = []
    for _ in range(0, n):
        loc.append(str(fake.secondary_address()))
    return loc
def locName(n):
    name = []
    for _ in range(0, n):
        name.append(str(fake.city()))
    return name

def createSize(n):
    s=[]
    for _ in range(0,n):
        s.append((fake.random_int(min=4000, max=9999)))
    return s

def createGreenroom(n):
    s=[]
    for _ in range(0,n):
        s.append((fake.random_int(min=1, max=10)))
    return s

def createShow(n):
    name = []
    for _ in range(0, n):
        name.append(str(fake.city()))
    return name

def createDate(n):
    s=[]
    for _ in range(0,n):
        s.append((fake.random_int(min=1990, max=2017)))
    return s



def generateCustomerCSV(n):
    a = createProfile(n)
    credit = cc(n)
    df = pd.DataFrame(a)
    df['payment_details'] = credit
    ids=[]
    for _ in range(1,n+1):
        ids.append(_)
    df['customer_id'] = ids
    customer = pd.DataFrame()
    customer = df[['customer_id','name','ssn','mail','payment_details']]
    customer = customer.rename(columns={"ssn": "phone_no", "mail": "email_id"})
    print (customer)
    customer.to_csv('customer.csv', sep = ',', quotechar='"',index=False)
def generateHallCSV(n):
    df = pd.DataFrame()
    ids=[]
    capacity =[]
    availability_label =[]
    for _ in range(1,n+1):
        ids.append(_)
        capacity.append(100)
        availability_label.append('YES')
    df['hall_id'] = ids
    df['capacity'] = capacity
    df['availability_label']=availability_label
    l = location(n)
    n = locName((n))
    df['location'] = l
    df['name_hall'] = n
    print (df)
    df.to_csv('hall.csv', sep = ',', quotechar='"',index=False)

def generateScreenCSV(n):
    df = pd.DataFrame()
    ids=[]
    s = createSize(n)
    type =[]
    experience =[]
    t=['Dome','Flat','Curve']
    e= ['2D','3D','4D']
    for _ in range(1,n+1):
        ids.append(_)
        type.append(random.choice(t))
        experience.append(random.choice(e))
    df['hall_id'] = ids
    df['size'] = s
    df['type']= type
    df['experience'] = experience
    print (df)
    df.to_csv('screen.csv', sep = ',', quotechar='"',index=False)

def generateAuditoriumCSV(n):
    df = pd.DataFrame()
    ids=[]
    s = createSize(n)
    greenrooms = createGreenroom(n)
    for _ in range(n+1,1001):
        ids.append(_)

    df['hall_id'] = ids
    df['stage_size'] = s
    df['no_of_green_rooms'] = greenrooms
    print (df)
    df.to_csv('auditorium.csv', sep = ',', quotechar='"',index=False)

def generateShowCSV(n):
    df = pd.DataFrame()
    ids=[]
    s = createShow(n)

    for _ in range(1,n+1):
        ids.append(_)

    df['show_id'] = ids
    df['show_name'] = s

    print (df)
    df.to_csv('shows.csv', sep = ',', quotechar='"',index=False)

def generatePerformancesCSV(n):
    df = pd.DataFrame()
    ids = []
    performers = createNames(n)
    performance_type =[]
    p = ['Play', 'Drama', 'Opera','Dance', 'Magic Show']
    for _ in range(n+1, 1001):
        ids.append(_)
        performance_type.append(random.choice(p))
    df['show_id'] = ids

    df['performers'] = performers
    df['performance_type'] = performance_type
    print(df)
    df.to_csv('performances.csv', sep=',', quotechar='"', index=False)

def generateMoviesCSV(n):
    df = pd.DataFrame()
    ids = []
    cast = createNames(n)

    releaseDate = createDate(n)
    director = createNames(n)
    rating =[]
    r = ['R', 'PG-13', 'A','U', 'PG-16']
    for _ in range(1, n+1):
        ids.append(_)
        rating.append(random.choice(r))
    df['show_id'] = ids
    df['movie_cast'] = cast
    df['release_date'] = releaseDate
    df['director'] = director
    df['rating'] = rating
    print(df)
    df.to_csv('movies.csv', sep=',', quotechar='"', index=False)




# generateMoviesCSV(500)


# def megacreate():
#     generateCustomerCSV(1000)
#     generateHallCSV(1000)
#     generateScreenCSV(500)
#     generateAuditoriumCSV(500)
#     generateShowCSV(1000)
#     generatePerformancesCSV(500)
#     generateMoviesCSV(500)



