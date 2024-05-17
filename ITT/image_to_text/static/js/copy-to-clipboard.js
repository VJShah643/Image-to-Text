function copyToClipboard() {
    // Get the converted text element
    var convertedText = document.getElementById('converted-text');
  
    // Create a new textarea element
    var textarea = document.createElement('textarea');
  
    // Set the value of the textarea to the converted text
    textarea.value = convertedText.innerText;
  
    // Add the textarea to the document body
    document.body.appendChild(textarea);
  
    // Select the textarea
    textarea.select();
  
    // Copy the text to the clipboard
    document.execCommand('copy');
  
    // Remove the textarea from the document body
    document.body.removeChild(textarea);
  }