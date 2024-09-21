document.querySelector('#upload-form').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const files = document.querySelector('#files').files;
    const formData = new FormData();

    for (let i = 0; i < files.length; i++) {
        formData.append('files[]', files[i]);
    }

    var xhr = new XMLHttpRequest(); 
    xhr.open('POST', '/upload/upload_pdf'); 
    
    const progressContainer = document.getElementById('progress-container');
    const circularProgress = document.getElementById('circular-progress');
    progressContainer.style.display = 'block';
    circularProgress.style.display = 'block';

    xhr.onload = function() {
        const status = document.getElementById('upload-status');
        const downloadContainer = document.getElementById('download-container');
        const downloadBtn = document.getElementById('download-btn');
        status.innerHTML = '';  

        circularProgress.style.display = 'none'; 
        progressContainer.style.display = 'none'; 

        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            const successMessages = [];
            const errorMessages = [];

            response.forEach(result => {
                if (result.status === 'success') {
                    successMessages.push(result.filename); 
                } else {
                    errorMessages.push(`Error with file: ${result.filename}. ${result.error}`); 
                }
            });

            handleMessages(successMessages, errorMessages, downloadBtn, downloadContainer, status);

        } else {
            console.error('Error:', xhr.statusText);
            status.innerHTML = '<p class="error">There was an error uploading files.</p>';
        }
    };

    xhr.onerror = function() {
        console.error('Network Error');
        const status = document.getElementById('upload-status');
        status.innerHTML = '<p class="error">There was an error uploading files.</p>';
        circularProgress.style.display = 'none'; 
        progressContainer.style.display = 'none'; 
    };

    xhr.send(formData);
});

function handleMessages(successMessages, errorMessages, downloadBtn, downloadContainer, status) {
    if (successMessages.length > 0 && errorMessages.length > 0) {
        const mixedMessage = document.createElement('p');
        mixedMessage.textContent = 'Files were uploaded, but there were errors:';
        mixedMessage.classList.add('warning');
        status.appendChild(mixedMessage);
        
        errorMessages.forEach(error => {
            const errorMessage = document.createElement('p');
            errorMessage.textContent = error;
            errorMessage.classList.add('error');
            status.appendChild(errorMessage);
        });
        
        downloadBtn.href = '/download/zip';
        downloadContainer.style.display = 'block';

    } else if (successMessages.length > 0) {
        const successMessage = document.createElement('p');
        successMessage.textContent = 'Upload was successful!';
        successMessage.classList.add('success');
        status.appendChild(successMessage);

        downloadBtn.href = '/download/zip';
        downloadContainer.style.display = 'block';

    } else if (errorMessages.length > 0) {
        errorMessages.forEach(error => {
            const errorMessage = document.createElement('p');
            errorMessage.textContent = error;
            errorMessage.classList.add('error');
            status.appendChild(errorMessage);
        });
    }
}