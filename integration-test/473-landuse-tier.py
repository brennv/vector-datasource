from . import FixtureTest


class LanduseTier(FixtureTest):
    def test_large_national_park(self):
        # area 1.75564e+10
        self.load_fixtures(['http://www.openstreetmap.org/relation/1453306'])

        self.assert_has_feature(
            4, 3, 5, 'landuse',
            {'kind': 'national_park', 'id': -1453306, 'tier': 1,
             'min_zoom': 3})

        self.assert_has_feature(
            6, 12, 23, 'pois',
            {'kind': 'national_park', 'id': -1453306, 'tier': 1,
             'min_zoom': 3.74})

    def test_national_park(self):
        # area 30089300
        self.load_fixtures(['http://www.openstreetmap.org/relation/921675'])

        self.assert_has_feature(
            8, 56, 115, 'landuse',
            {'kind': 'national_park', 'tier': 1, 'min_zoom': 8})

        self.assert_has_feature(
            8, 56, 115, 'pois',
            {'kind': 'national_park', 'id': -921675, 'tier': 1,
             'min_zoom': 8.33})

    def test_national_forest(self):
        # this is USFS, so demoted to tier 2 :-(
        # area 86685400
        self.load_fixtures(['http://www.openstreetmap.org/way/34416231'])

        self.assert_has_feature(
            8, 71, 98, 'landuse',
            {'kind': 'forest', 'id': 34416231,
             'tier': 2, 'min_zoom': 8})

        # this one is clipped by the polygon min_zoom, and so appears at the
        # same level.
        #
        # note that the feature _is_ present in the zoom 8 tile, but gets
        # merged with a nearby feature of the same name, so instead we test
        # this at z9.
        self.assert_has_feature(
            9, 142, 196, 'pois',
            {'kind': 'forest', 'id': 34416231,
             'tier': 2, 'min_zoom': 8})
