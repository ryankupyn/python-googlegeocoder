#!/usr/bin/env python
import unittest
from googlegeocoder import *
from pprint import pprint


class BaseTest(unittest.TestCase):
    
    def setUp(self):
        self.geocoder = GoogleGeocoder()

class GoogleTest(BaseTest):
    
    def test_search(self):
        result = self.geocoder.get("Winnetka")
        self.assertEqual(type(result[0]), GeocoderResult)
    
    def test_result_attributes(self):
        result = self.geocoder.get("Winnetka")[0]
        self.assertEqual(type(result.address_components), type([]))
        [self.assertEqual(type(i), AddressComponent) for i in result.address_components]
        [self.assertEqual(type(i.long_name), type(u"")) for i in result.address_components]
        [self.assertEqual(type(i.short_name), type(u"")) for i in result.address_components]
        [self.assertEqual(type(i.types), type([])) for i in result.address_components]
        self.assertEqual(type(result.formatted_address), type(u""))
        self.assertEqual(type(result.types), type([]))
        self.assertEqual(type(result.geometry), Geometry)
        self.assertEqual(type(result.geometry.location), Coordinate)
        self.assertEqual(type(result.geometry.location_type), type(u""))
        self.assertEqual(type(result.geometry.viewport), Bounds)
        self.assertEqual(type(result.geometry.bounds), Bounds)
        self.assertEqual(type(result.geometry.partial_match), type(True))
     
    def test_viewport_bias(self):
        result = self.geocoder.get("Winnetka", 
            bounding_box=((34.172684,-118.604794), (34.236144,-118.500938)))
        self.assertEqual(result[0].formatted_address, 
            u'Winnetka, Los Angeles, CA, USA')
    
    def test_region_bias(self):
        result = self.geocoder.get("Toledo", region='ES')
        self.assertEqual(result[0].formatted_address, u'Toledo, Spain')

if __name__ == '__main__':
    unittest.main()
