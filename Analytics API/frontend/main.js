const apiUrlInput = document.getElementById('apiUrl');
    const healthBtn = document.getElementById('healthBtn');
    const analyzeJsonBtn = document.getElementById('analyzeJsonBtn');
    const analyzeFileBtn = document.getElementById('analyzeFileBtn');
    const clearLogsBtn = document.getElementById('clearLogsBtn');
    const logsInput = document.getElementById('logsInput');
    const fileInput = document.getElementById('fileInput');
    const output = document.getElementById('output');
    const healthStatus = document.getElementById('healthStatus');
    const jsonStatus = document.getElementById('jsonStatus');
    const fileStatus = document.getElementById('fileStatus');

    function getBaseUrl() {
      return apiUrlInput.value.trim().replace(/\/$/, '');
    }

    function setOutput(data) {
      output.textContent = typeof data === 'string' ? data : JSON.stringify(data, null, 2);
    }

    async function handleResponse(response) {
      const text = await response.text();
      let parsed;

      try {
        parsed = JSON.parse(text);
      } catch {
        parsed = text;
      }

      if (!response.ok) {
        throw new Error(typeof parsed === 'string' ? parsed : JSON.stringify(parsed, null, 2));
      }

      return parsed;
    }

    healthBtn.addEventListener('click', async () => {
      healthStatus.textContent = 'Checking API...';
      try {
        const response = await fetch(`${getBaseUrl()}/`);
        const data = await handleResponse(response);
        healthStatus.textContent = 'API is reachable.';
        setOutput(data);
      } catch (error) {
        healthStatus.textContent = 'Health check failed.';
        setOutput(error.message);
      }
    });

    analyzeJsonBtn.addEventListener('click', async () => {
      jsonStatus.textContent = 'Sending JSON logs...';

      const logs = logsInput.value
        .split('\n')
        .map(line => line.trim())
        .filter(line => line !== '');

      try {
        const response = await fetch(`${getBaseUrl()}/analyze`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ logs })
        });

        const data = await handleResponse(response);
        jsonStatus.textContent = 'JSON analysis completed.';
        setOutput(data);
      } catch (error) {
        jsonStatus.textContent = 'JSON analysis failed.';
        setOutput(error.message);
      }
    });

    analyzeFileBtn.addEventListener('click', async () => {
      fileStatus.textContent = 'Uploading file...';

      const selectedFile = fileInput.files[0];
      if (!selectedFile) {
        fileStatus.textContent = 'Please choose a file first.';
        setOutput('No file selected.');
        return;
      }

      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const response = await fetch(`${getBaseUrl()}/analyze-file`, {
          method: 'POST',
          body: formData
        });

        const data = await handleResponse(response);
        fileStatus.textContent = 'File analysis completed.';
        setOutput(data);
      } catch (error) {
        fileStatus.textContent = 'File analysis failed.';
        setOutput(error.message);
      }
    });

    clearLogsBtn.addEventListener('click', () => {
      logsInput.value = '';
      jsonStatus.textContent = '';
      setOutput('No request sent yet.');
    });