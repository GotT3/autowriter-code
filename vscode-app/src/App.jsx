import React from 'react';
import MonacoEditor from '@uiw/react-monacoeditor';
import config from '../../config.json'


function App() {
  return (
      <MonacoEditor
        language="swift"
        height={config.video.height}
        width={config.video.width}
        value=""
        options={{
          acceptSuggestionOnEnter: "off",
          tabCompletion: "off",
          autoClosingBrackets: "never",
          autoClosingOvertype: "never",
          autoClosingQuotes: "never",
          autoIndent: "none",
          fontSize: 11,
          theme:"vs-dark"
        }}
      />
    
  );
}

export default App