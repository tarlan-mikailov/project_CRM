const form = document.getElementById('form');
form.addEventListener('submit', submitHandler);

function submitHandler(e){
    e.preventDefault();     // This method will prevent from submitting a form, when clicking on a "Submit" button

    fetch(form.action, {method: 'POST', body: new FormData(form)}) //This line makes a POST request to the form's action URL. 
    .then(response=>response.json())
    .then(data=>{
        if (data.message === 'success'){
            alert('Success!');
            form.reset()
        }
    })
}