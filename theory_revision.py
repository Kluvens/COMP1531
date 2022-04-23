historically use waterfall method: requirements -> design -> implementation -> testing -> deployment&maintenance
wasterfall has never been proposed as a viable software methodology.
Agile is an iterative approach to project management and software development that helps teams deliver value to their customers faster and with fewer headaches.
standups: frequent short progress update meetings
taskboards: use them to store and track your progress on user stories
sprints: a fixed of time where you set a number of tasks to be completed in the team. After that period is up, your review progress, and set tracks for the next sprint.
meeting minutes: just like the notes in a regular team meeting (including attendees, agenda, discussion points, actions)
pair programming: two programmers, one computer, one keyboard. Take turns to write codes but discuss it as they go

Static analysis is the processing of analysing as much of your program as you can before running it.
We use pylint to help us check the linting

Continuous integration: Practice of automating the integration of code changes from multiple contributors into a single software project.
Verification: Verification in a system life cycle context is a set of activities that compares a product of the system life cycle against the required characteristics for that product. This may include, but is not limited to, specified requirements, design description and the system itself.
Validation: Validation in a system life cycle context is a set of activities ensuring and gaining confidence that a system is able to accomplish its intended use, goals and objectives.
Verification can be broken up into two main types:
    Static verification (what you know as "linting")
    Dynamic verification (what you know as "testing")
Methods of static verification include:
    Style checking
    Type checking
    Logic checking. Includes: Anti-pattern detection and Potential warnings
    Key metric checking. Includes: Coupling and Cyclomatic complexity
    Formal verification
    Informal reasoning
Dynamic Verification typically falls into one of three categories: testing in the small, testing in the large, acceptance tests
  We often refer to small tests as unit tests, which the ISTQB defines as the testing of individual software components.
    These can be white0box or black-box tests, and are wirtten often by engineers who will implement work.
  Larger tests are tests performed to expose defects in the interfaces and in the interactions between integrated components or systems
    typically these tests fall into tcategories: module tests, integration tests, system tests
  ISTQB defines acceptance testing as formal testing with respect to user needs, requirements, and business processes conducted to determine whether or not a system satisfies the acceptance criteria and to enable the user, customers or other authorized entity to determine whether or not to accept the system.
    this testing is always balck-box and is typically testsed on the customer or user themselves
  
Coverage:
  test coverage: a measure of how much of the feature set is covered with tests
  code coverage: a measure of how much code is executed during testing
  Measure code coverage as a percentage of statements (lines) executed
  Commands are coverage run --source=. -m pytest and coverage report

Relation: Network > Internect > World Wide Web
WWW is a combination of three technologies: HTML, URL, and HTTP. It is all served over the internet
Network Protocol is a standardised structure for communicating data
Flask is a python library for creating and handling HTTP requests
API is a specification of how a software system accessed programmatically
RESTful APIs
Method: POST - GET - PUT - DELETE
Operation: Create - Read - Update - Delete
