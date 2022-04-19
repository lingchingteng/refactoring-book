from math import floor


def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    result = f'Statement for {invoice["customer"]}\n'
    format = "${:,.2f}"

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        thisAmount = 0

        if play["type"] == "tragedy":
            thisAmount = 40000
            if perf["audience"] > 30:
                thisAmount += 1000 * (perf["audience"] - 30)
        elif play["type"] == "comedy":
            thisAmount = 30000
            if perf["audience"] > 20:
                thisAmount += 10000 + 500 * (perf["audience"] - 20)
            thisAmount += 300 * perf["audience"]
        else:
            raise Exception(f'unknown type: {play["type"]}')

        volumeCredits += max(perf["audience"] - 30, 0)
        if "comedy" == play["type"]:
            volumeCredits += floor(perf["audience"] / 5)

        result += f' {play["name"]}: {format.format(thisAmount/100)} ({perf["audience"]} seats)\n'
        totalAmount += thisAmount

    result += f"Amount owed is {format.format(totalAmount/100)}\n"
    result += f"You earned {volumeCredits} credits\n"
    return result
