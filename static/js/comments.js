const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-outline-danger");
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteConfirmButton = document.getElementById("deleteConfirmButton");
/*
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}

/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
 for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}

// When the user confirms the deletion in the modal
deleteConfirmButton.addEventListener('click', (event) => {
  event.preventDefault(); // Prevent the default action from happening immediately
  const confirmUrl = deleteConfirm.href; // Get the URL for the deletion
  const  csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  fetch(confirmUrl, {
      method: "POST",  // Send a POST request to the server for deletion
      headers: {
          "X-CSRFToken": csrfToken,
      },
  }).then(response => {
      if (response.ok) {
          window.location.reload(); // Refresh the page to remove the comment
      } else {
          alert('There was an error deleting the comment.');
      }
  });
  deleteModal.hide();  // Hide the modal after the request is made
});


function showEditForm(commentId) {
  document.getElementById('edit-form-' + commentId).style.display = 'block';
}

function hideEditForm(commentId) {
  document.getElementById('edit-form-' + commentId).style.display = 'none';
}
