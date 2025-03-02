// script.js - Basic client-side functionality

// Function to validate the registration form
function validateRegisterForm() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (name === "" || email === "" || password === "") {
        alert("All fields are required!");
        return false;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters long!");
        return false;
    }

    return true;
}

// Function to validate the login form
function validateLoginForm() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (email === "" || password === "") {
        alert("All fields are required!");
        return false;
    }

    return true;
}

// Function to validate the job application form
function validateApplyJobForm() {
    const resume = document.getElementById('resume').value;
    const jobUrl = document.getElementById('job_url').value;

    if (resume === "" || jobUrl === "") {
        alert("All fields are required!");
        return false;
    }

    if (!jobUrl.startsWith("http://") && !jobUrl.startsWith("https://")) {
        alert("Please enter a valid job URL!");
        return false;
    }

    return true;
}

// Add event listeners to forms
document.addEventListener('DOMContentLoaded', function () {
    const registerForm = document.querySelector('form[action="/register"]');
    const loginForm = document.querySelector('form[action="/login"]');
    const applyJobForm = document.querySelector('form[action="/apply_job"]');

    if (registerForm) {
        registerForm.addEventListener('submit', function (event) {
            if (!validateRegisterForm()) {
                event.preventDefault();
            }
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            if (!validateLoginForm()) {
                event.preventDefault();
            }
        });
    }

    if (applyJobForm) {
        applyJobForm.addEventListener('submit', function (event) {
            if (!validateApplyJobForm()) {
                event.preventDefault();
            }
        });
    }
});

