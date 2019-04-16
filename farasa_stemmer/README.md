# Farasa   
Farasa (which means “insight” in Arabic), is a fast and accurate text processing toolkit for Arabic text. 
Farasa consists of the segmentation/tokenization module, POS tagger, Arabic text Diacritizer, and Dependency Parser. 
Farasa segmentation/tokenization module is based on SVM-rank using linear kernels that uses a variety of features and lexicons to rank possible segmentations of a word. The features include: likelihoods of stems, prefixes, suffixes, their combinations; presence in lexicons containing valid stems or named entities; and underlying stem templates.

- **Authors**:  
        -- [Kareem Darwish](https://scinapse.io/authors/2064042002)
        -- [Hamdy Mubarak](https://scinapse.io/authors/2251487896)
- **License**: /
- **Links**: [Website](http://qatsdemo.cloudapp.net/farasa/)

## Usage
### Java
#### Install
- You can download FarasaSegmenterJar file manually from [Here](http://qatsdemo.cloudapp.net/farasa/register.html) after registration.

#### Run

```shell
$ cd {Root}/FarasaSegmenterJar_Directory

$ java -Dfile.encoding=UTF-8 -jar FarasaSegmenterJar.jar -l true -i input_file.txt -o out_file.txt
```



