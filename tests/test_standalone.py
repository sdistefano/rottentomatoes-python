from rottentomatoes import standalone


def test_tomatometer():
    assert standalone.tomatometer("top gun") == 58


def test_movie_url():
    assert standalone._movie_url("top gun") == "https://www.rottentomatoes.com/m/top_gun"


def test_audience_score():
    assert standalone.audience_score("happy gilmore") == 85


def test_genres():
    assert standalone.genres("happy gilmore") == ["Comedy"]


def test_weighted_score():
    assert standalone.weighted_score("top gun maverick") == 97


def test_rating():
    assert standalone.rating("top gun maverick") == "PG-13"


def test_duration():
    assert standalone.duration("top gun") == "1h 49m"


def test_year_released():
    assert standalone.year_released("forrest gump") == "1994"


def test_actors():
    res = standalone.actors("forrest gump", 5)
    
    for actor in [
        'Tom Hanks', 'Robin Wright', 'Gary Sinise', 'Mykelti Williamson', 'Sally Field'
    ]:
        assert actor in res
