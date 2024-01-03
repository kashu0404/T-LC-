
document.getElementById("hamburger-icon").addEventListener("click", function() {
    let sidebar = document.getElementById("mySidebar");
    let main = document.getElementById("main");

    if (sidebar.style.width === "250px") {
        sidebar.style.width = "0";
        main.style.marginLeft= "0";
        localStorage.setItem('sidebarState', 'closed');
    } else {
        sidebar.style.width = "200px";
        main.style.marginLeft = "200px";
        localStorage.setItem('sidebarState', 'open');
    }
});

function closeNav() {
    var sidebar = document.getElementById("mySidebar");
    var main = document.getElementById("main");

    sidebar.style.width = "0";
    main.style.marginLeft = "0";
    localStorage.setItem('sidebarState', 'closed');
}

window.onload = () => {
    let sidebar = document.getElementById("mySidebar");
    let main = document.getElementById("main");
    let sidebarState = localStorage.getItem('sidebarState');

    if (sidebarState === 'closed') {
        sidebar.style.width = "200px";
        main.style.marginLeft = "200px";
    } else {
        sidebar.style.width = "0";
        main.style.marginLeft = "0";
    }

    document.querySelector('.img-1').classList.add('selected-img');
};



function changeMainImage(src) {
    let mainImg = document.querySelector('.main-img');
    mainImg.src = src;

    document.querySelector('.img-1').classList.remove('selected-img');
    
    let selectedSmallImg = document.querySelector(`.other-img img[src="${src}"]`);
    
    if (selectedSmallImg) {
        selectedSmallImg.classList.add('selected-img');
        localStorage.setItem('smallImg', JSON.stringify(selectedSmallImg));
    }
}