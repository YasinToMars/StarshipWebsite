function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    if (sidebar.style.transform === "translateX(0px)") {
        sidebar.style.transform = "translateX(-100%)"; 
    } else {
        sidebar.style.transform = "translateX(0px)"; 
    }
}
