import json

# class MushroomSpot(models.Model):

#     title = models.CharField(max_length=256)
#     description = models.TextField()
#     picture = models.ImageField()
#     geom = PointField()

#     def __str__(self):
#         return self.title

#     @property
#     def picture_url(self):
#         return self.picture.url

# "14631": [
#     47.179417, -1.533628,
#     "https://s3-eu-west-1.amazonaws.com/media-zerogachis/thumbnails/cf/30/cf302691ffe486961058301e574caf49.png",
#     2.065675,
#     "intermarche_super_reze_14631",
#     "/fr/listing-magasins/intermarche_super_reze_14631/"
# ],


#   {
#     "model": "myapp.person",
#     "pk": 1,
#     "fields": {
#       "first_name": "John",
#       "last_name": "Lennon"
#     }
#   },

newdatas = []
newdatadict = {}
newfields = {}

with open('marker.json') as json_file:
    data = json.load(json_file)


for name,item in data.items():
    newdatadict['model'] = 'zerogachis.ZerogachisSpot'
    newdatadict['pk'] = name
    value = item[4].replace('_',' ').split()
    marque =''
    if value[0] == 'auchan':
        marque = value[0] 
    else:
        marque = value[0] + ' ' + value[1]

    newfields['title'] = marque
    newfields['description'] = " ".join(value[2:])
    newfields['picture'] = item[2]
    newfields['partenaire'] = True
    newfields['geom'] = {'type': 'Point', 'coordinates': [item[1], item[0]]}
    newdatadict['fields'] = newfields
    newdatas.append(newdatadict)
    newdatadict = {}
    newfields = {}

with open('data.json', 'w') as outfile:
    json.dump(newdatas,  outfile ,indent=4 )