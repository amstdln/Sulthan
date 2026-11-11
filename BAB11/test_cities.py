from city_functions import get_city_country


def test_city_country():
    """Apakah 'Santiago, Chile' dihasilkan dengan benar?"""
    formatted_city = get_city_country('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'