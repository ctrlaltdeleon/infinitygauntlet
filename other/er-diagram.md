# ER DIAGRAM

# What is an ER diagram?

- Entity Relationship (ER) diagram.
- Shows how entities relate to each other within a system.
- Built to design or debug relational databases.
- "A unified view of data" (Peter Chen, founder of the modern ER diagrams).
- Previously known as Unified MOdeling Language (UML), which is widely used in software design.

# The components and features of an ER diagram

- Entity is defined by a rectangle.
  - A group of definable things such as students or athletes.
- Relationship is defined by a diamond.
  - Think of these as verbs.
  - Owns, utilizes, teaches, makes, etc.
- Attribute is defined by a circle.
  - Derived attribute (dotted circle, calculated from another).
    - Calculated from another attribute.
    - Age can be calculated from a date of birth.
  - Multi-valued attribute (2 circles).
    - A person can have multiple phone numbers.
- Cardinality is defined by lines.
  - 1-to-1.
    - One student with one mailing address.
  - 1-to-many.
    - One student with many classes.
  - Many-to-many.
    - Students with teachers and teachers with students.

# Mapping natural language

- Common nouns are entities.
  - Student.
- Proper nouns are entities.
  - Keanu Reeves.
- Verbs are relationships.
  - Enrolls.
- Adjectives are attributes.
  - Sophomore.
- Adverbs are attributes.
  - Digitally.

# ERD symbols and notations

- Chen style.
  - Rectangles, diamonds, and circles.
- Crow style.
  - Rectangles with entities and attributes combined.
  - Lines with relationships attached, no diamonds.

# Limitations of ER diagrams and models

- Shows relationships, but that's about it.
- Not for unstructured data because of being messy.
- Difficulty integrating with an existing database.

# How to draw a basic ER diagram

- Purpose and scope.
  - Define the purpose and scope of what you're modeling.
- Entities.
  - Identify the entities that are involved.
- Relationships.
  - Determine how entities are related.
- Attributes.
  - Layer in detail by adding details needed.
- Cardinality.
  - Show relationship if 1-to-1, etc.
