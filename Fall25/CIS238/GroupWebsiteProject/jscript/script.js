// Function to toggle the hamburger menu
function HamburgerMenu() {
    const hamburgerLinks = document.getElementById('hamburger-links');
    
    if (hamburgerLinks.style.display === 'block') {
        hamburgerLinks.style.display = 'none';
    } else {
        hamburgerLinks.style.display = 'block';
    }
}

// Function to close the hamburger menu
function closeHamburgerMenu() {
    const hamburgerLinks = document.getElementById('hamburger-links');
    hamburgerLinks.style.display = 'none';
}

// Event listener for the close button
document.addEventListener('DOMContentLoaded', function() {
    const closeButton = document.getElementById('close-button');
    
    if (closeButton) {
        closeButton.addEventListener('click', function(e) {
            e.preventDefault(); 
            closeHamburgerMenu();
        });
    }
});