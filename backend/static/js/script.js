// Get elements
const uploadArea = document.getElementById('uploadArea');
const imageInput = document.getElementById('imageInput');
const fileInfo = document.getElementById('fileInfo');
const fileName = document.getElementById('fileName');
const fileSize = document.getElementById('fileSize');
const predictBtn = document.getElementById('predictBtn');
const loading = document.getElementById('loading');
const form = document.getElementById('uploadForm');

// Click on upload area
uploadArea.addEventListener('click', () => {
    imageInput.click();
});

// File selection change
imageInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        // Check file size (10MB)
        if (file.size > 10 * 1024 * 1024) {
            alert('File too large! Please upload image less than 10MB.');
            imageInput.value = '';
            return;
        }

        // Check file type
        if (!file.type.startsWith('image/')) {
            alert('Please upload an image file only.');
            imageInput.value = '';
            return;
        }

        // Display file info
        fileName.textContent = file.name;

        // Format file size
        const sizeInKB = file.size / 1024;
        if (sizeInKB < 1024) {
            fileSize.textContent = `${sizeInKB.toFixed(1)} KB`;
        } else {
            fileSize.textContent = `${(sizeInKB / 1024).toFixed(1)} MB`;
        }

        fileInfo.classList.add('show');
        predictBtn.disabled = false;
        uploadArea.style.background = '#e8f5e9';
    } else {
        fileInfo.classList.remove('show');
        predictBtn.disabled = true;
        uploadArea.style.background = 'white';
    }
});

// Drag and drop
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.style.background = '#e8f5e9';
    uploadArea.style.borderColor = '#1e4b3a';
    uploadArea.style.transform = 'scale(1.02)';
});

uploadArea.addEventListener('dragleave', (e) => {
    e.preventDefault();
    uploadArea.style.background = 'white';
    uploadArea.style.borderColor = '#2d6a4f';
    uploadArea.style.transform = 'scale(1)';
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.style.background = 'white';
    uploadArea.style.borderColor = '#2d6a4f';
    uploadArea.style.transform = 'scale(1)';

    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
        if (file.size <= 10 * 1024 * 1024) {
            imageInput.files = e.dataTransfer.files;

            // Trigger change event
            const event = new Event('change', { bubbles: true });
            imageInput.dispatchEvent(event);
        } else {
            alert('File too large! Please upload image less than 10MB.');
        }
    } else {
        alert('Please upload a valid image file.');
    }
});

// Show loading on form submit
form.addEventListener('submit', (e) => {
    if (imageInput.files.length > 0) {
        loading.classList.add('show');
        predictBtn.disabled = true;
        fileInfo.classList.remove('show');
    }
});

// Safety - page load par loading hide rahe
document.addEventListener('DOMContentLoaded', function () {
    loading.classList.remove('show');
});