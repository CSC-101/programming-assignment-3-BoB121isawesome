import data
import build_data
import unittest
import hw3

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    # Part 1
    # test population_total
    def test_population_total(self):
        self.assertEqual(318857056,hw3.population_total(full_data))

    def test_population_total_2(self):
        self.assertEqual(655813,hw3.population_total(reduced_data))
    # Part 2
    # test filter_by_state
    def test_filter_by_state(self):
        self.assertEqual([data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA')], hw3.filter_by_state(reduced_data,"CA"))

    def test_filter_by_state_2(self):
        self.assertEqual([data.CountyDemographics(
    {'Percent 65 and Older': 13.8,
     'Percent Under 18 Years': 25.2,
     'Percent Under 5 Years': 6.0},
    'Autauga County',
    {"Bachelor's Degree or Higher": 20.9,
     'High School or Higher': 85.6},
    {'American Indian and Alaska Native Alone': 0.5,
     'Asian Alone': 1.1,
     'Black Alone': 18.7,
     'Hispanic or Latino': 2.7,
     'Native Hawaiian and Other Pacific Islander Alone': 0.1,
     'Two or More Races': 1.8,
     'White Alone': 77.9,
     'White Alone, not Hispanic or Latino': 75.6},
    {'Per Capita Income': 24571,
     'Persons Below Poverty Level': 12.1,
     'Median Household Income': 53682},
    {'2010 Population': 54571,
     '2014 Population': 55395,
     'Population Percent Change': 1.5,
     'Population per Square Mile': 91.8},
    'AL'),], hw3.filter_by_state(reduced_data, "AL"))

    # Part 3
    # test population_by_education
    # test population_by_ethnicity
    # test population_below_poverty_level
    def test_population_by_education(self):
        self.assertAlmostEqual(195114,hw3.population_by_education(reduced_data,"Bachelor's Degree or Higher"),0)
    def test_population_by_education_2(self):
        self.assertAlmostEqual( 566564,hw3.population_by_education(reduced_data,"High School or Higher"),0)

    def test_population_by_ethnicity(self):
        self.assertAlmostEqual(23614,hw3.population_by_ethnicity(reduced_data,"Two or More Races"),0)
    def test_population_by_ethnicity_2(self):
        self.assertAlmostEqual(41181,hw3.population_by_ethnicity(reduced_data,"Asian Alone"),0)

    def test_population_below_poverty(self):
        self.assertAlmostEqual(107712,hw3.population_below_poverty_level(reduced_data),0)
    def test_population_below_poverty_2(self):
        self.assertAlmostEqual(107712,hw3.population_below_poverty_level(reduced_data),0)

    # Part 4
    # test percent_by_education
    # test percent_by_ethnicity
    # test percent_below_poverty_level
    def test_percent_by_education(self):
        self.assertAlmostEqual(29.75,hw3.percent_by_education(reduced_data,"Bachelor's Degree or Higher"),2)
    def test_percent_by_education_2(self):
        self.assertAlmostEqual(86.39,hw3.percent_by_education(reduced_data,"High School or Higher"),2)

    def test_percent_by_ethnicity(self):
        self.assertAlmostEqual(3.60,hw3.percent_by_ethnicity(reduced_data,"Two or More Races"),2)
    def test_percent_by_ethnicity_2(self):
        self.assertAlmostEqual(6.28,hw3.percent_by_ethnicity(reduced_data,"Asian Alone"),2)

    def test_percent_below_poverty(self):
        self.assertAlmostEqual(16.42,hw3.percent_below_poverty_level(reduced_data),2)
    def test_percent_below_poverty_2(self):
        self.assertAlmostEqual(15.37,hw3.percent_below_poverty_level(full_data),2)
    # Part 5
    # test education_greater_than
    # test education_less_than
    # test ethnicity_greater_than
    # test ethnicity_less_than
    # test below_poverty_level_greater_than
    # test below_poverty_level_less_than
    def test_education_greater_than(self):
        expected=[data.CountyDemographics({'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8}, 'San Luis Obispo County', {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6}, {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2, 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2, 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5}, {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697}, {'2010 Population': 269637, '2014 Population': 279083, 'Population Percent Change': 3.5, 'Population per Square Mile': 81.7}, 'CA'),
        data.CountyDemographics({'Percent 65 and Older': 11.5, 'Percent Under 18 Years': 21.7, 'Percent Under 5 Years': 5.8},
                           'Yolo County', {"Bachelor's Degree or Higher": 37.9, 'High School or Higher': 84.3}, {
            'American Indian and Alaska Native Alone': 1.8, 'Asian Alone': 13.8, 'Black Alone': 3.0,
            'Hispanic or Latino': 31.5, 'Native Hawaiian and Other Pacific Islander Alone': 0.6,
            'Two or More Races': 5.0, 'White Alone': 75.9, 'White Alone, not Hispanic or Latino': 48.3}, {
            'Per Capita Income': 27730, 'Persons Below Poverty Level': 19.1, 'Median Household Income': 55918}, {
            '2010 Population': 200849, '2014 Population': 207590, 'Population Percent Change': 3.4,
            'Population per Square Mile': 197.9}, 'CA')]
        self.assertEqual(expected,hw3.education_greater_than(reduced_data,"Bachelor's Degree or Higher",30))
    def test_education_greater_than_2(self):
        expected=[data.CountyDemographics({'Percent 65 and Older': 18.1, 'Percent Under 18 Years': 21.6, 'Percent Under 5 Years': 6.5}, 'Weston County', {"Bachelor's Degree or Higher": 17.2, 'High School or Higher': 90.2}, {'American Indian and Alaska Native Alone': 1.7, 'Asian Alone': 0.4, 'Black Alone': 0.7, 'Hispanic or Latino': 4.2, 'Native Hawaiian and Other Pacific Islander Alone': 0.0, 'Two or More Races': 2.2, 'White Alone': 95.0, 'White Alone, not Hispanic or Latino': 91.5}, {'Per Capita Income': 28764, 'Persons Below Poverty Level': 11.2, 'Median Household Income': 55461}, {'2010 Population': 7208, '2014 Population': 7201, 'Population Percent Change': -0.1, 'Population per Square Mile': 3.0}, 'WY')]
        self.assertEqual(expected,hw3.education_greater_than(reduced_data, "High School or Higher", 90))

    def test_education_less_than(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 15.3, 'Percent Under 18 Years': 25.1, 'Percent Under 5 Years': 6.0}, 'Crawford County', {"Bachelor's Degree or Higher": 14.3, 'High School or Higher': 82.2}, {'American Indian and Alaska Native Alone': 2.5, 'Asian Alone': 1.6, 'Black Alone': 1.6, 'Hispanic or Latino': 6.7, 'Native Hawaiian and Other Pacific Islander Alone': 0.1, 'Two or More Races': 2.8, 'White Alone': 91.5, 'White Alone, not Hispanic or Latino': 85.6}, {'Per Capita Income': 19477, 'Persons Below Poverty Level': 20.2, 'Median Household Income': 39479}, {'2010 Population': 61948, '2014 Population': 61697, 'Population Percent Change': -0.4, 'Population per Square Mile': 104.4}, 'AR')]
,hw3.education_lesser_than(reduced_data,"Bachelor's Degree or Higher",15))
    def test_education_less_than_2(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 11.3, 'Percent Under 18 Years': 33.0, 'Percent Under 5 Years': 10.4}, 'Starr County', {"Bachelor's Degree or Higher": 8.6, 'High School or Higher': 45.0}, {'American Indian and Alaska Native Alone': 0.3, 'Asian Alone': 0.3, 'Black Alone': 0.4, 'Hispanic or Latino': 95.8, 'Native Hawaiian and Other Pacific Islander Alone': 0.0, 'Two or More Races': 0.2, 'White Alone': 98.8, 'White Alone, not Hispanic or Latino': 3.8}, {'Per Capita Income': 11584, 'Persons Below Poverty Level': 39.2, 'Median Household Income': 24927}, {'2010 Population': 60968, '2014 Population': 62955, 'Population Percent Change': 3.3, 'Population per Square Mile': 49.8}, 'TX')]
