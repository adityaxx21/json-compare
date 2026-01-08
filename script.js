document.addEventListener('DOMContentLoaded', () => {
    const compareBtn = document.getElementById('compare-btn');
    const jsonAInput = document.getElementById('json-a');
    const jsonBInput = document.getElementById('json-b');
    const resultSection = document.getElementById('result-section');
    const resultOutput = document.getElementById('result-output');

    // Configure Marked
    marked.setOptions({
        highlight: function (code, lang) {
            const language = highlight.getLanguage(lang) ? lang : 'plaintext';
            return highlight.highlight(code, { language }).value;
        },
        langPrefix: 'hljs language-'
    });

    compareBtn.addEventListener('click', async () => {
        const jsonA = jsonAInput.value.trim();
        const jsonB = jsonBInput.value.trim();

        if (!jsonA || !jsonB) {
            showError("Please enter JSON in both fields.");
            return;
        }

        // Add loading state
        const originalText = compareBtn.innerHTML;
        compareBtn.innerHTML = 'Comparing...';
        compareBtn.disabled = true;
        hideError(); // Clear previous errors

        try {
            const response = await fetch('/api/compare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    json_a: jsonA,
                    json_b: jsonB
                })
            });

            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(errorText || 'Comparison failed');
            }

            const markdown = await response.text();

            // Render Markdown
            resultOutput.innerHTML = marked.parse(markdown);

            // Populate Raw
            document.getElementById('result-raw').value = markdown;

            // Reset to preview mode by default
            showResultPreview();

            // Show result section
            resultSection.classList.remove('hidden');
            resultSection.scrollIntoView({ behavior: 'smooth' });

        } catch (error) {
            console.error('Error:', error);
            showError(error.message);
        } finally {
            compareBtn.innerHTML = originalText;
            compareBtn.disabled = false;
        }
    });

    // Auto-focus first input
    jsonAInput.focus();

    // Resizer Logic
    const resizer = document.getElementById('resizer');
    const leftPane = document.getElementById('left-pane');
    const rightPane = document.getElementById('right-pane');
    const container = document.querySelector('.editors-container');

    let isResizing = false;

    resizer.addEventListener('mousedown', (e) => {
        isResizing = true;
        resizer.classList.add('resizing');
        document.body.style.cursor = 'col-resize';
        document.body.style.userSelect = 'none'; // Prevent text selection
    });

    document.addEventListener('mousemove', (e) => {
        if (!isResizing) return;

        const containerRect = container.getBoundingClientRect();
        const containerWidth = containerRect.width;

        // Calculate pointer position relative to container
        let x = e.clientX - containerRect.left;

        // Constraints (min width 200px approx)
        if (x < 200) x = 200;
        if (x > containerWidth - 200) x = containerWidth - 200;

        const leftWidthPercent = (x / containerWidth) * 100;

        leftPane.style.width = `${leftWidthPercent}%`;
        rightPane.style.width = `${100 - leftWidthPercent}%`;
    });

    document.addEventListener('mouseup', () => {
        if (isResizing) {
            isResizing = false;
            resizer.classList.remove('resizing');
            document.body.style.cursor = '';
            document.body.style.userSelect = '';
        }
    });
});

function showResultPreview() {
    document.getElementById('result-output').classList.remove('hidden');
    document.getElementById('result-raw').classList.add('hidden');

    document.getElementById('btn-preview').classList.add('active__btn');
    document.getElementById('btn-raw').classList.remove('active__btn');
}

function showResultRaw() {
    document.getElementById('result-output').classList.add('hidden');
    document.getElementById('result-raw').classList.remove('hidden');

    document.getElementById('btn-preview').classList.remove('active__btn');
    document.getElementById('btn-raw').classList.add('active__btn');
}

function showError(message) {
    const banner = document.getElementById('error-banner');
    const msgSpan = document.getElementById('error-message');
    msgSpan.textContent = message;
    banner.classList.remove('hidden');

    // Auto hide after 5 seconds
    setTimeout(() => {
        hideError();
    }, 5000);
}

function hideError() {
    const banner = document.getElementById('error-banner');
    banner.classList.add('hidden');
}

function formatJSON(elementId) {
    const textarea = document.getElementById(elementId);
    const value = textarea.value.trim();
    if (!value) return;

    try {
        const json = JSON.parse(value);
        textarea.value = JSON.stringify(json, null, 4);
        hideError();
    } catch (e) {
        showError("Invalid JSON: " + e.message);
    }
}

function minifyJSON(elementId) {
    const textarea = document.getElementById(elementId);
    const value = textarea.value.trim();
    if (!value) return;

    try {
        const json = JSON.parse(value);
        textarea.value = JSON.stringify(json);
        hideError();
    } catch (e) {
        showError("Invalid JSON: " + e.message);
    }
}
