# Loan Aggregator

A simple python script that performs a group by on loan data.

## Features

- Performs a group by on loan data.

## How to Run

1. Open the python file `loan-aggregator.py` in any python interpretor and run

## Design & Specification

### Assumptions

* Data will always be correctly formatted
* Loan objects will not vary
* Group by will not change, i.e. always on network, month, product
* Dates can have different years
* Group by must be performed without the use of any library

### Class Hierachy

**`Loan`**
  - `msisdn`: `string`
  - `network`: `string`
  - `date`: `string`
  - `product`: `string`
  - `amount`: `float` 
  - `day`: `string`
  - `month`: `string`
  - `year`: `string`
  &nbsp; 
  - `display()`: Displays the data in the loan object as a simple string
    - ***V2.0 Tip:** Loan objects should have more powerful functions as well as better data handling*
  
**`AggregatedLoan`**
  - `Loan`: Inherited data from a loan object
  - `count`: `int`
  - `aggregate`: `float`
  &nbsp; 
  - `display_aggregate()`: Displays the aggregated loan as a tuple with the total amount, average and count
