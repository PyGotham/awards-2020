from applications.forms import FinancialAidApplicationForm


def test_financial_aid_lodging_requested_is_treated_as_boolean() -> None:
    other_fields = {"background": "a", "reason_to_attend": "b"}

    form = FinancialAidApplicationForm(other_fields)
    assert form.is_valid()
    # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/261.
    assert form.cleaned_data["lodging_requested"] is False


def test_financial_aid_travel_amount_must_be_greater_than_zero() -> None:
    other_fields = {"background": "a", "reason_to_attend": "b"}

    form = FinancialAidApplicationForm(
        {"travel_requested": True, "travel_amount": -1, **other_fields}
    )
    assert not form.is_valid()
    assert "travel_amount" in form.errors

    form = FinancialAidApplicationForm(
        {"travel_requested": True, "travel_amount": 0, **other_fields}
    )
    assert not form.is_valid()
    assert "travel_amount" in form.errors

    form = FinancialAidApplicationForm(
        {"travel_requested": True, "travel_amount": 1, **other_fields}
    )
    assert form.is_valid()


def test_financial_aid_travel_must_be_requested_if_amount_specified() -> None:
    other_fields = {"background": "a", "reason_to_attend": "b"}

    form = FinancialAidApplicationForm(
        {"travel_requested": False, "travel_amount": 1, **other_fields}
    )
    assert not form.is_valid()
    assert "travel_requested" in form.errors
