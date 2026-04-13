import os
import sys
import calendar as _stdlib_calendar
from importlib import import_module


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "custom_components", "waste_collection_schedule")
    ),
)

regioentsorgung_de = import_module("waste_collection_schedule.source.regioentsorgung_de")


def test_resolve_option_accepts_normal_spaces_for_nbsp_options():
    options = ["Krefelder\u00A0Straße", "Merzbrück"]

    resolved = regioentsorgung_de.resolve_option("street", "Krefelder Straße", options)

    assert resolved == "Krefelder\u00A0Straße"