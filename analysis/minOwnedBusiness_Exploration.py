#DATA SET FROM: https://www.opendataphilly.org/dataset/office-of-economic-opportunity-registration
import pandas as pd
import numpy
import matplotlib.pyplot as plt

df = pd.read_csv('oeo_registry.csv')

##find the number of MOB in PA and neighboring states
#print(df['physical_address_state'].unique())
mob_in_states = df[df.physical_address_state.isin(
    ['PA', 'NY', 'WV', 'MD', 'DE', 'NJ'])]

#print(mob_in_states[['company_name', 'physical_address_state']])

##find biz in the food/snack/beverage industry (capability)
searchwords = ['grocery', 'food', 'produce', 'mart', 'edible']
#convert 'capabilities' column to all lower case
#mob_in_states['capability'] = mob_in_states['capability'].str.lower().contains(searchwords) 

keyWords = "Grocery, food, mart, edible, WIC, WICcash, SFMNP, SNAP, Organic, Baked Goods, Bakedgoods, Cheese, Crafts, Flowers, Eggs, Seafood, Herbs, Vegetables, Honey, Jams, Maple, Meat, Nursery, Nuts, Plants, Poultry, Prepared, Prepared Foods, Soap, Trees, Wine, Coffee, Beans, Fruits, Grains, Juices, Mushrooms, Pet, Petfood, Pet food, Tofu, Wild Harvested, WildHarvested, Fair Trade, Flour, Bakery, Farmer, Sugar, Spices, Candy, dry goods, supplement, agriculture, f&b, food and beverage, store, dairy, floral, wellness, gluten free, meat & seafood, deli, massage oil, sunscreen, baby care, facial care, dietary, homeopathic, lotion, lotions, oils, hair care, vitamins, bug repellant, dog food, cat food, cat litter, kosher, halal, chocolate, chocolates, snack, vegan, non-gmo, refrigerated, frozen, soup, sauces, dips, desserts, canned, fully-cooked, chicken, sausage, pork, turkey, beans, fresh-cut, fresh"
keyWordsBar = keyWords.replace(", ", "|")
print(keyWordsBar)

food = mob_in_states[mob_in_states['capability'].str.contains(keyWordsBar , na = False, regex = True)]
#pd.set_option("display.max_colwidth", -1)
pd.set_option('display.max_rows', None)
print(food[['company_name', 'physical_address_state', 'capability']])

food.to_csv('/Users/thatcass/DS4A2/ds4a-team/data/minority_owned_biz/food.csv', index = False)


#for category in searchwords:

#    mob_in_states[category] = mob_in_states.astype(str).sum(axis=1).str.contains(category)


