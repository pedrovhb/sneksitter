---
file: /home/pedro/Documents/chatgpt_export/Markdown/YAML Structured Design Patterns.md
heading_stack: <root> -> 3719366d-8d92-4f7b-a774-200e1af7f98d -> System -> eeb3eb73-253d-4b37-bdd7-596c5d4e9bbd -> System -> aaa2ae17-25fc-4113-b7ef-fc0d1b838779 -> User -> cd35cb40-3b7d-477e-89c3-b34909bf37f7 -> Assistant -> aaa20074-3c55-4f29-a7f5-57885bd7d73d -> User -> b75744a5-d648-4ba9-8625-df50b2768c1d -> Assistant
---
# Assistant

Sure, here is the provided information structured as a hierarchical YAML document:

```yaml
Design Patterns:
  Creational patterns:
    - Name: Abstract factory
      Description: Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
    - Name: Builder
      Description: Separate the construction of a complex object from its representation, allowing the same construction process to create various representations.
    - Name: Dependency Injection
      Description: A class accepts the objects it requires from an injector instead of creating the objects directly.
    - Name: Factory method
      Description: Define an interface for creating a single object, but let subclasses decide which class to instantiate.
    - Name: Lazy initialization
      Description: Tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed.
    - Name: Multiton
      Description: Ensure a class has only named instances, and provide a global point of access to them.
    - Name: Object pool
      Description: Avoid expensive acquisition and release of resources by recycling objects that are no longer in use.
    - Name: Prototype
      Description: Specify the kinds of objects to create using a prototypical instance, and create new objects from the 'skeleton' of an existing object.
    - Name: Resource acquisition is initialization (RAII)
      Description: Ensure that resources are properly released by tying them to the lifespan of suitable objects.
    - Name: Singleton
      Description: Ensure a class has only one instance, and provide a global point of access to it.
  Structural patterns:
    - Name: Adapter, Wrapper, or Translator
      Description: Convert the interface of a class into another interface clients expect.
    - Name: Bridge
      Description: Decouple an abstraction from its implementation allowing the two to vary independently.
    - Name: Composite
      Description: Compose objects into tree structures to represent part-whole hierarchies.
    - Name: Decorator
      Description: Attach additional responsibilities to an object dynamically keeping the same interface.
    - Name: Delegation
      Description: Extend a class by composition instead of subclassing.
    - Name: Extension object
      Description: Adding functionality to a hierarchy without changing the hierarchy.
    - Name: Facade
      Description: Provide a unified interface to a set of interfaces in a subsystem.
    - Name: Flyweight
      Description: Use sharing to support large numbers of similar objects efficiently.
  Behavioral patterns:
    - Name: Blackboard
      Description: Artificial intelligence pattern for combining disparate sources of data.
    - Name: Chain of responsibility
      Description: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
    - Name: Command
      Description: Encapsulate a request as an object, thereby allowing for the parameterization of clients with different requests.
    - Name: Fluent interface
      Description: Design an API to be method chained so that it reads like a DSL.
    - Name: Interpreter
      Description: Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
    - Name: Iterator
      Description: Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
    - Name: Mediator
      Description: Define an object that encapsulates how a set of objects interact.
    - Name: Memento
      Description: Capture and externalize an object's internal state allowing the object to be restored to this state later.
    - Name: Null object
      Description: Avoid null references by providing a default object.
    - Name: Observer or Publish/subscribe
      Description: Define a one-to-many dependency between objects where a state change in one object results in all its dependents being notified and updated automatically.
    - Name: Servant
      Description: Define common functionality for a group of classes.
    - Name: State
      Description: Allow an object to alter its behavior when its internal state changes.
    - Name: Strategy
      Description: Define a family of algorithms, encapsulate each one, and make them interchangeable.
    - Name: Template method
      Description: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses.
    - Name: Visitor
      Description: Represent an operation to be performed on instances of a set of classes.
  Concurrency patterns:
    - Name: Active Object
      Description: Decouples method execution from method invocation that reside in their own thread of control.
    - Name: Balking
      Description: Only execute an action on an object when the object is in a particular state.
    - Name: Binding properties
      Description: Combining multiple observers to force properties in different objects to be synchronized or coordinated in some way.
    - Name: Compute kernel
      Description: The same calculation many times in parallel, differing by integer parameters used with non-branching pointer math into shared arrays.
    - Name: Double-checked locking
      Description: Reduce the overhead of acquiring a lock by first testing the locking criterion.
    - Name: Event-based asynchronous
      Description: Addresses problems with the asynchronous pattern that occur in multithreaded programs.
    - Name: Guarded suspension
      Description: Manages operations that require both a lock to be acquired and a precondition to be satisfied before the operation can be executed.
    - Name: Join
      Description: Provides a way to write concurrent, parallel, and distributed programs by message passing.
    - Name: Lock
      Description: One thread puts a "lock" on a resource, preventing other threads from accessing or modifying it.
    - Name: Messaging design pattern (MDP)
      Description: Allows the interchange of information (i.e. messages) between components and applications.
    - Name: Monitor object
      Description: An object whose methods are subject to mutual exclusion.
    - Name: Reactor
      Description: A reactor object provides an asynchronous interface to resources that must be handled synchronously.
    - Name: Read-write lock
      Description: Allows concurrent read access to an object, but requires exclusive access for write operations.
    - Name: Scheduler
      Description: Explicitly control when threads may execute single-threaded code.
    - Name: Thread pool
      Description: A number of threads are created to perform a number of tasks, which are usually organized in a queue.
    - Name: Thread-specific storage
      Description: Static or "global" memory local to a thread.
    - Name: Safe Concurrency with Exclusive Ownership
      Description: Avoiding the need for runtime concurrent mechanisms by using exclusive ownership.
    - Name: CPU atomic operation
      Description: CPU architectures support a range of atomic instructions that guarantee memory safety for modifying and accessing primitive values.
```

Please note that I have omitted the "In Design Patterns," "In Code Complete," and "Other" keys as requested.

---
