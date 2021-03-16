# Design Patterns

ProVax will be a web app that the public can use to discover their eligibility for a Covid-19 vaccination. A design pattern that is currently being used in our project is the Observer pattern. The Observer pattern is used in the Model View Controller architectural pattern, which is the basis for the Django framework. The ProVax project uses models as the observable objects, interfaces that define the operations for attaching observers to the client. The project also implements observers in the form of views, which are interfaces that define the operations to be used to notify the object of updates. 

## Design patterns we may use in the future:  
* **Strategy**: This pattern may be useful for creating Person objects that have the same attributes, but different behavior.  
* **Mediator**: This pattern is often used with the Observer pattern, which our project currently uses. This pattern helps separate objects and controls how they interact, so interdependencies are kept to a minimum. 
* **Bridge**: This is a structural pattern used to separate the client code from implementation. It is used when interacting with a database. Since our project will communicate with a few different APIs, we will most likely have need for this design pattern.  


## The plan moving forward:  
Most of the design patterns at OODesign.com stress the importance of and provide methods for modularizing code. The plan for our future design is to take note of that and focus on modularization. The best way to keep code clean and functional is to build independent units that interact without effecting each other. Building and testing need to be done in small increments to ensure that new additions to the code work with existing elements and produce the desired results. 
