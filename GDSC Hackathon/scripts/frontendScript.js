
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
// function displaySelection() {
//     let titleElements = document.querySelectorAll('.title');

//     titleElements.forEach(titleElement => {
//         let rangeElements = document.querySelectorAll('.ranges');

//         titleElement.addEventListener('click', function () {
//             rangeElements.forEach(rangeElement => {
//                 // Toggle the 'ranges-selected' class
//                 rangeElement.classList.toggle('ranges-selected');

//                 // Toggle the 'display' property based on the presence of 'ranges-selected' class
//                 if (rangeElement.classList.contains('ranges-selected')) {
//                     rangeElement.style.display = 'flex';
//                 } else {
//                     rangeElement.style.display = 'none';
//                 }
//             });
//         });
//     });
// }


function displaySelection(button) {
    // Get the parent filter container
    let filterContainer = button.closest('.filter-container');

    // Hide all ranges in the parent container first
    let allRanges = filterContainer.querySelectorAll('.ranges');
    allRanges.forEach(function (range) {
        range.style.display = 'none';
        range.classList.remove('ranges-selected'); // Remove the class from all ranges
    });

    // Show the specific ranges associated with the clicked button
    let ranges = button.parentElement.nextElementSibling;

    // Toggle the display property of the ranges
    if (ranges.style.display === 'none') {
        ranges.style.display = 'flex';
        ranges.classList.add('ranges-selected'); // Add the class to the specific ranges
    } else {
        ranges.style.display = 'none';
        ranges.classList.remove('ranges-selected'); // Remove the class if hiding the ranges
    }
}


