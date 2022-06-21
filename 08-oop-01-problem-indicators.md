## OO or OOP
OO is about structuring modules to prevent rigid & fragile code.
There are problem indicators that tells us if we are dealing with fragile or problem codes

## Problem Indicators

### Duplicate Code
Same code that appears in more than one place.  When code changes, this requires changes in multiple place of the code

### Coupling
Code that are tightly connected to other code that it becomes hard or impossible to change code without causing problems

### No Single Responsibility
Module should only have only one reason to change.  If you are dealing with a module that needs to be changed constantly, perhaps that module is doing too many things.
evaluate for Single Responsibility Principle.

### if/else
Not about "if someone is logged in" or "if someone is over 21".  Codes violates this principle when a module performs different action based on object types

## Tool Box
Preventing rigid and fragile codes involves using one or more of the OO toolbox below:

### Objects & Classes

### Inheritance

### Encapsulation

### Polymorphism

### Composition