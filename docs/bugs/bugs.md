### **5.3.1. Fixed Bugs **

During the project development these bugs are encountered and solved
-NameError: name 'views' is not defined:
_Removed views reference: Ensure that the views reference is removed completely from the urlpatterns list.
Directly used imported view classes and functions: Use PostList, PostDetail, read_later, add_to_read_later, post_upvote, and post_downvote directly in the path definitions._


### **5.3.2. Unfixed Bugs ** 

During the project development these bugs are encountered and not solved

-Uncaught ReferenceError: bootstrap is not defined

-Refused to execute script from 'https://res.cloudinary.com/dlznujk9q/raw/upload/v1/static/' because its MIME type ('image/gif') is not executable.

-This page is failed to load a stylesheet