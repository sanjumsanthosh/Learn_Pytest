# Determining Test Scope

##### Different projects have differnt goals and requirements. So we must always want to find a way to test the user visible functionality. So we must ask ourselves a series of questions to determine it.

1. is security a concern? like if there is any confidential information
2. Performance ? Do interactions need to be fast ? if so how fast ?
3. Loading ? Can it handle a lot of requests ?
4. Input validation ? If we need to validate input, we need tests for that also

##### On the perspective of card project

1. Mostly used by individual or a team
2. We need to test the visible funcitons
3. Dont need to test security of data for now.
4. We may atleast need to validate input at cli side.
