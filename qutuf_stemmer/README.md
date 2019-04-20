# Qutuf (قُطُوْف) 
An Arabic Morphological Analyzer (Including Stemming and Root Extraction) and Part-Of-Speech Tagger as an Expert System.

- **Author/Affiliation**:  [Muhammad Altabba](https://www.linkedin.com/in/muhammadaltabba)
- **License**: /
- **Links**: [Website](http://qutuf.com/Default.aspx)


## Usage
### Python

#### Install
- You can download qutuf souce code from [Here](https://github.com/Qutuf/Qutuf/releases)


#### Run

As Qutuf serves as a framework, you can run for the processing phase you need and passing the applicable parameter for each processing phase.
The entry code for running all features can be found at: [SourceCode/Views/run_Qutuf.py](./SourceCode/Views/run_Qutuf.py)
And you can check the free web-service online as you can see in [Qutuf as-a-Service](#qutuf-as-a-service) section. However, we encourage you to run qutuf on your machine and start adding additional text processing steps on top of the existing ones.

#### Qutuf as-a-Service

Qutuf is available as an experimental service at https://qutuf.herokuapp.com.
You can get the output in json, xml or html (default) by using the following url parameter:
`outputformat = [json|xml|html]`

##### JSON format
To process the word غير for example and get the result in JSON:
https://qutuf.herokuapp.com/?outputformat=json&text=غير

##### XML format
Similarly, to process the word غير for example and get the result in XML:
https://qutuf.herokuapp.com/?outputformat=xml&text=غير

##### HTML format
HTML is the default format. The following will give the output for the word غير in HTML:
https://qutuf.herokuapp.com/?text=غير

#### Using Qutuf for Lemmatization (you may call it Stemming)
Similar to `outputformat` mentioned above, there is an optional URL parameter to use when getting only the possible lemma(s) / Stem(s) of every word.
`[functionality=lemma]`
<a href='https://qutuf.herokuapp.com/?functionality=lemma&outputformat=html&text=%D8%A7%D9%84%D9%85%D9%84%D9%83%20%D8%A8%D8%A7%D9%84%D9%85%D9%84%D9%83%20%D9%81%D8%A7%D9%84%D9%85%D9%84%D9%83%20%D9%88%D9%85%D9%84%D9%83%20%D9%88%D8%A7%D9%84%D9%85%D9%84%D9%83'>?functionality=lemma&outputformat=html&text=الملك بالملك فالملك وملك والملك</a>

###### Sample Lemmatization (Stemming)
If it is intended to get only the lemma/stem of the given words. Qutuf will do all the processing but will output only the lemma(s).
Below, is the output for 'الملك بالملك فالملك وملك والملك'. Note that if the string was not a word (like space, semicolon, exclamation marks, and etc.), there will be no `lemmas` attribute.
If Qutuf could not identify the word, it will mark `has_been_identified` as `false` and will return the original word as the lemma. This will happen if the word is not in the dictionaries nor it has a valid root-and-pattern.
```
{"Word":[{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك","@number_of_possibilities":"10","@original_string":"الملك"},{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك","@number_of_possibilities":"8","@original_string":"بالملك"},{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك","@number_of_possibilities":"20","@original_string":"فالملك"},{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك, مل","@number_of_possibilities":"60","@original_string":"وملك"},{"@number_of_possibilities":"0","@original_string":" "},{"@has_been_identified":"true","@lemmas":"ملك","@number_of_possibilities":"28","@original_string":"والملك"},{"@number_of_possibilities":"0","@original_string":"."}]}
```









