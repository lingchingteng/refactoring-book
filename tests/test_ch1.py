import json

from src.ch1 import statement


def test_ch1():
    with open("tests/plays.json", "r") as f:
        plays = json.load(f)

    with open("tests/invoices.json", "r") as f:
        invoices = json.load(f)

    actual = statement(invoice=invoices[0], plays=plays)
    expected = "Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n"
    assert expected == actual
