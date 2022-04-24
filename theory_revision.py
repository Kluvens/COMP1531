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

API testing:
    one way of testing a web server
    it's a black-box testing
    widely used in industry

Design approaches that do not make things better are called design smells
Generally speaking, well designed code is simple, clear, and resists the tendency to break as the software changes or grows.
"Don't repeat yourself" (DRY) is about reducing repetition in code. The same code/configuration should ideally not be written in multiple places.
"Keep it Simple, Stupid" (KISS) principles state that a software system works best when things are kept simple. It is the believe that complexity and errors are correlated.
Coupling is the degree of interdependence between software components. Excessive coupling can lead to spaghetti code.
Top-down thinking says that when building capabilities, we should work from high levels of abstraction down to lower levels of abstraction.
Refactoring is restructuring existing code withour changing its external behaviour. Typically this is to fix code or design smells and thus make code more maintainable.
We also should find a balance:
    don't over-optimise to remove design smells
    don't apply priciples when there are no design smells
Clean code is generally defined by:
    being as simple as possible
    following standard & understood conventions
Within python, being "Pythonic" means that your code generally follows a set of idioms agreed upon by the broader python community.
Docstrings are an important way to document code and make clear to other programmers the intent and meaning behind what you're writing. We are somewhat different on the formatting, but we want it to include 1) Description, 2) Parameters, 3) Returns

Authentication: Process of verifying the identity of a user
Authorisation: Process of verifying an identity's access privileges
In other words, user registers, we store their password. When user logs in, we compare their input password to their stored password.
Authorisation typically involves giving the user some kind of pseudo-password that they store on their computer (client-side) which is a shortcut method for authorising a particular user.
A token means a packet of data used to autorise the user
JWTs are lightweight ways of encoding and decoding private information via a secret
Persistence: When program state outlives the process that created it. This is achieved by storing the state as data in computer data storage.
We use pickle to achieve data persistence

SDLC: Requirements analysis -> design -> development -> testing -> deployment -> maintainance ->
requirements: A condition or capability needed by a user to solve a problem or achieve an objective
Functional requirements specify a specific capability/service that the system should provide. It's what the system does.
Non-functional requirements place a constraint on how the system can achieve that. Typically this is a performance characteristic.
examples:
    Functional: The system must send a notification to all users whenever there is a new post, or someone comments on an existing post
    Non-functional: The system must send emails no later than 30 minutes after from such an activity
requirements engineering is:
    A set of activities focused on identifying the purpose and goal of a software system
    A negotiation process where stakeholders agree on what they want. Stakeholders include: end users, clients, design teams
requiremetns engineering follows a logical process across 4 steps:
    Elicitation of raw requirements from stakeholders (question and discovery)
    Analysis of requirements (building the picture)
    Formal specification of requirements (refining the picture)
    Validation of requirements (check you haven't gotten lost)

User Stories are a method of requirements engineering used to inform the development process and what features to build with the user at the centre.
A student can purchase monthly parking passes online -> As a student, I want to purchase a parking pass so that I can drive to school
User stories: Are written in non-technical language and Are user-goal focused, not product-feature focused
INVEST
    I = Independent: user story could be developed independently and delivered separately
    N = Negotiable: avoid too much detail.
    V = Valuable: must hold some value to the client
    E = Estimable: we'll get to this in a later lecture
    S = Small: user story should be small
    T = Testable
User Acceptance Criteria:
    Break down a user story into criteria that must be met for the user, or customer, to accept
    Written in natural language
    Can be refined before implementation
example:
    As a user, I want to use a search field to type a city, name, or street, so that I can find matching hotel options.
        The search field is placed on the top bar
        Search starts once the user clicks “Search”
        The field contains a placeholder with a grey-colored text: “Where are you going?”
        The placeholder disappears once the user starts typing
        Search is performed if a user types in a city, hotel name, street, or all combined
        The user can’t type more than 200 symbols

Acceptance Tests are tests that are performed to ensure acceptance criteria have been met
Not all acceptance criteria can easily be mapped to automated acceptance tests
Acceptance tests are black-box tests
The Acceptance criteria from before are often referred to a rule-based AC
Sometimes it is preferable to have AC that describe a scenario
This can be done in the Given/When/Then format

Rule-based acceptance criteria are simpler and generally work for all sorts of stories
Scenario-based AC work for stories that imply specific user actions, but don't work for higher-level system properties (e.g. design)
Scenario-based AC are more likely to be implementable as tests

use cases:
Represent a dialogue between the user and the system, with the aim of helping the user achieve a business goal
The user initiates actions and the system responds with reactions
They consider systems as a black box, and are only focused on high level understanding of flow

generally you can represent use cases as:
    informal list of steps
    diagramatic

A model is an attempt to represent a more complex system
A conceptual model captures a system in a conceptual way: high level abstraction and tends to be diagramatic or visual
conceptual models software engineers care about: data models, mathematical models, domain models, data flow models, state transition models
conceptual models:
    structural - emphasise the static structure of the system: UML class diagrams and ER diagrams
    behavioural - emphasise the Dynamic behaviour: state diagrams, use case diagram

state diagrams:
    state machines made up of a finite number of states
    the machine can be transitioned from one state to another through an action
    simple example: door (from open to close)
state machines:
    useful for modelling systems that have clearly defined states. For example:
        UIs with different screens
        Network protocols
        conversational interfaces
