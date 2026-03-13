const root = document.documentElement;

// Load saved theme or system preference
const theme = localStorage.getItem("theme");
if (theme) {
    root.setAttribute("data-theme", theme);
    updateThemeDisplay(theme);
} else {
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const systemtheme = prefersDark ? "dark" : "light";
    root.setAttribute("data-theme", systemtheme);
    localStorage.setItem("theme", systemtheme);
    updateThemeDisplay(systemtheme);
}

function updateThemeDisplay(theme) {
    const themeNames = {
        'dark': 'Dark',
        'light': 'Light',
        'default': 'Default',
        'steam-old': 'Steam Old',
        'frutiger-aero': 'Frutiger Aero'
    };
    document.getElementById('theme_used').textContent = themeNames[theme] || 'Theme';
}

document.querySelectorAll('#theme_menu a').forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault();
        const newtheme = this.dataset.theme;
        document.getElementById('theme_used').textContent = this.textContent;
        root.setAttribute("data-theme", newtheme);
        localStorage.setItem("theme", newtheme);
    });
});