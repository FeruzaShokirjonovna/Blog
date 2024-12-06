# Manual Testing

[Go to README](README.md)

| Testcase                          | Expected Result                                                       | Test Result |
|-----------------------------------|-----------------------------------------------------------------------|-------------|
| Open the Homepage                 | Homepage loads with the correct template and data                     | ✅ PASS          |
| Register a user with valid data   | Request is successful, user is registered and logged in               | ✅ PASS          |
| Register a user with invalid data | Request fails, form loads again with data and errors                  | ✅ PASS          |
| Login a user with valid data      | Request is successful, user is logged in                              | ✅ PASS          |
| Login a user with invalid data    | Request fails, form loads again with data and errors                  | ✅ PASS          |
| Open an post by clicking          | Post Detail page loads with correct template and data                 | ✅ PASS          |
| Open an post through url          | Post Detail page loads with correct template and data                 | ✅ PASS          |
| Open an post with invalid url     | 404 Error page is shown                                               | ✅ PASS          |
| **Read Later**                    |                                                                       |             |
| Add a post to "Read Later" (authenticated user) | Post is added to the "Read Later" list and a success message is shown | ✅ PASS          |
| Add a post that's already in the "Read Later" list | A success message is displayed stating "This post is already in your Read Later list." | ✅ PASS          |
| View the "Read Later" list (authenticated user) | User's saved posts are displayed correctly in the "Read Later" page | ✅ PASS          |
| Remove a post from "Read Later" list | Post is removed from the "Read Later" list and a success message is displayed | ✅ PASS          |
| Try to access the "Read Later" list without being authenticated | Redirected to the login page | ✅ PASS          |
| Add a post to "Read Later" for an unauthenticated user | Display message to login for adding to read later | ✅ PASS          |
| Remove a post from "Read Later" when no posts exist | The page refreshes without errors and remains empty | ✅ PASS          |
| Upvoting an article               | Upvote count increases                                                | ✅ PASS          |
| Downvoting an article             | Downvote count decreases                                              | ✅ PASS          |
| **Commenting**                    |                                                                       |             |
| Writing a comment                 | Request is successful, comment is added to the list, message is shown | ✅ PASS          |
| Editing a comment                 | Request is successful, comment content is edited, message is shown    | ✅ PASS          |
| Delete a comment                  | Request is successful, comment is deleted,displays modal, message is shown           | ✅ PASS          |
| **Unauthorised requests**         |                                                                       |                   |
| Voting an article                 | Request fails, redirect to login page                                 | ✅ PASS          |
| Writing a comment                 | Request fails, redirect to login page                                 | ✅ PASS          |
| Editing a comment                 | Request fails, redirect to login page                                 | ✅ PASS          |
| Delete a comment                  | Request fails, redirect to login page                                 | ✅ PASS          |