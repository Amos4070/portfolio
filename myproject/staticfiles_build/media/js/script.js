


// console.log('JavaScript is running');

// if (typeof staticPath === "undefined") {
//     console.error("Error: staticPath is not defined! Ensure it's set in your HTML.");
// } else {
//     console.log("staticPath:", staticPath);
// }

// // Get saved theme from localStorage or default to 'light'
// let theme = localStorage.getItem('theme') || 'light';
// setTheme(theme);

// // Attach event listeners to theme buttons
// let themeDots = document.querySelectorAll('.theme-dot');
// themeDots.forEach(dot => {
//     dot.addEventListener('click', function () {
//         let mode = this.dataset.mode;
//         console.log('Theme option clicked:', mode);
//         setTheme(mode);
//     });
// });

// // Function to change theme
// function setTheme(mode) {
//     let themeStyle = document.getElementById('theme-style');

//     if (typeof staticPath === "undefined") {
//         console.error("Error: staticPath is missing!");
//         return;
//     }

//     // Update the stylesheet link dynamically
//     themeStyle.href = staticPath + mode + ".css";
//     localStorage.setItem('theme', mode);
//     console.log('Theme changed to:', mode);
// }



//this below auto change the user theme every 10 seconds

// console.log('JavaScript is running');

// if (typeof staticPath === "undefined") {
//     console.error("Error: staticPath is not defined! Ensure it's set in your HTML.");
// } else {
//     console.log("staticPath:", staticPath);
// }

// // Available themes
// const themes = ['light', 'blue', 'green', 'purple'];
// let themeIndex = 0;

// // Get saved theme from localStorage or default to 'light'
// let savedTheme = localStorage.getItem('theme') || 'light';
// setTheme(savedTheme);

// // Attach event listeners to theme buttons
// let themeDots = document.querySelectorAll('.theme-dot');
// themeDots.forEach(dot => {
//     dot.addEventListener('click', function () {
//         let mode = this.dataset.mode;
//         console.log('Theme option clicked:', mode);
//         clearInterval(autoThemeInterval); // Stop auto-switching if user selects a theme
//         setTheme(mode);
//     });
// });

// // Function to change theme
// function setTheme(mode) {
//     let themeStyle = document.getElementById('theme-style');

//     if (typeof staticPath === "undefined") {
//         console.error("Error: staticPath is missing!");
//         return;
//     }

//     // Update the stylesheet link dynamically
//     themeStyle.href = staticPath + mode + ".css";
//     localStorage.setItem('theme', mode);
//     console.log('Theme changed to:', mode);
// }

// // Auto-switch themes every 3 seconds
// let autoThemeInterval = setInterval(() => {
//     themeIndex = (themeIndex + 1) % themes.length; // Cycle through themes
//     let newTheme = themes[themeIndex];
//     console.log("Auto-changing theme to:", newTheme);
//     setTheme(newTheme);
// }, 100000); // Change every 10 seconds

