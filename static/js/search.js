var endpoint = 'http://127.0.0.1:8000/api/clients?search='
const form = document.getElementById('search');
form.addEventListener('submit', submitHandler);

function submitHandler(e){
    e.preventDefault();     // This method will prevent from submitting a form, when clicking on a "Submit" button

    fetch(endpoint + form.querySelector('input').value) //This function makes a GET request to endpoint. 
    .then(response=>response.json())
    .then(data=>{
        row_cells = []
        client_id = []
        for (item of data) {
            client_id.push(item.id);
            row_cells.push(`<td>${item.first_name} ${item.last_name}</td>
                            <td>${item.phone || 'empty'}</td>
                            <td>${item.email || 'empty'}</td>
                            <td>${item.birthday || 'empty'}</td>
                            <td>${item.comment || 'empty'}</td>`
            )
        }
        
        rows = '<tr><th>Full Name</th><th>Phone</th><th>Email</th><th>Birthday</th><th>Comment</th></tr>'
        for (i = 0; i <= (data.length - 1); i++) {
            rows += `<tr class='clickable-row' onclick="window.location='/client/detail/${client_id[i]}'">${row_cells[i]}</tr>`
        }

        document.getElementById('table_row').innerHTML = rows
    })
}