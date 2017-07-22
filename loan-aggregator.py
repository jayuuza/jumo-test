import csv
from pprint import pprint
import decimal


class Loan:
    """Loan object"""

    def __init__(self, msisdn, network, date, product, amount):
        self.msisdn = msisdn
        self.network = network
        self.date = date
        self.day = date.split("-")[0]
        self.month = date.split("-")[1]
        self.year = date.split("-")[2]
        self.product = product
        self.amount = float(amount)

    def display(self):
        return "Loan " + self.msisdn + ": " + self.network + ", " + self.date + ", " + self.product + ", " + str(
            self.amount)


class AggregatedLoan(Loan):
    """A extension of a loan object containing aggregated information. i.e. how many loans are contained in the aggregate as well as the aggregate itself."""

    def __init__(self, loan):
        Loan.__init__(self, loan.msisdn, loan.network, loan.date, loan.product,
                      loan.amount)
        self.count = 1
        self.aggregate = float(self.amount)

    def add_loan(self, amount):
        self.amount += amount
        self.count += 1
        self.aggregate = float(self.amount / self.count)

    def display_aggregate(self):
        return "(" + self.network + ", " + self.product + ", " + self.month  + "): average=" + str(
            self.aggregate) + ", count =" + str(self.count)+ ", amount =" + str(self.amount)


# def get_distinct_values_for_key(key, my_dataset):
#     return {getattr(obj, key)  for obj in my_dataset}

# def get_subset(my_dataset, key, value):
#     return [row for row in my_dataset if row[key] == value]


def aggregate_loans(loans):
    # newtorks = get_distinct_values_for_key('network', loans)
    # months = get_distinct_values_for_key('month', loans)
    # years = get_distinct_values_for_key('year', loans)
    # products = get_distinct_values_for_key('product',loans)
    aggregate_loans = []
    for loan in loans:
        if len(aggregate_loans) > 0:
            found = False
            check = loan
            for aggregate in aggregate_loans:
                if aggregate.network == loan.network and aggregate.year == loan.year and aggregate.month == loan.month and aggregate.product == loan.product:
                    found = True
                    check = aggregate
            if found:
                check.add_loan(loan.amount)
            else:
                new_aggregate = AggregatedLoan(loan)
                aggregate_loans.append(new_aggregate)
        else:
            new_aggregate = AggregatedLoan(loan)
            aggregate_loans.append(new_aggregate)

    return aggregate_loans


loans = []

with open('Loans.csv', mode='r') as infile:
    reader = csv.reader(infile)
    infile.readline()
    loans = [
        Loan(row[0], row[1].replace("'", ""), row[2].replace("'", ""),
             row[3].replace("'", ""), row[4].replace("'", ""))
        for row in reader
    ]
    infile.close()

# for loan in loans:
# 	print loan.display()

aggregated_loans = aggregate_loans(loans)

with open('output.csv', mode='w') as outfile:
    for loan in aggregated_loans:
        outfile.write(loan.display_aggregate() + "\n")
    outfile.close()

# for loan in aggregated_loans:
# 	print loan.display_aggregate()
