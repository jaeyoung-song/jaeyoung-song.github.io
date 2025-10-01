// This file contains JavaScript functionality for the homepage.
// You can add interactive elements and dynamic content updates here.

document.addEventListener('DOMContentLoaded', () => {
    // Example: Add a click event to a button
    const button = document.getElementById('myButton');
    if (button) {
        button.addEventListener('click', () => {
            alert('Button clicked!');
        });
    }

    // Example: Dynamic content update
    const contentArea = document.getElementById('content');
    if (contentArea) {
        contentArea.innerHTML = '<p>Welcome to my personal homepage!</p>';
    }
});