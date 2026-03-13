const root = document.documentElement;

const theme = localStorage.getItem("theme");

if (theme) {
    root.setAttribute("data-theme", theme);
} else {
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const systemtheme = prefersDark ? "dark" : "light";

    // apply
    root.setAttribute("data-theme", systemtheme);
    // save
    localStorage.setItem("theme", systemtheme);
}

document.getElementById("theme-toggle").addEventListener("click", () => {

    
});

$('#theme_menu li').click(function(){
    $('#theme_used').html($(this).text() + '<span class="caret"></span>')
    const newtheme = $('#theme_menu li').getAttribute("data-theme");
    root.setAttribute("data-theme", newtheme);
    localStorage.setItem("theme", newtheme);
})