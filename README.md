<h1>Whatsapp Reader</h1>

A program to read, analyise and interact with conversations exported from Whatsapp chat
Working for:

- Android ✅
- IOS ❌ (WIP)

<h2>Data analysis</h2>

<b> 1. Manually detect patterns in the exported chat (android version)</b>

- Each message consists of a single line

- Beggining with the message date (format: DD/MM/YYY)
- A comma followed by a space (, ) as a separator
- The hour (format: HH:MM)
- A dash between spaces ( - ) as a separator
- The sender name
- A colon followed by a space (: ) as a separator
- The message itself

- The messages containing image/video/audio are shown as <Media ommited> if that option was selected when exporting

- TBC

<b>2. To parse the messages we'll be using the python built-in function .split() for strings</b>

- Each line will be read till a \n is detected meaning the end of line, or till a EOF is found

- Dividing the line by the symbol " - " we get both the message timestamp (date + time) and the message itself (author + content)

- Dividing the timestamp by the symbol ", " we get separately the date and the hour the message was sent, useful for analysis purpose, such as knowing the average hour where messages were mostly sent along the year

- Dividing the message by the symbol ": " we get separately the sender and the content, the sender info can be used to determine e.g: who sends more messages, and the content might be used to get the most used words, and later to extract the emojis as well.

<h2>Authors</h2>

- [@PabloRius](https://github.com/PabloRius)
