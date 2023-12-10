---
file: /home/pedro/Documents/chatgpt_export/Markdown/YAML Structured Design Patterns.md
heading_stack: <root> -> 3719366d-8d92-4f7b-a774-200e1af7f98d -> System -> eeb3eb73-253d-4b37-bdd7-596c5d4e9bbd -> System -> aaa2ae17-25fc-4113-b7ef-fc0d1b838779 -> User -> cd35cb40-3b7d-477e-89c3-b34909bf37f7 -> Assistant -> aaa20074-3c55-4f29-a7f5-57885bd7d73d -> User
---
# User

Please structure the following into a code block with the same contents but structured as a hierarchical YAML document. Don't include the "In design patterns", "in code complete", "other" keys.

Design patterns had originally been categorized into 3 sub-classifications based on what kind of problem they solve. Creational patterns provide the capability to create objects based on a required criterion and in a controlled way. Structural patterns are about organizing different classes and objects to form larger structures and provide new functionality. Finally, behavioral patterns are about identifying common communication patterns between objects and realizing these patterns.
Creational patterns
Name 	Description 	In Design Patterns 	In Code Complete[14] 	Other
Abstract factory 	Provide an interface for creating families of related or dependent objects without specifying their concrete classes. 	Yes 	Yes 	—
Builder 	Separate the construction of a complex object from its representation, allowing the same construction process to create various representations. 	Yes 	No 	—
Dependency Injection 	A class accepts the objects it requires from an injector instead of creating the objects directly. 	No 	No 	—
Factory method 	Define an interface for creating a single object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses. 	Yes 	Yes 	—
Lazy initialization 	Tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed. This pattern appears in the GoF catalog as "virtual proxy", an implementation strategy for the Proxy pattern. 	No 	No 	PoEAA[15]
Multiton 	Ensure a class has only named instances, and provide a global point of access to them. 	No 	No 	—
Object pool 	Avoid expensive acquisition and release of resources by recycling objects that are no longer in use. Can be considered a generalisation of connection pool and thread pool patterns. 	No 	No 	—
Prototype 	Specify the kinds of objects to create using a prototypical instance, and create new objects from the 'skeleton' of an existing object, thus boosting performance and keeping memory footprints to a minimum. 	Yes 	No 	—
Resource acquisition is initialization (RAII) 	Ensure that resources are properly released by tying them to the lifespan of suitable objects. 	No 	No 	—
Singleton 	Ensure a class has only one instance, and provide a global point of access to it. 	Yes 	Yes 	—
Structural patterns
Name 	Description 	In Design Patterns 	In Code Complete[14] 	Other
Adapter, Wrapper, or Translator 	Convert the interface of a class into another interface clients expect. An adapter lets classes work together that could not otherwise because of incompatible interfaces. The enterprise integration pattern equivalent is the translator. 	Yes 	Yes 	—
Bridge 	Decouple an abstraction from its implementation allowing the two to vary independently. 	Yes 	Yes 	—
Composite 	Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly. 	Yes 	Yes 	—
Decorator 	Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality. 	Yes 	Yes 	—
Delegation 	Extend a class by composition instead of subclassing. The object handles a request by delegating to a second object (the delegate) 	— 	— 	—
Extension object 	Adding functionality to a hierarchy without changing the hierarchy. 	No 	No 	Agile Software Development, Principles, Patterns, and Practices[16]
Facade 	Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use. 	Yes 	Yes 	—
Flyweight 	Use sharing to support large numbers of similar objects efficiently. 	Yes 	No 	—
Front controller 	The pattern relates to the design of Web applications. It provides a centralized entry point for handling requests. 	No 	No 	

