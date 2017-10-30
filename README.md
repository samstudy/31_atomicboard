# Integration tests for AtomicBoard


The aim of this project is to cover by integration tests the web service AtomicBoard. The stage server is available by address 
[atomicboard.devman.org](http://atomicboard.devman.org).

#### Warning!
Before push test cases,needed to be created a new user with fake date by link: [atomicboard.devman.org/create_test_user](http://atomicboard.devman.org/create_test_user/)


## Test cases

  - Download and view all actuall tasks
  - Drag and drop a task
  - Modify one of current task
  - Update status of task as closed
  - Create a new task
 


### Used technological stack:
  - Selenium
  - PhantomJS

### How to push

Example of  launch on Linux, Python 3.5:

```bash

python3 test_cases.py
```



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
