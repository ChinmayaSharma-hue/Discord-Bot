# Discord Dictionary Bot, "Case" 
A discord bot that can respond with various different descriptions of the word, based on the command.

(Task ID : Discord Dictionary Bot)

## Setup Instructions
* Create a bot in this [link](https://discord.com/developers/applications) and copy the token
that is generated for the bot, and paste it in the code where the bot token is to be inserted.
* In order to make the ```$query``` command available, create an account in [openAI](https://openai.com/)
and get the API key and paste it in the code where the openAI key is to be inserted.
* Add the bot to the server of choice.
* Type ```$help``` for further instructions.

## Features
* Get the meaning of a word
* Get the part of speech the word belongs to
* Find out the origin of the word
* Learn how to pronounce the word through phonetics
* Learn how to use the word in a sentence
* Get the synonyms of the word
* Ask the bot questions to get a witty answer

## How to use
* Invite the bot to the server, by clicking on this link.
* All the commands are to be preceded by '$', type ```$help``` to know what commands you can use, and what those commands can do.
  * ```$all``` To get all the information about the word 
  * ```$definition```To get the meaning of the word
  * ```$pos``` To get the part of speech the word belongs to
  * ```$org``` To find out about the origin of the word
  * ```$phonetic```To learn about the pronounciation of the word
  * ```$usage```To see the word being used in a sentence
  * ```$syn```To obtain the synonyms of the word
  * ```$ant```To obtain the antonyms of the word
  * ```$query```To talk to the bot
 
 ## Libraries/APIs used
 * [Dictionary API](https://dictionaryapi.dev/)
 * [OpenAI API](https://beta.openai.com/playground)
 * [discord.py](https://discordpy.readthedocs.io/en/stable/)
 
 ## Requirements
 ```
 pip install discord.py openai requests
 ```
 
 ## Demo
```
$help <word>
```
<img src="https://github.com/ChinmayaSharma-hue/Discord_Dictionary_Bot/blob/main/images/Screenshot%202021-11-29%20010922.jpg">


```
$all <word>
```
<img src="https://github.com/ChinmayaSharma-hue/Discord_Dictionary_Bot/blob/main/images/Screenshot%202021-11-29%20011753.jpg">


```
$query <word>
```
<img src="https://github.com/ChinmayaSharma-hue/Discord_Dictionary_Bot/blob/main/images/Screenshot%202021-11-29%20011907.jpg">
 
The demo video of the bot working can be found in this [link](https://drive.google.com/file/d/1DNxH3q1ubHRMXdc3Bn-DhN3-SgWegr0a/view?usp=sharing).