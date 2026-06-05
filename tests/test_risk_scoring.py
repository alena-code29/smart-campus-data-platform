from pipelines.silver_to_gold import risk_level


def test_risk_level_low():
    assert risk_level(0.1) == 'low'


def test_risk_level_medium():
    assert risk_level(0.4) == 'medium'


def test_risk_level_high():
    assert risk_level(0.8) == 'high'
