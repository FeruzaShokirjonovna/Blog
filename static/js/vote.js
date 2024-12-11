/* jshint esversion: 6 */
document.addEventListener("DOMContentLoaded", function () {
    const upvoteForms = document.querySelectorAll(".btn-upvote");
    const downvoteForms = document.querySelectorAll(".btn-downvote");

    //Make the page to update dynamically without a reload when users vote
    upvoteForms.forEach((form) => {
        form.addEventListener("click", (event) => {
            event.preventDefault();
            fetch(form.action, {
                method: "POST",
                headers: {
                    "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
                },
            }).then((response) => {
                if (response.ok) {
                    location.reload(); // Reload to reflect changes
                }
            });
        });
    });
    downvoteForms.forEach((form) => {
        form.addEventListener("click", (event) => {
            event.preventDefault();
            fetch(form.action, {
                method: "POST",
                headers: {
                    "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
                },
            }).then((response) => {
                if (response.ok) {
                    location.reload(); // Reload to reflect changes
                }
            });
        });
    });
});