,hw3.education_lesser_than(full_data,"High School or Higher",50))

    def test_ethnicity_greater_than(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 11.5, 'Percent Under 18 Years': 21.7, 'Percent Under 5 Years': 5.8},'Yolo County', {"Bachelor's Degree or Higher": 37.9, 'High School or Higher': 84.3}, {'American Indian and Alaska Native Alone': 1.8, 'Asian Alone': 13.8, 'Black Alone': 3.0, 'Hispanic or Latino': 31.5, 'Native Hawaiian and Other Pacific Islander Alone': 0.6, 'Two or More Races': 5.0, 'White Alone': 75.9, 'White Alone, not Hispanic or Latino': 48.3}, {'Per Capita Income': 27730, 'Persons Below Poverty Level': 19.1, 'Median Household Income': 55918}, {'2010 Population': 200849, '2014 Population': 207590, 'Population Percent Change': 3.4, 'Population per Square Mile': 197.9}, 'CA')]
, hw3.ethnicity_greater_than(reduced_data, "Two or More Races",4))
    def test_education_greater_than_2(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 6.6, 'Percent Under 18 Years': 10.1, 'Percent Under 5 Years': 2.8}, 'Aleutians East Borough', {"Bachelor's Degree or Higher": 12.0, 'High School or Higher': 78.5}, {'American Indian and Alaska Native Alone': 20.5, 'Asian Alone': 40.7, 'Black Alone': 12.0, 'Hispanic or Latino': 13.2, 'Native Hawaiian and Other Pacific Islander Alone': 0.6, 'Two or More Races': 3.4, 'White Alone': 22.8, 'White Alone, not Hispanic or Latino': 11.5}, {'Per Capita Income': 26535, 'Persons Below Poverty Level': 16.7, 'Median Household Income': 61250}, {'2010 Population': 3141, '2014 Population': 3360, 'Population Percent Change': 7.0, 'Population per Square Mile': 0.4}, 'AK'),data.CountyDemographics({'Percent 65 and Older': 15.8, 'Percent Under 18 Years': 21.5, 'Percent Under 5 Years': 6.5}, 'Honolulu County', {"Bachelor's Degree or Higher": 32.1, 'High School or Higher': 90.3}, {'American Indian and Alaska Native Alone': 0.4, 'Asian Alone': 42.4, 'Black Alone': 3.1, 'Hispanic or Latino': 9.5, 'Native Hawaiian and Other Pacific Islander Alone': 9.4, 'Two or More Races': 21.6, 'White Alone': 23.1, 'White Alone, not Hispanic or Latino': 19.6}, {'Per Capita Income': 30361, 'Persons Below Poverty Level': 9.8, 'Median Household Income': 72764}, {'2010 Population': 953207, '2014 Population': 991788, 'Population Percent Change': 4.0, 'Population per Square Mile': 1586.7}, 'HI')]
