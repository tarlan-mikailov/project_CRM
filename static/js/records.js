// filling reservation date input with current date
const date = new Date()
document.getElementById('reservation_date').value = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate().toString().padStart(2, "0")}`

// Calling the function for constructing forms and record table
getBookings()

// Constructing trigger by changing the reservation date for function calling
document.getElementById('reservation_date').addEventListener('change', getBookings)

function getBookings() {
    let reserved_slots = []
    const date = document.getElementById('reservation_date').value
    document.getElementById('today').innerHTML = date

    fetch("/record/list/" + '?date=' + date)
        .then(r => r.json())
        .then(data => {
            reserved_slots = []
            bookings = ""
            
            // Constructing paragraphs for reserved times
            for (const item of data) {
                reserved_slots.push(item.time_slot)
                bookings += `<p>${item.id_client.first_name} ${item.id_client.last_name} - ${formatTime(item.time_slot)} - ${item.id_staff.first_name} </p>`
            }

            // Constructing options for time select
            slot_options = `<option value="0" disabled>Select time</option>`
            for (let i = 10; i < 20; i++) {
                const label = formatTime(i)
                if (reserved_slots.includes(i)) {
                slot_options += `<option value=${i} disabled>${label}</option>`
                } else {
                slot_options += `<option value=${i}>${label}</option>`
                }
            }
            
            // Inserting reserved times and options
            document.getElementById('reservation_slot').innerHTML = slot_options
            if(bookings==''){
                bookings = "No records"
            }
            document.getElementById('records').innerHTML = bookings
        })
}


// Function for constructing time label
function formatTime(time) {
    const ampm = time < 12 ? 'AM' : 'PM'
    const t = time < 12 ? time : time > 12 ? time - 12 : time
    const label = `${t} ${ampm}`
    return label
}


const form = document.getElementById('form');
// Submitting the form
document.getElementById('button').addEventListener('click', function (e) {
    e.preventDefault();

    fetch(form.action, {method: 'post', body: new FormData(form)})
        .then(r => r.json())
        .then(data => {
            if (data.message == 'success') {
                alert('Success!');
                getBookings()}
        })
})