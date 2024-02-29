let phone = document.getElementById('id_phone');
phone.addEventListener('input', changHandler);

function changHandler(e){
    if (e.inputType == 'insertText') {
        var cleaned = ('' + e.target.value).replace(/\D/g, '');
        var match;
        switch (Number(cleaned)) {
            case Number(cleaned.match(/^(\d{2})$/g)):
                match = cleaned.match(/^(\d{2})$/);
                phone.value = 38 +  ' 0' + match[1] + ' ';
                break;
            case Number(cleaned.match(/^380(\d{2})(\d{3})$/g)):
                match = cleaned.match(/^380(\d{2})(\d{3})$/);
                phone.value = 38 +  ' 0' + match[1] + ' ' + match[2] + '-';
                break;
            case Number(cleaned.match(/^380(\d{2})(\d{3})(\d{2})$/g)):
                match = cleaned.match(/^380(\d{2})(\d{3})(\d{2})$/);
                phone.value = 38 +  ' 0' + match[1] + ' ' + match[2] + '-' + match[3] + '-';
                break;
            case Number(cleaned.match(/^380(\d{2})(\d{3})(\d{2})(\d{2})$/g)):
                match = cleaned.match(/^380(\d{2})(\d{3})(\d{2})(\d{2})$/);
                phone.value = 38 +  ' 0' + match[1] + ' ' + match[2] + '-' + match[3] + '-' + match[4];
                break;
        }
    }
}