const roles = ["Python Developer", "AI/ML Enthusiast", "Software Developer", "DSA Enthusiast"];
let roleIndex = 0;
let charIndex = 0;
let typingText = document.getElementById("typing-text");

function typeText() {
    if (charIndex < roles[roleIndex].length) {
        typingText.innerHTML += roles[roleIndex].charAt(charIndex);
        charIndex++;
        setTimeout(typeText, 100);  // Adjust typing speed
    } else {
        setTimeout(eraseText, 1000); // Pause before deleting
    }
}

function eraseText() {
    if (charIndex > 0) {
        typingText.innerHTML = roles[roleIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(eraseText, 50); // Adjust deleting speed
    } else {
        roleIndex = (roleIndex + 1) % roles.length; // Move to next role
        setTimeout(typeText, 500);
    }
}

document.addEventListener("DOMContentLoaded", function() {
    typeText();
});
function toggleMenu() {
    let menu = document.querySelector("nav ul");
    menu.classList.toggle("active");
}

