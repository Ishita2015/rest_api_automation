A repository for REST API Automation

The aim is to write a generic framework which can be used by anyone to talk to REST API end-points.
In other words, if I want to just call a GET, POST or PUT, I should be able to import this module and
simply make the calls.

Jira REST API automation will be another project which will use this as a dependent library.

To be able to take this code base to that level, there are a number of steps involved as follows.

---------------------------------------
Phase-1 - To be completed by EOD 05/14
---------------------------------------
1. Create a main class where the REST Client utility will be used to make calls to end-points
2. Next create a class called as RESTClientUtil.py
3. Implement get(), post(), put() and delete() methods which can be called in a generic way. Remember
   this is framework code. Frameworks do not go throogh changes very often.
4. Move the end-point URI from get_issue.py to a file where constants can be stored at a later point of time
5. Write unit tests to test all sorts of end-points

Authentication details are right now exposed as plain-text in the code. This is bad security practice. Explore on ways to hide this from the code.
