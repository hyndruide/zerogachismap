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

with open('zero-gachis.com.json') as json_file:
    data = json.load(json_file)["objects"]


for item in data:
    newdatadict['model'] = 'zerogachis.ZerogachisSpot'
    newdatadict['pk'] = item["id"]
    newfields['title'] = item["enseigne"]["nom"]
    if item["adresse1"] is None:
        item["adresse1"] = "Magazin"
    newfields['description'] = item["adresse1"]
    newfields['picture'] = "https://static-zerogachis.s3-eu-west-1.amazonaws.com/markers/images/green-icon.png"
    newfields['partenaire'] = False
    newfields['geom'] = {'type': 'Point', 'coordinates': [item["longitude"], item["latitude"]]}
    newdatadict['fields'] = newfields
    newdatas.append(newdatadict)
    newdatadict = {}
    newfields = {}

with open('datanonpart.json', 'w') as outfile:
    json.dump(newdatas,  outfile ,indent=4 )