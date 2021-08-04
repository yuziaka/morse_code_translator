# Morse code translator.

Morse code translator is a small library for translating Latin letters into Morse code and vice 
versa.

## Table of Contents
* [Installation](#installation)
* [Quick Start](#quick-start)
* [License](#license)

## Installation

```console
pip install morse-code-translator2
```

## Quick Start

Translation morse code to lat. 
```python
from morse_code_translator.translator import translate_to_lat
translate_to_lat(".--. -.-- - .... --- -.  --- -. .  .-.. --- ...- .")
'python one love'
```

Translation lat to morse code. 
```python
from morse_code_translator.translator import translate_to_morse
translate_to_morse("Python one love")
'.--. -.-- - .... --- -.  --- -. .  .-.. --- ...- .'
```

## License
<pre>
Morse code translator is licensed under the MIT License. See the LICENSE file distributed with this 
work for additional information regarding copyright ownership.

Except as contained in the LICENSE file, the name(s) of the above copyright holders shall not be 
used in advertising or otherwise to promote the sale, use or other dealings in this Software without
prior written authorization.
</pre>