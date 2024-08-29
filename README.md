In traditional software testing, code coverage metrics such as statement, branch, and function coverage have been
the primary means of assessing the thoroughness of tests. However, these methods often overlook the semantic
importance of different parts of the code, leading to scenarios where a high coverage percentage does not nec-
essarily equate to effective testing. To address this, we propose a novel approach to software coverage, termed
**Semantic Coverage**, which introduces a more meaningful way to measure code coverage by assigning weigh-
tages to different segments of a function based on their significance. Each function is divided into distinct code
splits—Core Functionality, Boundary Conditions and Edge Cases, Error Handling, Integration Points, User In-
terface Interactions, Security Features, Performance and Scalability, Configuration and Environment, and Output
Consistency. Each of these splits is then assigned a weight based on its importance to the overall function. The
total coverage for a function is calculated by aggregating these weighted splits, offering a more nuanced view of
coverage.

For instance, consider a ‘withdraw‘ function in a banking application. The core functionality, which updates
the account balance, is crucial and thus given a higher weight (e.g., 70 out of 100). In contrast, the pre- and
post-conditions, while still important, are assigned lower weights. By evaluating coverage through this lens, we
can recognize that a test case with lower statement coverage but targeting core functionality might be more valu-
able than one with higher coverage but focusing on less critical aspects. Semantic Coverage thus provides a more
accurate and meaningful metric for assessing test effectiveness, bridging the gap between coverage numbers and
real-world software reliability.

More about semantic coverage can be found below:

**Shared Semantic coverage report**: https://www.overleaf.com/read/bbjzbnbtnhmm#28d1bd 

Project Coverage Spreadsheet: [Project Ranking System.xlsx](https://1drv.ms/x/s!Agi6R56uM4x40VQu4EkrZt0RUKhc?e=LFlCf6)
