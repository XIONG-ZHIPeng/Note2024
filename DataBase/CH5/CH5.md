<div style = "font-family : 'Times New Roman'; font-size: 20px;">

# CH5 SQL: QUERIES, CONSTRAINTS, TRIGGERS

- [CH5 SQL: QUERIES, CONSTRAINTS, TRIGGERS](#ch5-sql-queries-constraints-triggers)
  - [What is included in the SQL language?](#what-is-included-in-the-sql-language)
  - [How are queries expressed in SQL? How is the meaning of a query specified in the SQL standard?(Section5.2)](#how-are-queries-expressed-in-sql-how-is-the-meaning-of-a-query-specified-in-the-sql-standardsection52)
  - [How does SQL build on and extend relational algebra and calculus?(Section5.3)](#how-does-sql-build-on-and-extend-relational-algebra-and-calculussection53)
  - [What are nested queries?](#what-are-nested-queries)
    - [More Examples of Aggregate Queries](#more-examples-of-aggregate-queries)
  - [What are null values?(Section5.6)](#what-are-null-valuessection56)
  - [How can we use queries in writing complex integrity constraints?(Section5.7)](#how-can-we-use-queries-in-writing-complex-integrity-constraintssection57)
  - [What are triggers, and why are they useful? How are they related to integrity constraints?](#what-are-triggers-and-why-are-they-useful-how-are-they-related-to-integrity-constraints)

## What is included in the SQL language? 

- **The Data Manipulation Language (DML):** This subset of SQL allows users to pose queries and to insert, delete, and modify rows.
- **The Data Definition Language (DDL):** This subset of SQL supports the creation, deletion, and modification of definitions for tables and views. Integrity constraints can be defined on tables, either when the table is created or later.
- **Triggers and Advanced Integrity Constraints:** The new SQL:1999 standard includes support for triggers, which are actions executed by the DBMS whenever changes to the database meet conditions specified in the trigger.
- **Embedded and Dynamic SQL:** Embedded SQL features allow SQL code to be called from a host language such as C or COBOL. Dynamic SQL features allow a query to be constructed (and executed) at run-time.
- **Client-Server Execution and Remote Database Access:** These commands control how a client application program can connect to an SQL database server, or access data from a database over a network.
- **Transaction Management:** Various commands allow a user to explicitly control aspects of how a transaction is to be executed.
- **Security:** SQL provides mechanisms to control users’ access to data objects such as tables and views.

## How are queries expressed in SQL? How is the meaning of a query specified in the SQL standard?(Section5.2)

![](./Images/Q2.png)

<dl>
    <dt>conceptual evaluation strategy</dt>
    <dd>a way to evaluate the query that is intended to be easy to understand rather than efficient.</dd>
</dl>

![](./Images/Q2_1.png)

Every query must have a **SELECT** clause, which specifies columns to be retained in the result, and a FROM clause, which specifies a cross-product of tables. The optional **WHERE** clause specifies selection conditions on the tables mentioned in the **FROM** clause.

![](./Images/Q2_2.png)
![](./Images/Q2_3.png)
![](./Images/Q2_4.png)
![](./Images/Q2_5.png)
![](./Images/Q2_6.png)

## How does SQL build on and extend relational algebra and calculus?(Section5.3)

![](./Images/Q3.png)
![](./Images/Q3_1.png)

## What are nested queries?

<dl>
    <dt>nested query</dt>
    <dd>a query that has another query embedded within it</dd>
</dl>

the embedded query is called a **subquery**.

![](./Images/Q4.png)

![](./Images/Q4_1.png)
![](./Images/Q4_2.png)
![](./Images/Q4_3.png)
![](./Images/Q4_4.png)
Intuitively, for each sailor we check that there is no boat that has not been reserved by this sailor.

![](./Images/Q4_5.png)
![](./Images/Q4_6.png)
![](./Images/Q4_7.png)
$SELECT\ S.rating,\ MIN\ (S.age) \\ FROM\ Sailors\ S \\ GROUP\ BY\ S.rating$


![](./Images/Q4_8.png)

*(Q32) Find the age of the youngest sailor who is eligible to vote (i.e., is at least 18 years old) for each rating level with at least two such sailors.*

$SELECT\ S.rating,\ MIN\ (S.age)\ AS\ minage \\ FROM\ Sailors\ S \\ WHERE\ S.age>=18\\ GROUP\ BY\ S.rating\\ HAVING\ COUNT\ (*)>1$

- The first step is to construct the crossproduct of tables in the from-list. Because the only relation in the **from-list** in Query Q32 is Sailors, the result is just the instance shown in Figure 5.10.
![](./Images/Figure5.10.png)
- The second step is to apply the qualification in the WHERE clause, S.age >= 18. This step eliminates the row <71, zorba, 10, 16>.
- The third step is to eliminate unwanted columns. Only columns mentioned in the SELECT clause, the GROUP BY clause, or the HAVING clause are necessary, which means we can eliminate sid and sname in our example. The result is shown in Figure 5.11.
![](./Images/Figure1112.png)
- The fourth step is to sort the table according to the GROUP BY clause to identify the groups. The result of this step is shown in Figure 5.12.
- The fifth step is to apply the group-qualification in the HAVING clause, that is, the condition COUNT (*) > 1. This step eliminates the groups with rating equal to 1, 9, and 10. Observe that the order in which the WHERE and GROUP BY clauses are considered is significant: If the WHERE clause were not considered first, the group with rating=10 would have met the group-qualification in the HAVING clause.
- The sixth step is to generate one answer row for each remaining group. The answer row corresponding to a group consists of a subset of the grouping columns, plus one or more columns generated by applying an aggregation operator. In our example, each answer row has a rating column and a minage column, which is computed by applying MIN to the values in the age column of the corresponding group. The result of this step is shown in Figure 5.13.
![](./Images/Figure5.13.png)

### More Examples of Aggregate Queries

*(Q33) For each red boat, find the number of reservations for this boat.*

$SELECT\ B.bid,COUNT\ (*)\ AS\ reservationcount \\ FROM\ Boats\ B, Reserves\ R\\ WHERE\ R.bid=B.bid\ AND\ B.color = `red'\\ GROUP\ BY\ B.bid$ 

Only columns that appear in the GROUP BY clause can appear in the HAVING clause, unless they appear as arguments to an aggregate operator in the HAVING clause.

![](./Images/Q4_9.png)
![](./Images/Q4_10.png)
![](./Images/Q4_11.png)
![](./Images/Q4_12.png)
![](./Images/Q4_13.png)

## What are null values?(Section5.6)
We use null when the column value is either unknown or inapplicable.
![](./Images/Q5.png)

## How can we use queries in writing complex integrity constraints?(Section5.7)

![](./Images/Review.png)
![](./Images/Q6.png)
![](./Images/Q6_1.png)

CREATE DOMAIN statement: 
    $CREATE\ DOMAIN\ ratingval\ INTEGER\ DEFAULT\ 1\\ CHECK\ ( VALUE >= 1\ AND\ VALUE <= 10 )$

INTEGER is the underlying, or source, type for the domain ratingval, and every ratingval value must be of this type. Values in ratingval are further restricted by using a CHECK constraint; in defining this constraint, we use the keyword VALUE to refer to a value in the domain.

## What are triggers, and why are they useful? How are they related to integrity constraints?

<dl>
    <dt>trigger</dt>
    <dd>describes actions to be taken when certain situations arise</dd>
</dl>

A database that has a set of associated triggers is called an active database.

![](./Images/Q7.png)
![](./Images/Q7_1.png)

![](./Images/S1.png)
![](./Images/S2.png)

</div>