d = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
d[5]= {1:2,3:4}
print(d)
d['key1']['d'] = d['key2']
print(d)


info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

color = info['personal_data']['physical_features']['color']