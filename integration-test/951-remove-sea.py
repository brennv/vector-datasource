# Drop sea polygon but keep the label

# http://www.openstreetmap.org/relation/4594226
assert_no_matching_feature(
    12, 2315, 1580, 'water',
    {'id': -4594226, 'kind': 'sea', 'label_placement': None})

assert_has_feature(
    9, 292, 197, 'water',
    {'id': -4594226, 'kind': 'sea', 'label_placement': True})

assert_has_feature(
    12, 2338, 1579, 'water',
    {'id': -4594226, 'kind': 'sea', 'label_placement': True})
