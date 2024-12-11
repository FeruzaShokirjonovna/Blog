### **5.3.1. Fixed Bugs **

During the project development these bugs are encountered and solved:

- NameError: name 'views' is not defined:
- _Removed views reference: Ensure that the views reference is removed completely from the urlpatterns list.
Directly used imported view classes and functions: Use PostList, PostDetail, read_later, add_to_read_later, post_upvote, and post_downvote directly in the path definitions._

- After passing html validator, the errors below found:

![HTML bug](static/images/html-validator-bug.png)

    - The values Home, Signup, and Login are not valid values for the aria-current attribute. 
- Fix: need to replace the incorrect values (Home, Signup, Login) with page, as these values are referring to the current page in the navigation.

### **5.3.2. Unfixed Bugs ** 

There are no known unfixed bugs.
