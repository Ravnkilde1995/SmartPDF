document.querySelector('#upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const files = document.querySelector('#files').files;
    const formData = new FormData();

    if (files.length === 0) {
        alert('Please select at least one file to upload.');
        return;
    }

    for (let i = 0; i < files.length; i++) {
        formData.append('files[]', files[i]);
    }

    const progressContainer = document.getElementById('progress');
    const circularProgress = document.getElementById('circular-progress');
    const successMessage = document.getElementById('p.success');
    const downloadContainer = document.getElementById('download-container');
    const downloadBtn = document.getElementById('download-btn');

    progressContainer.style.display = 'block';
    circularProgress.style.display = 'block';

    fetch('/upload/upload_pdf', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        circularProgress.style.display = 'none';
        progressContainer.style.display = 'none';

        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(data => {
        const hasErrors = data.some(fileResult => fileResult.error);

        if (hasErrors) {
            alert('Some files could not be uploaded due to unsupported file types.');
            downloadContainer.style.display = 'none';
        } else {
            successMessage.style.display = 'block';
            downloadBtn.href = '/download/zip';
            downloadContainer.style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Network Error:', error);
        circularProgress.style.display = 'none';
        progressContainer.style.display = 'none';
    });

    downloadBtn.addEventListener('click', () => {
        successMessage.style.display = 'none';
        downloadContainer.style.display = 'none';
    });
});