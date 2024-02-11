// Navigation Burgur
burger = document.querySelector('.burger');
navig = document.querySelector('.navig');
navul = document.querySelector('.navul');

burger.addEventListener('click', () => {
    navul.classList.toggle('v-class-resp');
    navig.classList.toggle('h-nav-resp');
});

function logout() {
    window.open('/accounts/logout', '_self');
}

// JavaScript code for real-time search
document.getElementById("searchInput").addEventListener("input", function () {
    searchProducts(this.value);
});

function searchProducts(searchQuery) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/inventory/search/?search_query=" + encodeURIComponent(searchQuery), true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            updateProductTable(JSON.parse(xhr.responseText).products);
        }
    };
    xhr.send();
}

function updateProductTable(products) {
    var tableBody = document.querySelector("#productTable tbody");
    tableBody.innerHTML = "";

    // Add table headers
    var headers = "<tr>" +
        "<th class='tableHead'>Product Name</th>" +
        "<th class='tableHead'>Price (in ₹)</th>" +
        "<th class='tableHead'>Available Quantity</th>" +
        "<th class='tableHead'>Product Id</th>" +
        "<th class='tableHead'></th>" +
        "</tr>";
    tableBody.innerHTML += headers;

    // Add product rows
    products.forEach(function (product) {
        var row = "<tr>" +
            "<td class='tableData'>" + product.prod_name + "</td>" +
            "<td class='tableData'>" + product.price + "</td>" +
            "<td class='tableData'>" + product.quantity + "</td>" +
            "<td class='tableData'>" + product.prod_id + "</td>" +
            "<td class='tableData btns'>";

        // Add edit button
        row += "<form action='/inventory/edit/" + product.prod_id + "/' method='get'>" +
            "<button class='editBtn fa-btn' type='submit'><i class='fa-solid fa-pen'></i></button>" +
            "</form>";

        // Add delete button if user is authenticated and is a superuser
        if (product.is_superuser) {
            row += "<form action='/inventory/delete/" + product.prod_id + "/' method='get'>" +
                "<button class='deleteBtn fa-btn' type='submit'><i class='fa-solid fa-trash'></i></button>" +
                "</form>";
        }

        row += "</td></tr>";
        tableBody.innerHTML += row;
    });
}