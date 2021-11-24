import twint 

search = input("What your search? ")
country = input("where? ")
city = input("where? ")

c = twint.Config()
c.Search = search 
c.Near = country
c.Near = city
c.Limit = 10
c.Populat_tweets = true

twint.run.Search(c)