, hw3.ethnicity_greater_than(full_data, "Asian Alone",40))

    def test_ethnicity_less_than(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 13.8, 'Percent Under 18 Years': 25.2, 'Percent Under 5 Years': 6.0}, 'Autauga County', {"Bachelor's Degree or Higher": 20.9, 'High School or Higher': 85.6}, {'American Indian and Alaska Native Alone': 0.5, 'Asian Alone': 1.1, 'Black Alone': 18.7, 'Hispanic or Latino': 2.7, 'Native Hawaiian and Other Pacific Islander Alone': 0.1, 'Two or More Races': 1.8, 'White Alone': 77.9, 'White Alone, not Hispanic or Latino': 75.6}, {'Per Capita Income': 24571, 'Persons Below Poverty Level': 12.1, 'Median Household Income': 53682}, {'2010 Population': 54571, '2014 Population': 55395, 'Population Percent Change': 1.5, 'Population per Square Mile': 91.8}, 'AL'),
        data.CountyDemographics({'Percent 65 and Older': 15.3, 'Percent Under 18 Years': 25.1, 'Percent Under 5 Years': 6.9},
                           'Pettis County', {"Bachelor's Degree or Higher": 15.2, 'High School or Higher': 81.8}, {
            'American Indian and Alaska Native Alone': 0.7, 'Asian Alone': 0.7, 'Black Alone': 3.4,
            'Hispanic or Latino': 8.3, 'Native Hawaiian and Other Pacific Islander Alone': 0.3,
            'Two or More Races': 1.9, 'White Alone': 92.9, 'White Alone, not Hispanic or Latino': 85.5}, {
            'Per Capita Income': 19709, 'Persons Below Poverty Level': 18.4, 'Median Household Income': 38580}, {
            '2010 Population': 42201, '2014 Population': 42225, 'Population Percent Change': 0.1,
            'Population per Square Mile': 61.9}, 'MO')]

        , hw3.ethnicity_lesser_than(reduced_data, "Two or More Races",2))
    def test_ethnicity_less_than_2(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 19.6, 'Percent Under 18 Years': 25.6, 'Percent Under 5 Years': 4.9}, 'Butte County', {"Bachelor's Degree or Higher": 17.9, 'High School or Higher': 89.2}, {'American Indian and Alaska Native Alone': 1.0, 'Asian Alone': 0.3, 'Black Alone': 0.2, 'Hispanic or Latino': 5.8, 'Native Hawaiian and Other Pacific Islander Alone': 0.2, 'Two or More Races': 2.3, 'White Alone': 96.1, 'White Alone, not Hispanic or Latino': 90.6}, {'Per Capita Income': 20995, 'Persons Below Poverty Level': 15.7, 'Median Household Income': 41131}, {'2010 Population': 2891, '2014 Population': 2622, 'Population Percent Change': -9.4, 'Population per Square Mile': 1.3}, 'ID'),
        data.CountyDemographics({'Percent 65 and Older': 18.1, 'Percent Under 18 Years': 21.6, 'Percent Under 5 Years': 6.5},
                           'Weston County', {"Bachelor's Degree or Higher": 17.2, 'High School or Higher': 90.2}, {
            'American Indian and Alaska Native Alone': 1.7, 'Asian Alone': 0.4, 'Black Alone': 0.7,
            'Hispanic or Latino': 4.2, 'Native Hawaiian and Other Pacific Islander Alone': 0.0,
            'Two or More Races': 2.2, 'White Alone': 95.0, 'White Alone, not Hispanic or Latino': 91.5}, {
            'Per Capita Income': 28764, 'Persons Below Poverty Level': 11.2, 'Median Household Income': 55461}, {
            '2010 Population': 7208, '2014 Population': 7201, 'Population Percent Change': -0.1,
            'Population per Square Mile': 3.0}, 'WY')]
        , hw3.ethnicity_lesser_than(reduced_data, "Asian Alone",0.5))

    def test_below_poverty_line_greater_than(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 15.3, 'Percent Under 18 Years': 25.1, 'Percent Under 5 Years': 6.0}, 'Crawford County', {"Bachelor's Degree or Higher": 14.3, 'High School or Higher': 82.2}, {'American Indian and Alaska Native Alone': 2.5, 'Asian Alone': 1.6, 'Black Alone': 1.6, 'Hispanic or Latino': 6.7, 'Native Hawaiian and Other Pacific Islander Alone': 0.1, 'Two or More Races': 2.8, 'White Alone': 91.5, 'White Alone, not Hispanic or Latino': 85.6}, {'Per Capita Income': 19477, 'Persons Below Poverty Level': 20.2, 'Median Household Income': 39479}, {'2010 Population': 61948, '2014 Population': 61697, 'Population Percent Change': -0.4, 'Population per Square Mile': 104.4}, 'AR')]
