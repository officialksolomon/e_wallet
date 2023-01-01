/* global bootstrap: false */
(() => {
    const tooltipTriggerList = Array.from(
        document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );
    tooltipTriggerList.forEach((tooltipTriggerEl) => {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });

    //
    const navLinks = document.querySelectorAll(".sidebar-nav-link");
    navLinks.forEach((navLink) =>
        navLink.addEventListener("click", (e) => {
            navLinks.forEach((navLink) => navLink.classList.remove("active"));
            e.target.classList.remove("link-dark");
            e.target.classList.add("active");
        })
    );
})();
