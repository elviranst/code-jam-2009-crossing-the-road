# Problem Description
Where roads intersect, there are often traffic lights that tell pedestrians (people walking) when they should cross the street. A clever pedestrian may try to optimize her path through a city based on when those lights turn green. The city in this problem is a grid, N rows tall by M columns wide. Our pedestrian wants to get from the northeast corner of the southwest block to the southwest corner of the northeast block. Your objective is to help her find her way from corner to corner in the fastest way possible. The pedestrian can cross a street in 1 minute, but only if the traffic light is green for the entire crossing. The pedestrian can move between two streets, along one edge of a block, in 2 minutes. The pedestrian can only move along the edges of the block; she cannot move diagonally from one corner of a block to the opposite corner. Traffic lights follow the following pattern: at intersection i, the north-south lights stay green for S minutes, while the east-west lights stay red. Then the north-south lights turn red, the east-west lights turn green, and they stay that way for W minutes. Then they start the same cycle again. The pedestrian starts moving at t=0 minutes; traffic light i starts a cycle by turning green in the north-south direction at t=T minutes. There are cycles before t=T as well.

For example, intersection 0 could have the following values:
The north-south direction turns green after 0 minutes. That lasts 3 minutes, during which time the pedestrian can cross in the north-south direction and not the east-west direction. Then the lights switch, and for the next 2 minutes the pedestrian can cross in the east-west direction and not the north-south direction. Then, 5 minutes after it started, the cycle starts again. This is exactly the same as the following configuration:

Input
The first line in the input contains the number of test cases, C. This is followed by C test cases in the following format:
A single line containing "N M", where N and M are the number of horizontal roads (rows) and vertical roads (columns), as above. This is followed by N lines. The ith of those lines contains information about intersections on the ith row, where the 0th row is the northmost. Each of those lines will contain 3M integers, separated by spaces, in the following form:
S, W and T all refer to the intersection in the ith row from the north and the jth column from the west.

Output
For each test case, output a single line containing the text "Case #x: t", where x is the number of the test case and t is the minimum number of minutes it takes the pedestrian to get from the southwest corner to the northeast corner.

Limits
C, N, M, S, W, T are all non-negative integers.
C ≤ 100
Small Input
1 ≤ N, M ≤ 3
0 < S, W ≤ 10
0 ≤ T ≤ 20
Large Input
1 ≤ N, M ≤ 20
0 < S, W ≤ 10^7
0 ≤ T ≤ 10^8
