document.addEventListener("DOMContentLoaded", function () {
    const upvoteForms = document.querySelectorAll(".btn-upvote");
    const downvoteForms = document.querySelectorAll(".btn-downvote");

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
});