import tracery
from tracery.modifiers import base_english

rules = {
    'prompt': '#setting#, #modifiers#, #modifiers#, #modifiers#',
    'setting': ['#cosy#', '#place#', '#countryside#', '#train#', '#cityscene#'],
    'cosy': ['cosy scene #time#', 'a hot cup of tea, #weather# outside', 'looking out the window at #city# #time#'],
    'countryside': ['#country# #time#', '#weather# #country# #time#', '#country#'],
    'train': ['#transit# #time#', '#weather# #transit# #time#'],
    'transit': ['train station', 'an old bus stop', 'rail station', 'subway station'],
    'time': ['at night', 'at sunrise', 'at dusk', 'at midnight', 'midday'],
    'weather': ['rainy', 'cloudy', 'foggy', 'clear', 'overcast'],
    'city': ['Tokyo', 'Sydney', 'Paris', 'Kyoto', 'Chicago', 'New York', 'San Francisco', 'Reykjavik', 'Hanoi', 'Hong Kong', 'London', 'Madrid', 'Barcelona', 'Prague', 'Santa Fe', 'Portland', 'New Orleans'],
    'cityscene': ['#place# in #city# #time#', '#weather# #place# in #city#', '#place# #time#'],
    'place': ['art museum', 'old diner', 'fancy restaurant', 'abandoned storefront', 'alleyway', 'dive bar', 'post office', 'cosy cabin', 'hotel', 'covered bridge', 'waterfront', 'pier', 'street scene'],
    'country': ['lakeside dock', 'deep in the woods', 'hillside', 'deer trail', 'hiking trail', 'mountain overlook', 'mountain pass', 'riverbank', 'forest glen', 'meadow'],
    'modifiers': ['detailed', 'trending on artstation', '4k', 'highly realistic', 'fantasy vivid colors', 'ghibli inspired', 'studio ghibli', 'anime', 'anime art style', 'anime concept art', 'vivid colors', 'bokeh', 'aesthetic', 'trending on cgsociety', 'cinematic',]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

print(grammar.flatten("#prompt#"))