, hw3.below_poverty_level_greater_than(reduced_data,20))
    def test_below_poverty_line_greater_than_2(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 15.3, 'Percent Under 18 Years': 25.1, 'Percent Under 5 Years': 6.0}, 'Crawford County', {"Bachelor's Degree or Higher": 14.3, 'High School or Higher': 82.2}, {'American Indian and Alaska Native Alone': 2.5, 'Asian Alone': 1.6, 'Black Alone': 1.6, 'Hispanic or Latino': 6.7, 'Native Hawaiian and Other Pacific Islander Alone': 0.1, 'Two or More Races': 2.8, 'White Alone': 91.5, 'White Alone, not Hispanic or Latino': 85.6}, {'Per Capita Income': 19477, 'Persons Below Poverty Level': 20.2, 'Median Household Income': 39479}, {'2010 Population': 61948, '2014 Population': 61697, 'Population Percent Change': -0.4, 'Population per Square Mile': 104.4}, 'AR'),
                          data.CountyDemographics({'Percent 65 and Older': 11.5, 'Percent Under 18 Years': 21.7,
                                              'Percent Under 5 Years': 5.8}, 'Yolo County',
                          {"Bachelor's Degree or Higher": 37.9, 'High School or Higher': 84.3},
                          {'American Indian and Alaska Native Alone': 1.8, 'Asian Alone': 13.8, 'Black Alone': 3.0,
                           'Hispanic or Latino': 31.5, 'Native Hawaiian and Other Pacific Islander Alone': 0.6,
                           'Two or More Races': 5.0, 'White Alone': 75.9, 'White Alone, not Hispanic or Latino': 48.3},
                          {'Per Capita Income': 27730, 'Persons Below Poverty Level': 19.1,
                           'Median Household Income': 55918},
                          {'2010 Population': 200849, '2014 Population': 207590, 'Population Percent Change': 3.4,
                           'Population per Square Mile': 197.9}, 'CA')]
        , hw3.below_poverty_level_greater_than(reduced_data,19))

    def test_below_poverty_line_lesser_than(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 18.1, 'Percent Under 18 Years': 21.6, 'Percent Under 5 Years': 6.5}, 'Weston County', {"Bachelor's Degree or Higher": 17.2, 'High School or Higher': 90.2}, {'American Indian and Alaska Native Alone': 1.7, 'Asian Alone': 0.4, 'Black Alone': 0.7, 'Hispanic or Latino': 4.2, 'Native Hawaiian and Other Pacific Islander Alone': 0.0, 'Two or More Races': 2.2, 'White Alone': 95.0, 'White Alone, not Hispanic or Latino': 91.5}, {'Per Capita Income': 28764, 'Persons Below Poverty Level': 11.2, 'Median Household Income': 55461}, {'2010 Population': 7208, '2014 Population': 7201, 'Population Percent Change': -0.1, 'Population per Square Mile': 3.0}, 'WY')]
