[**in progress...**] (also **waiting for the homework 6 instructions 2023**)

Done:
- refactored homework 4 code to NOT use any global variables (to make it easier to be tested)

TODO:
- create unit tests for the code (with pytest)
- create an integration test
- (optional) run a shell script to run the tests
- (optional) run the tests within a GitHub pre-commit hook
    - so the tests are run automatically before being able to commit something (the commit will not go through if the tests fail)

# How to run the code
- Cd into homework 6 folder (if not already)
    ```
    cd 06-tests
    ```
- Build Docker image (if not already)
  ```
  docker build -t hw6 .
  ```
- Run Docker image
    ```
    docker run -p 80:80 -v $PWD/app/output:/code/app/output hw6
    ```
- For more instructions on how to interact with the app, see README of homework 4