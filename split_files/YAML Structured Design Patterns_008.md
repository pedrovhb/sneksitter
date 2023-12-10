---
file: /home/pedro/Documents/chatgpt_export/Markdown/YAML Structured Design Patterns.md
heading_stack: <root> -> 3719366d-8d92-4f7b-a774-200e1af7f98d -> System -> eeb3eb73-253d-4b37-bdd7-596c5d4e9bbd -> System -> aaa2ae17-25fc-4113-b7ef-fc0d1b838779 -> User -> cd35cb40-3b7d-477e-89c3-b34909bf37f7 -> Assistant
---
# Assistant

Certainly, I've structured the information you provided into a hierarchical YAML document:

```yaml
Design Patterns:
  Creational patterns:
    - Name: Abstract factory
      Description: Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
      In Design Patterns: Yes
      In Code Complete[14]: Yes
      Other: —

    - Name: Builder
      Description: Separate the construction of a complex object from its representation, allowing the same construction process to create various representations.
      In Design Patterns: Yes
      In Code Complete[14]: No
      Other: —

    - Name: Dependency Injection
      Description: A class accepts the objects it requires from an injector instead of creating the objects directly.
      In Design Patterns: No
      In Code Complete[14]: No
      Other: —

    - Name: Factory method
      Description: Define an interface for creating a single object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
      In Design Patterns: Yes
      In Code Complete[14]: Yes
      Other: —

    - Name: Lazy initialization
      Description: Tactic of delaying the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed.
      In Design Patterns: No
      In Code Complete[14]: No
      Other: PoEAA[15]

    - Name: Multiton
      Description: Ensure a class has only named instances and provide a global point of access to them.
      In Design Patterns: No
      In Code Complete[14]: No
      Other: —

    - Name: Object pool
      Description: Avoid expensive acquisition and release of resources by recycling objects that are no longer in use. Can be considered a generalization of connection pool and thread pool patterns.
      In Design Patterns: No
      In Code Complete[14]: No
      Other: —

    - Name: Prototype
      Description: Specify the kinds of objects to create using a prototypical instance and create new objects from the 'skeleton' of an existing object, thus boosting performance and keeping memory footprints to a minimum.
      In Design Patterns: Yes
      In Code Complete[14]: No
      Other: —

    - Name: Resource acquisition is initialization (RAII)
      Description: Ensure that resources are properly released by tying them to the lifespan of suitable objects.
      In Design Patterns: No
      In Code Complete[14]: No
      Other: —

    - Name: Singleton
      Description: Ensure a class has only one instance and provide a global point of access to it.
      In Design Patterns: Yes
      In Code Complete[14]: Yes
      Other: —

  Structural patterns:
    - Name: Adapter, Wrapper, or Translator
      Description: Convert the interface of a class into another interface clients expect. An adapter lets classes work together that could not otherwise because of incompatible interfaces. The enterprise integration pattern equivalent is the translator.
      In Design Patterns: Yes
      In Code Complete[14]: Yes
      Other: —

    - Name: Bridge
      Description: Decouple an abstraction from its implementation allowing the two to vary independently.
      In Design Patterns: Yes
      In Code Complete[14]: Yes
      Other: —

    - Name: Composite
      Description: Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
      In Design Patterns: Yes
      In Code Complete[14]: Yes
      Other: —

    - Name: Decorator
      Description: Attach additional responsibilities to an object dynamically keeping the same interface. Decorators provide a flexible alternative to subclassing for extending functionality.
      In Design Patterns: Yes
      In Code Complete[14]: Yes
      Other: —

    - Name: Delegation
      Description: Extend a class by composition instead of subclassing. The object handles a request by delegating to a second object (the delegate).
      In Design Patterns: —
      In Code Complete[14]: —
      Other: —

    - Name: Extension object
      Description: Adding functionality to a hierarchy without changing the hierarchy.
      In Design Patterns: No
      In Code Complete[14]: No
      Other: Agile Software Development, Principles, Patterns, and Practices[16]

    - Name: Facade
      Description: Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
      In Design Patterns:
```

---

(main branch ⎇)
###### aaa20074-3c55-4f29-a7f5-57885bd7d73d
[parent ⬆️](#eeb3eb73-253d-4b37-bdd7-596c5d4e9bbd)
