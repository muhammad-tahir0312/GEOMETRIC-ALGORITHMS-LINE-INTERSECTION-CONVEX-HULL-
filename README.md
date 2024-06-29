# GEOMETRIC ALGORITHMS PROJECT REPORT

## Foundation of Advancement of Science and Technology
## National University of Computer and Emerging Sciences
## Department of Computer Science
## Karachi, Pakistan

### Abstract

This project explores geometric algorithms, specifically focusing on Convex Hull construction and Line Intersection detection. It implements various algorithms and evaluates their performance in terms of time complexity and execution efficiency.

### Contents

- [Introduction](#introduction)
- [Programming Design](#programming-design)
- [Experimental Setup](#experimental-setup)
- [Results and Discussion](#results-and-discussion)
  - [Line Intersection](#line-intersection)
  - [Convex Hull](#convex-hull)
- [Insights](#insights)
- [Conclusion](#conclusion)
- [References](#references)

## 1. Introduction <a name="introduction"></a>

This project delves into the realm of geometric algorithms, focusing on Convex Hull construction and Line Intersection detection. It aims to provide a comprehensive understanding and implementation of various algorithms in a user-friendly interface.

## 2. Programming Design <a name="programming-design"></a>

Implemented in C#, the programming design emphasizes clarity and efficiency. It incorporates a suite of geometric algorithms selected for their specific strengths in solving the Convex Hull and Line Intersection problems.

## 3. Experimental Setup <a name="experimental-setup"></a>

The experimental setup involves generating random points to visually represent and analyze algorithmic performance. Time and space complexities are calculated for each algorithm to evaluate their efficiency under different scenarios.

## 4. Results and Discussion <a name="results-and-discussion"></a>

### 4.1 Line Intersection <a name="line-intersection"></a>

| Algorithm             | Time Taken (s)  |
|-----------------------|-----------------|
| Counter-Clockwise     | 0.00320005      |
| Vector Cross Product  | 0.000365        |
| Parametric Equation   | 0.002537958     |

### 4.2 Convex Hull <a name="convex-hull"></a>

| Algorithm         | Time Complexity | Time Taken (s) on N=100 |
|-------------------|-----------------|-------------------------|
| Graham Scan       | O(nLog(n))      | 0.00432353              |
| Jarvis-March      | O(nh)           | 0.31947946              |
| Quick Elimination | O(nLog(n))      | 0.735836029             |
| Brute Force       | O(n^3)          | 0.0458802776            |
| A New Way         | O(nLog(n))      | 0.0015172615            |

## 5. Insights <a name="insights"></a>

- **Brute Force:** Despite its theoretical inefficiency (O(n^3)), it is impractical for large datasets.
- **Jarvis March:** Shows improved efficiency over Brute Force but is outperformed by more sophisticated algorithms.
- **Graham Scan:** Efficient with O(nLog(n)) complexity, suitable for large datasets.
- **Quick Elimination:** Competitive performance with average O(nLog(n)), though potential worst-case scenarios exist.
- **A New Way Algorithm:** Superior efficiency with O(nLog(n)), ideal for diverse and large datasets.

## 6. Conclusion <a name="conclusion"></a>

The project highlights the importance of selecting geometric algorithms based on input data characteristics. Sophisticated algorithms like Graham Scan and A New Way Algorithm demonstrate efficient solutions, influencing practical algorithmic choices in computational geometry.

## 7. References <a name="references"></a>

- Researchgate (A New Way Algorithm)
- Semisignal (Brute Force Algorithm)
- CISE (Parametric Equation Algorithm)
- Wikipedia (QuickHull Algorithm)
- GeekForgeeks (QuickHull Algorithm)
- Introduction to Algorithms by Thomas H. Cormen (Reference Book)