J2EE Patterns[17] PoEAA[18]
Marker 	Empty interface to associate metadata with a class. 	No 	No 	Effective Java[19]
Module 	Group several related elements, such as classes, singletons, methods, globally used, into a single conceptual entity. 	No 	No 	—
Proxy 	Provide a surrogate or placeholder for another object to control access to it. 	Yes 	No 	—
Twin[20] 	Twin allows modeling of multiple inheritance in programming languages that do not support this feature. 	No 	No 	—
Behavioral patterns
Name 	Description 	In Design Patterns 	In Code Complete[14] 	Other
Blackboard 	Artificial intelligence pattern for combining disparate sources of data (see blackboard system) 	No 	No 	—
Chain of responsibility 	Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it. 	Yes 	No 	—
Command 	Encapsulate a request as an object, thereby allowing for the parameterization of clients with different requests, and the queuing or logging of requests. It also allows for the support of undoable operations. 	Yes 	No 	—
Fluent interface 	Design an API to be method chained so that it reads like a DSL. Each method call returns a context through which the next logical method call(s) are made available. 	No 	No 	—
Interpreter 	Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language. 	Yes 	No 	—
Iterator 	Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation. 	Yes 	Yes 	—
Mediator 	Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it allows their interaction to vary independently. 	Yes 	No 	—
Memento 	Without violating encapsulation, capture and externalize an object's internal state allowing the object to be restored to this state later. 	Yes 	No 	—
Null object 	Avoid null references by providing a default object. 	No 	No 	—
Observer or Publish/subscribe 	Define a one-to-many dependency between objects where a state change in one object results in all its dependents being notified and updated automatically. 	Yes 	Yes 	—
Servant 	Define common functionality for a group of classes. The servant pattern is also frequently called helper class or utility class implementation for a given set of classes. The helper classes generally have no objects hence they have all static methods that act upon different kinds of class objects. 	No 	No 	—
Specification 	Recombinable business logic in a Boolean fashion. 	No 	No 	—
State 	Allow an object to alter its behavior when its internal state changes. The object will appear to change its class. 	Yes 	No 	—
Strategy 	Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it. 	Yes 	Yes 	—
Template method 	Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure. 	Yes 	Yes 	—
Visitor 	Represent an operation to be performed on instances of a set of classes. Visitor lets a new operation be defined without changing the classes of the elements on which it operates. 	Yes 	No 	—
Concurrency patterns
Name 	Description 	In POSA2[21] 	Other
Active Object 	Decouples method execution from method invocation that reside in their own thread of control. The goal is to introduce concurrency, by using asynchronous method invocation and a scheduler for handling requests. 	Yes 	—
Balking 	Only execute an action on an object when the object is in a particular state. 	No 	—
Binding properties 	Combining multiple observers to force properties in different objects to be synchronized or coordinated in some way.[22] 	No 	—
Compute kernel 	The same calculation many times in parallel, differing by integer parameters used with non-branching pointer math into shared arrays, such as GPU-optimized Matrix multiplication or Convolutional neural network. 	No 	—
Double-checked locking 	Reduce the overhead of acquiring a lock by first testing the locking criterion (the 'lock hint') in an unsafe manner; only if that succeeds does the actual locking logic proceed.

Can be unsafe when implemented in some language/hardware combinations. It can therefore sometimes be considered an anti-pattern.
	Yes 	—
Event-based asynchronous 	Addresses problems with the asynchronous pattern that occur in multithreaded programs.[23] 	No 	—
Guarded suspension 	Manages operations that require both a lock to be acquired and a precondition to be satisfied before the operation can be executed. 	No 	—
Join 	Join-pattern provides a way to write concurrent, parallel and distributed programs by message passing. Compared to the use of threads and locks, this is a high-level programming model. 	No 	—
Lock 	One thread puts a "lock" on a resource, preventing other threads from accessing or modifying it.[24] 	No 	PoEAA[15]
Messaging design pattern (MDP) 	Allows the interchange of information (i.e. messages) between components and applications. 	No 	—
Monitor object 	An object whose methods are subject to mutual exclusion, thus preventing multiple objects from erroneously trying to use it at the same time. 	Yes 	—
Reactor 	A reactor object provides an asynchronous interface to resources that must be handled synchronously. 	Yes 	—
Read-write lock 	Allows concurrent read access to an object, but requires exclusive access for write operations. An underlying semaphore might be used for writing, and a Copy-on-write mechanism may or may not be used. 	No 	—
Scheduler 	Explicitly control when threads may execute single-threaded code. 	No 	—
Thread pool 	A number of threads are created to perform a number of tasks, which are usually organized in a queue. Typically, there are many more tasks than threads. Can be considered a special case of the object pool pattern. 	No 	—
Thread-specific storage 	Static or "global" memory local to a thread. 	Yes 	—
Safe Concurrency with Exclusive Ownership 	Avoiding the need for runtime concurrent mechanisms, because exclusive ownership can be proven. This is a notable capability of the Rust language, but compile-time checking isn't the only means, a programmer will often manually design such patterns into code - omitting the use of locking mechanism because the programmer assesses that a given variable is never going to be concurrently accessed. 	No 	—
CPU atomic operation 	x86 and other CPU architectures support a range of atomic instructions that guarantee memory safety for modifying and accessing primitive values (integers). For example, two threads may both increment a counter safely. These capabilities can also be used to implement the mechanisms for other concurrency patterns as above. The C# language uses the Interlocked class for these capabilities. 

[child ⬇️](#b75744a5-d648-4ba9-8625-df50b2768c1d)

---

(main branch ⎇)
###### b75744a5-d648-4ba9-8625-df50b2768c1d
[parent ⬆️](#aaa20074-3c55-4f29-a7f5-57885bd7d73d)
