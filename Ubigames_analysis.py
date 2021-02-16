from Ubigames_scraping import *
import pandas as pd
import matplotlib.pyplot as plt

"""
Analysis of the data collected in Ubigames_scraping 

note : due to what I believe to be a filter error, some games are in the wrong order. 
I therefore chose to analyse only a sample containing the 12 first games
"""

UGNames = CreateUbiGames.Names[-12:] #UG = Ubisoft games
UGPrices = CreateUbiGames.Prices[-12:]
UGEditions = CreateUbiGames.Editions[-12:]
UGDiscounts = CreateUbiGames.Discounts[-12:]
UbiGames = []

for index,p in enumerate(UGPrices):
	p = float(p.split()[0].replace(',','.'))
	UGPrices[index] = p

#for index,p in enumerate(UGDiscounts):

for index,p in enumerate(UGDiscounts):
	UGDiscounts[index] = int(p[1:3])

for i in range(len(UGNames)):
	UbiGames.append(UGNames[i] + ' - ' + UGEditions[i])

UGGamesDf = pd.DataFrame({'Games':UbiGames,'Names':UGNames,'Editions':UGEditions,'Prices':UGPrices,'Discounts':UGDiscounts})


plt.figure(1)
plt.bar('Games','Prices',data=UGGamesDf.sort_values('Prices',ascending=False))
plt.xticks(rotation=-90)
plt.title("Ubisoft Games sorted by prices",size=20)


plt.figure(2)
plt.bar('Games','Discounts',data=UGGamesDf.sort_values('Discounts',ascending=False))
plt.xticks(rotation=-90)
plt.title("Ubisoft Games sorted by discounts",size=20)
plt.show()