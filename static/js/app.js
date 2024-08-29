window.onload = function () {
    const view = document.querySelector('meta[name="current-view"]').getAttribute('content');
    const editorView = document.getElementById('editor-view');
    const uploadView = document.getElementById('upload-view');
    const showEditorBtn = document.getElementById('show-editor');
    const showUploadBtn = document.getElementById('show-upload');

    function showView(view) {
        if (view === 'editor') {
            editorView.style.display = 'block';
            uploadView.style.display = 'none';
        } else if (view === 'upload') {
            editorView.style.display = 'none';
            uploadView.style.display = 'block';
        } else {
            console.error('Invalid view parameter: ' + view);
            alert('Something went wrong. The default view will be reloaded.');
            editorView.style.display = 'block';
            uploadView.style.display = 'none';
            history.replaceState(null, null, '?view=editor');
        }
    }

    // Initialize view based on current URL or default
    const urlParams = new URLSearchParams(window.location.search);
    const viewParam = urlParams.get('view') || 'editor';
    showView(viewParam);

    // Event listeners for buttons to change the view
    showEditorBtn.addEventListener('click', function () {
        history.pushState(null, null, '?view=editor');
        showView('editor');
    });
    showUploadBtn.addEventListener('click', function () {
        history.pushState(null, null, '?view=upload');
        showView('upload');
    });

    // Handle back/forward browser navigation
    window.addEventListener('popstate', function () {
        const urlParams = new URLSearchParams(window.location.search);
        const viewParam = urlParams.get('view') || 'editor';
        showView(viewParam);
    });
};