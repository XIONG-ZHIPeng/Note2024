<div style = "font-family : 'Times New Roman'; font-size: 20px;">

# CH4 RELATIONAL ALGEBRA AND CALCULUS

- [CH4 RELATIONAL ALGEBRA AND CALCULUS](#ch4-relational-algebra-and-calculus)
  - [What is the foundation for relational query languages like SQL? What is the difference between procedural and declarative languages?](#what-is-the-foundation-for-relational-query-languages-like-sql-what-is-the-difference-between-procedural-and-declarative-languages)
  - [What is relational algebra, and why is it important?](#what-is-relational-algebra-and-why-is-it-important)
  - [What are the basic algebra operators, and how are they combined to write complex queries?](#what-are-the-basic-algebra-operators-and-how-are-they-combined-to-write-complex-queries)
    - [Selection and Projection](#selection-and-projection)
    - [Set Operations](#set-operations)
    - [Join](#join)
    - [Division](#division)
    - [More Example](#more-example)
  - [What is relational calculus, and why is it important?](#what-is-relational-calculus-and-why-is-it-important)
    - [Tuple Relational Calculus](#tuple-relational-calculus)
    - [Domain Relational Calculus](#domain-relational-calculus)

## What is the foundation for relational query languages like SQL? What is the difference between procedural and declarative languages?

<dl>
    <dt>Query languages</dt>
    <dd>specialized languages for asking questions, or queries, that involve the data in a database.</dd>
</dl>

![](./Images/Q1.png)
![](./Images/Q1_1.png)

The inputs and outputs of a query are relations. A query is evaluated using *instances* of each input relation and it produces an instance of the output relation.
![](./Images/Q1_2.png)
![](./Images/Q1_3.png)


## What is relational algebra, and why is it important?

**Relational algebra** is one of the two formal query languages associated with the relational model. Each relational query describes a step-by-step procedure for computing the desired answer, based on the order in which operators are applied in the query.

## What are the basic algebra operators, and how are they combined to write complex queries?

### Selection and Projection

![](./Images/Q3.png)
The projection operator &pi; allows us to extract columns from a relation; for example, we can find out all sailor names and ratings by using &pi;.
![](./Images/Q3_2.png)

The important point to note is that, although three sailors are aged 35, a single tuple with age=35.0 appears in the result of the projection. This follows from the definition of a relation as a set of tuples. In practice, real systems often omit the expensive step of eliminating duplicate tuples, leading to relations that are multisets.
![](./Images/Q3_1.png)

### Set Operations

The following standard operations on sets are also available in relational algebra: $union\ (\cup), intersection\ (\cap), set-difference\ (-), and\ cross-product\ (\times)$

- **Union:** R &cup; S returns a relation instance containing all tuples that occur in *either* relation instance R or relation instance S (or both). R and S must be *union-compatible*, and the schema of the result is defined to be identical to the schema of R. <br> Two relation instances are said to be union-compatible if the following conditions hold: <br> 1. they have the same number of the fields, and <br> 2. corresponding fields, taken in order from left to right, have the same *domains*. <br> Note that field names are not used in defining union-compatibility. For convenience, we will assume that the fields of R ∪ S inherit names from R, if the fields of R have names. (This assumption is implicit in defining the schema of R ∪ S to be identical to the schema of R, as stated earlier.)
- **Intersection:** R ∩ S returns a relation instance containing all tuples that occur in both R and S. The relations R and S must be union-compatible, and the schema of the result is defined to be identical to the schema of R.
- **set-difference:** R−S returns a relation instance containing all tuples that occur in R but not in S. The relations R and S must be union-compatible, and the schema of the result is defined to be identical to the schema of R.

![](./Images/Q3_3.png)


- **Cross-product:** R × S returns a relation instance whose schema contains all the fields of R (in the same order as they appear in R) followed by all the fields of S (in the same order as they appear in S). The result of R × S contains one tuple r, s (the concatenation of tuples r and s) for each pair of tuples r ∈ R, s ∈ S. The cross-product opertion is sometimes called **Cartesian product**. <br> We use the convention that the fields of R × S inherit names from the corresponding fields of R and S. It is possible for both R and S to contain one or more fields having the same name; this situation creates a naming conflict. The corresponding fields in R × S are unnamed and are referred to solely by position.

![](./Images/Q3_4.png)

renaming operator ρ.

### Join

The most general version of the join operation accepts a join condition c and a pair of relation instances as arguments and returns a relation instance. The *join condition* is identical to a *selection conditio*n in form. The operation is defined as follows:

$$R \bowtie_c S = \sigma_c (R \times S)$$

Thus &bowtie; is defined to be a cross-product followed by a selection. Note that the condition c can (and typically does) refer to attributes of both R and S. The reference to an attribute of a relation, say, R, can be by position (of the form R.i) or by name (of the form R.name).

![](./Images/Q3_5.png)
![](./Images/Q3_6.png)


### Division

![](./Images/Q3_7.png)
![](./Images/Q3_8.png)
![](./Images/Q3_9.png)


### More Example

![](./Images/Instance.png)
![](./Images/Instance2.png)
![](./Images/E1.png)
![](./Images/E2.png)
![](./Images/E3.png)
![](./Images/E4.png)
![](./Images/E5.png)

![](./Images/S.png)


## What is relational calculus, and why is it important?

### Tuple Relational Calculus

![](./Images/Q4.png)

A tuple relational calculus query has the form { T | p(T) }, where T is a tuple variable and p(T ) denotes a formula that describes T.
(Q11) Find all sailors with a rating above 7.
*{S | S ∈ Sailors ∧ S.rating > 7}*


### Domain Relational Calculus

<dl>
    <dt>domain variable</dt>
    <dd>a variable that ranges over the values in the domain of some attribute</dd>
</dl>

![](./Images/DRC.png)

![](./Images/DRC1.png)
![](./Images/DRC2.png)
![](./Images/DRC3.png)
![](./Images/DRC4.png)
![](./Images/DRC5.png)
![](./Images/DRC6.png)
This query can be read as follows: “Find all values of N such that some tuple <I, N, T, A> in Sailors satisfies the following condition: For every B, BN, C , either this is not a tuple in Boats or there is some tuple Ir, Br, D in Reserves that proves that Sailor I has reserved boat B.” The ∀ quantifier allows the domain variables B, BN , and C to range over all values in their respective attribute domains, and the pattern ‘¬( B, BN, C ∈ Boats)∨’ is necessary to restrict attention to those values that appear in tuples of Boats.
![](./Images/DRC7.png)

![](./Images/Safe.png)

![](./Images/DRCS.png)


</div>