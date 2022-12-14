# Behaviroal Questions

### STAR
S for Situation
T for Task
A for Action
R for Results

## Genral

### How to write maintainable code
* Logic as simple as possible
* No more than 10 lines in a function
* S – Single Responsibility Principle (SRP)
* O – Open Closed Principle (OCP) (open for extension, but closed for modification)
* ~~L – Liskov Substitution Principle (LSP)~~
* ~~I – Interface Segregation Principle (ISP)~~
* ~~D – Dependency Inversion Principle (DIP)~~


### How to prioritize your work
* Prioritize based on importance and urgency
* Urgent and Important
* Important but not Urgent
* Urgent and Unimportant
* Neither Urgent or Important

### Resume
* LLVM
    - Overview: Arbitrary SIMD instruction set contains arbitrary vectors, which will decrease the efficiency of vectorization.
    - Approaches:
        - Type Legalization
        - SWAR: SIMD Within a Register

## eTRACS
* eTRACS
    - Overview:
        - Faculty Management
        - Academic Planning
        - Budget Preparation
        - Reporting
    - Details:
        - Stakeholder Management
        - 6SP / TTR
        - Document Management
        - Contract Management

### Challenges
* Data Migration
* S: When joinging the team, early stage of our product, we needed courses, course offerings and related data from another system.
* T: Was given the task 2 months after I joined. Migrate data and adjust our table structure accordingly => daily cron jobs.
* A: A year of work. Optimized work.
* R: Migrated data is the foundation of our product. Was an expert of writing sql queries at one point.

### Mistakes/Failures/Conflicts
* RBAC flag
* S: Second ticket I worked on.
* T: We need a logic for access control where people who are in different departments or have different ranks will be given different permissions.
* A: Writing this function in a logic oriented style where I checked different situations step by step. code review => Tech lead showed me a more maintainable way where flags indicating different status were initiated on the top of the function then assigned to values based on situations. Clear on what situations we are checking.
* R: Cried a little... Become obsessed with writing maintainable code.

### Enjoyed
* Nice working environtment
* Nice coworkers who spare no effort working towards the same goal
* Work hard and party hard
* Learned not only work culture but also life

### Leadership
* S: New Co-op students joined in our team
* T: Select interested technologies the team was using and give brief introduction. (Database, React)
* A: Introduce technologies and answer their questions.

### What You'd Do Differently
* Ask questions
* Speak up



## Workday

### XpressO
* What is it? XpressO (XO) is Workday's internal programming language where developers use drag and drop, form based UI interface to implement business logic(No actual coding involved). It isolates developers from UI considerations and the underlying platform with database, security and other services.
- Frontend: Using configurable UI packages. Filling out the right parmeters.
- Backend: Retrieve secured data to secured users.
- Automation: Imitating UI workflow by creating templates and variable assignments.

* Pros and cons:
- Pros:
    - Different developers are able to write exact same code with coding standards all met.
    - Don't need worry about authentication, optimization, how data is stored, etc.

- Cons:
    - Can't actually code.
    - Too many components. For normal web application implementation, MVC is pretty sufficient and also simple enough to build complicated applications. But XO has too many components that don't have a consistent backbone
        - We have our own components for MVC, which are not call MVC in Workday.
        - Businese Process Framework which allows us to configure and maintain process flow to connect people, applications and services.
        - Web services with at least 4 concepts that I still don't understand (EIB, iLoad, IMM, OX 2.0).
        - Notification.
    - Logic behind components is not consistent. Usually we learn the basics and we would be able to explore on our own. This is not the case in Workday. It also cases depression.
    - Too little documentation. Things are not documented well. But I learnt to ask for help right away after I'm stuck, which is a good thing for me.
    - Consequences:
        - Long learning curves. Too many components with too little documentation and nonconsistent logic makes it difficult to learn. It normally takes people a year to learn its basics.
        - Depression.
        - Limited functionality.
        - No technical difficulties but communication difficulties.
        - Once you get hang on things, they don't let you leave easily.
### XpressO is not programming
* A domain specific language designed with rigit object oriented principles for modeling business logic and the creation of form-based applications.


### Challenges
* Manager Insights Hub
* S: We are building a new feature to enable managers track their employee career activity and help them grow.
* T: Build a suggested mentor section.
* A: Features that I have worked on before were add-on features that are built on top of existing work. But for the suggested mentor section, I have to start from scratch. I helped rebuild our class model and created at least 4 abstract/non-abstract classes, on top of which I need to consider making future work easier. I have also utilized card framework for UI, notification framework and suggested mentor API.
* R: The logic for the feature is quite simple but different components/packages have their own limitations. Along the way of implementation, I had to communicate with a couple of teams to ask them to make a few adjustments on their side. Had to communicate with our tech lead and PM to adjust our class model and UI given the limitation we have. Overall, there were a lot of communications involved.

### Mistakes/Failures
* Goal Reordering
* S: Customers were asking for a feature where they can order goals in a performance review.
* T: Should be a fairly easy feature to implement if we used React. But we needed to utilize an item reordering framework to realize it.
* A: Made a big UI structure change in order to accommodate the ordering framework.
* R: Some of our data processing were relying on the UI structure. Tho we have automation and QA to test the feature, it still didn't capture some of the bugs. I wouldn't make UI structure change easily if it's not necessary. But if that is the only option left, I would test more thoroughly despite the automation and QA and check as much as I can to see which functions are using the structure.

### Leadership
* Helping new hires to learn about the team and answer their questions.

### Conflicts
* No conflicts.

### What You'd Do Differently
* Ask more
* Leave sooner
* Vitual: It would be more efficient when we work in the office. I haven't worked with anyone in person for 2 years. Hope we can get back to office soon. Hold the badminton event ASAP.