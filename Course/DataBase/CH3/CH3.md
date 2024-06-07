<div style = "font-family : 'Times New Roman'; font-size: 20px;">

# CH3 THE RELATIONAL MODEL

- [CH3 THE RELATIONAL MODEL](#ch3-the-relational-model)
  - [How is data represented in the relational model?](#how-is-data-represented-in-the-relational-model)
  - [What integrity constraints can be expressed?](#what-integrity-constraints-can-be-expressed)
    - [Key Constraints](#key-constraints)
    - [Specifying Key Constraints in SQL](#specifying-key-constraints-in-sql)
    - [Foreign Key Constraints](#foreign-key-constraints)
    - [General Constraints](#general-constraints)
  - [ENFORCING INTEGRITY CONSTRAINTS](#enforcing-integrity-constraints)
  - [How can data be manipulated and queried?](#how-can-data-be-manipulated-and-queried)
  - [How can we create, modify, and query tables using SQL?](#how-can-we-create-modify-and-query-tables-using-sql)
  - [How do we obtain a relational database design from an ER diagram?](#how-do-we-obtain-a-relational-database-design-from-an-er-diagram)
    - [Entity Sets to Tables](#entity-sets-to-tables)
    - [Relationship Sets (without Constraints) to Tables](#relationship-sets-without-constraints-to-tables)
    - [Translating Relationship Sets with Key Constraints](#translating-relationship-sets-with-key-constraints)
    - [Translating Weak Entity Sets](#translating-weak-entity-sets)
    - [Translating Class Hierarchies](#translating-class-hierarchies)
    - [Translating ER Diagrams with Aggregation](#translating-er-diagrams-with-aggregation)
  - [What are views and why are they used?](#what-are-views-and-why-are-they-used)

![](./Images/why.png)

## How is data represented in the relational model?

![](./Images/Q1.png)

The main construct for representing data in the relational model is a **relation**.

A relation consists of a **relation schema** and a **relation instance**. The relation instance is a table, and the relation schema describes the column heads for the table.

- The schema specifies the relation’s name, the name of each **field** (or **column**, or **attribute**), and the **domain** of each field. 
  - A domain is referred to in a relation schema by the **domain name** and has a set of associated **values**. We use the example of student information in a university database to illustrate the parts of a relation schema: 
  - $Student(sid:\textbf{string}, name:\textbf{string}, login: \textbf{string}, age:\textbf{integer},gpa:\textbf{real})$
  - This says, for instance, that the field named *sid* has a domain named **string**. The set of values associated with domain **string** is the set of all character strings. An **instance** of a relation is a set of **tuples**, also called **records**, in which each tuple has the same number of fields as the relation schema.
 ![](./Images/Figure3_1.png)
- ![](./Images/Q1_1.png)
- The **degree**, also called **arity**, of a relation is the number of fields.The **cardinality** of a relation instance is the number of tuples in it. 
- A **relational database** is a collection of relations with distinct relation names. The **relational database schema** is the collection of schemas for the relations in the database.

![](./Images/Q1_2.png)
![](./Images/Q1_3.png)



## What integrity constraints can be expressed?

<dl>
    <dt>Integrity constraint (IC)</dt>
    <dd>a condition specified on a database schema and restricts the data that can be stored in an instance of the database.</dd>
</dl>

![](./Images/Q2.png)

### Key Constraints
<dl>
    <dt>key constraint</dt>
    <dd>a statement that a certain minimal subset of the fields of a relation is a unique identifier for a tuple.</dd>

</dl>

![](./Images/Q2_1.png)

- The first part of the definition means that, in any legal instance, the values in the key fields uniquely identify a tuple in the instance.
- The second part of the definition means, for example, that the set of fields {sid, name} is not a key for Students, because this set properly contains the key {sid}. The set {sid, name} is an example of a superkey, which is a set of fields that contains a key.

A set of fields that uniquely identifies a tuple according to a key constraint is called a candidate key for the relation.

### Specifying Key Constraints in SQL

![](./Images/Q2_2.png)

In SQL, we can declare that a subset of the columns of a table constitute a key by using the **UNIQUE** constraint. At most one of these candidate keys can be declared to be a *primary key*, using the **PRIMARY KEY** constraint. (SQL does not require that such constraints be declared for a table.)

$CREATE\ TABLE\ Students\ (sid \ CHAR(20), \\ name \ CHAR(30), \\ login \ CHAR(20), \\ age \ INTEGER, \\ gpa \ REAL, \\ UNIQUE \ (name, age), \\ CONSTRAINT\ StudentsKey\ PRIMARY \ KEY \ (sid))$

This definition says that *sid* is the primary key and *the combination of name and age* is also a key. The definition of the primary key also illustrates how we can name a constraint by preceding it with **CONSTRAINT** *constraint-name*. If the constraint is violated, the constraint name is returned and can be used to identify the error.

### Foreign Key Constraints
![](./Images/Q2_3.png)

Sometimes the information stored in a relation is linked to the information stored in another relation. If one of the relations is modified, the other must be checked, and perhaps modified, to keep the data consistent.

Suppose that, in addition to Students, we have a second relation:

$$ENrolled(studid:string, cid:string, grade:string)$$

The *studid* field of Enrolled is called a **foreign key** and **refers** to Students.

![](./Images/Q2_4.png)

This constraint is illustrated in Figure 3.4. As the figure shows, there may well be some Students tuples that are not referenced from Enrolled (e.g., the student with sid=50000). However, every studid value that appears in the instance of the Enrolled table appears in the primary key column of a row in the Students table. 

If we try to insert the tuple <55555, Art104, A> into E1, the IC is violated because there is no tuple in S1 with sid 55555; the database system should reject such an insertion.

### General Constraints

## ENFORCING INTEGRITY CONSTRAINTS

**referential integrity enforcement steps**

![](./Images/Q2_5.png)
![](./Images/Q2_6.png)


## How can data be manipulated and queried?

<dl>
    <dt>relational database query</dt>
    <dd>a question about the data, and the answer consists of a new relation containing the result</dd>
</dl>

![](./Images/SELECT.png)
![](./Images/SELECT1.png)

## How can we create, modify, and query tables using SQL?

The SQL language standard uses the word *table* to denote *relation*. The subset of SQL that supports the* creation*, *deletion*, and *modification* of tables is called the **Data Definition Language (DDL)**.

We can modify the column values in an existing row using the **UPDATE** command. For example, we can increment the *age* and decrement the *gpa* of the student with *sid* 53688:

$UPDATE\ Students\ S \\ SET \ S.age=S.age+1, S.gpa = S.gpa - 1 \\ WHERE\ S.sid = 53688$

The **WHERE** clause is applied first and determines which rows are to be modified. The **SET** clause then determines how these rows are to be modified.

![](./Images/CREATE.png)
The **CREATE TABLE** statement is used to define a new table.

![](./Images/DESTORY.png)


Tuples are inserted using the **INSERT** command. We can optionally omit the list of column names in the **INTO** clause and list the values in the appropriate order.

We can delete tuples using the **DELETE** command. We can delete all Students tuples with name equal to Smith using the command.

![](./Images/ADD.png)
![](./Images/ICSummary.png)

## How do we obtain a relational database design from an ER diagram?


### Entity Sets to Tables
An entity set is mapped to a relation in a straightforward way: Each attribute of the entity set becomes an attribute of the table. Note that we know both the domain of each attribute and the (primary) key of an entity set.

![](./Images/Q6.png)

### Relationship Sets (without Constraints) to Tables
- The primary key attributes of each participating entity set, as foreign key fields.
- The descriptive attributes of the relationship set.


Consider the Works In2 relationship set shown in Figure 3.10. Each department has offices in several locations and we want to record the locations at which each employee works.
![](./Images/Figure3_10.png)


All the available information about the Works In2 table is captured by the following SQL definition:

$CREATE\ TABLE\ Works\_In2\ (ssn \ CHAR(11), \\ did \ INTEGER, \\ address\ CHAR(20),\\ since\ DATE, \\ PRIMARY\ KEY\ (ssn,did,address), \\ FOREIGN\ KEY\ (ssn)\ REFERENCES\ Employees, \\ FOREIGN\ KEY\ (address)\ REFERENCES\ Locations, \\ FOREIGN\ KEY\ (did)\ REFERENCES\ Departments)$


![](./Images/Q6_1.png)


### Translating Relationship Sets with Key Constraints
![](./Images/Review1.png)
![](./Images/Figure3_12.png)
because each department has at most one manager, no two tuples can have the same did value but differ on the ssn value. A consequence of this observation is that did is itself a key for Manages; indeed, the set did, ssn is not a key (because it is not minimal).
![](./Images/Q6_2.png)

![](./Images/Review2.png)

![](./Images/Q6_3.png)
It also captures the participation constraint that every department must have a manager: Because ssn cannot take on null values, each tuple of Dept Mgr identifies a tuple in Employees (who is the manager). The **NO ACTION** specification, which is the default and need not be explicitly specified, ensures that an Employees tuple cannot be deleted while it is pointed to by a Dept Mgr tuple. If we wish to delete such an Employees tuple, we must first change the Dept Mgr tuple to have a new employee as manager.

### Translating Weak Entity Sets

![](./Images/Review3.png)
![](./Images/Q6_4.png)

### Translating Class Hierarchies
![](./Images/Review4.png)
![](./Images/Q6_5.png)

### Translating ER Diagrams with Aggregation

![](./Images/Figure3_16.png)
For the Monitors relationship set, we create a relation with the following attributes: the key attributes of Employees (ssn), the key attributes of Sponsors (did, pid), and the descriptive attributes of Monitors (until).
![](./Images/Review5.png)
![](./Images/Q6_6.png)
Notice how the deletion of an employee leads to the deletion of all policies owned by the employee and all dependents who are beneficiaries of those policies. Further, each dependent is required to have a covering policy—because *policyid* is part of the primary key of Dependents, there is an implicit NOT NULL constraint.


## What are views and why are they used?
<dl>
    <dt>view</dt>
    <dd>a table whose rows are not explicitly stored in the database but are computed as needed from a view definition.</dd>
</dl>

![](./Images/Q7.png)
![](./Images/Q7_1.png)

![](./Images/Summary.png)

</div>