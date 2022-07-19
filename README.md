# Redis_like

The purpose of this exercise is to create a simple "Redis-like" key-value store in Python.
All data will be stored in memory for simplicity (so don't worry about disk persistence, or
any such mechanisms)

## Run the project

You need to have docker to run the code and the tests.
To run the project use the following command:

- docker-compose run app

## Some topics to be discussed

What data structures would be more adequate?
Dictionary or OrderedDictionary
To implement the state I used a single object instead of a list of it for simplicity.

What is the Big O complexity of each operation?
I will add the run time complexity of those methods in the code.

## Assumptions

I am assuming all the data we insert before starting a transaction are automatically committed.

## Tests

I used TDD to develop my tests and I love tests because they ensure the quality of the code.

##

I hope to see you soon and discuss this implementation in person. I am open to helping with any questions.

Kind regards,
Bruno Barros