, hw3.below_poverty_level_lesser_than(reduced_data,12))
    def test_below_poverty_line_lesser_than_2(self):
        self.assertEqual([data.CountyDemographics({'Percent 65 and Older': 13.8, 'Percent Under 18 Years': 25.2, 'Percent Under 5 Years': 6.0}, "Autauga County", {"Bachelor's Degree or Higher": 20.9, 'High School or Higher': 85.6}, {'American Indian and Alaska Native Alone': 0.5, 'Asian Alone': 1.1, 'Black Alone': 18.7, 'Hispanic or Latino': 2.7, 'Native Hawaiian and Other Pacific Islander Alone': 0.1, 'Two or More Races': 1.8, 'White Alone': 77.9, 'White Alone, not Hispanic or Latino': 75.6}, {'Per Capita Income': 24571, 'Persons Below Poverty Level': 12.1, 'Median Household Income': 53682}, {'2010 Population': 54571, '2014 Population': 55395, 'Population Percent Change': 1.5, 'Population per Square Mile': 91.8}, 'AL'),
        data.CountyDemographics({'Percent 65 and Older': 18.1, 'Percent Under 18 Years': 21.6, 'Percent Under 5 Years': 6.5},
                           "Weston County", {"Bachelor's Degree or Higher": 17.2, 'High School or Higher': 90.2}, {
            'American Indian and Alaska Native Alone': 1.7, 'Asian Alone': 0.4, 'Black Alone': 0.7,
            'Hispanic or Latino': 4.2, 'Native Hawaiian and Other Pacific Islander Alone': 0.0,
            'Two or More Races': 2.2, 'White Alone': 95.0, 'White Alone, not Hispanic or Latino': 91.5}, {
            'Per Capita Income': 28764, 'Persons Below Poverty Level': 11.2, 'Median Household Income': 55461}, {
            '2010 Population': 7208, '2014 Population': 7201, 'Population Percent Change': -0.1,
            'Population per Square Mile': 3.0}, "WY")]
        , hw3.below_poverty_level_lesser_than(reduced_data,13))
if __name__ == '__main__':
    unittest.main()
