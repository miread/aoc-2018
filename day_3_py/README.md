# --- Day 3: No Matter How You Slice It ---

Your input is a list of claims to a large sheet of fabric:  each claim has an ID
and consists of a single rectangle with edges parallel to the edges of the
fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of
the rectangle.
The number of inches between the top edge of the fabric and the top edge of the
rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.

A claim like **#123 @ 3,2: 5x4** means that claim ID 123 specifies a rectangle 3
inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4
inches tall. Visually, it claims the square inches of fabric represented by #
(and ignores the square inches of fabric represented by .) in the diagram below:
```
...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
```
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

**#1 @ 1,3: 4x4**
**#2 @ 3,1: 4x4**
**#3 @ 5,5: 2x2**

Visually, these claim the following areas:
```
........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
```
The four square inches marked with X are claimed by both 1 and 2. (Claim 3,
while adjacent to the others, does not overlap either of them.)

How many square inches of fabric are within two or more claims?


# --- Part Two ---

In the input file, exactly one claim doesn't overlap by even a single square
inch of fabric with any other claim.  What is the ID of the only claim that
doesn't overlap?
