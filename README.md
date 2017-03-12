# twiOpinion
## Introduction
**twiOpinion** enables users without programming experience to learn about public opinion through Twitter.   
It accesses Twitter, a social networking service, and applies machine learning on tweets.  
No programming experience is required for users. Both graphics user interface and command line interface is provided on operating systems including Linux, MacOS and Windows.  

## Installation
For Mac Users, click following link to download **twiOpinionDisk.dmg**:   
![installByDmg](graphs/dmgCapture.png)
https://www.dropbox.com/sh/fvqerxiw8nbta8o/AABlKIQrV2LOoZ4eDDF8UHLIa?dl=1  

For Linux User, clone codes directly.  

## Usage
Helpful information will be displayed on the blue label at the bottom of each frame. Hover your mouse above buttons when you need more information.  

### Main function
Select the function you like to use by selecting radiobuttons and click **Start!**.  
Check your current working directory by clicking **Path**.   
For Mac users: the working directory will usually be in subfolder of /Applications. To access it by 'Finder', right click /Applications/twiOpinion and click *'Show Package Contents'*   

### Function 0.  Twitter Accessing Setting
Generate the configuration file necessary for crawling Twitter: 
* 0.0. Create an Twitter account if you don't own one.  
* 0.1. Go to https://apps.twitter.com.  
* 0.2. Enter your application name, description and your website address.  
* 0.3. Submit the form by clicking the *'Create your Twitter Application'*   
* 0.4. Copy the keys and tokens into entries in Step 0 of **twiOpinion**  

### Function 1.  Crawling From Twitter
Crawl real-time tweets by the keyword/tag you indicated:  
* 1.0. Fill the tag/keyword you wish to crawl from Twitter in the first entry.  
* 1.1. Fill in the folder you wish to store crawled data in, which is default as "./output"  
* 1.2. Click **Start!** to start crawling real-time tweets. Wait till you get enough tweets. Output file named "stream\_(Keyword).json."  
* 1.3. Three buttons will be activated to control the crawling process now.  
* 1.4. Click **Check** to check number of tweets that have been crawled up to now.
* 1.5. Click **Fetch** to process crawled tweets, output files named "stream\_(Keyword)\_Fetched.json." and "stream\_(Keyword)\_Fetched.txt." Explain later 
* 1.6. Click **Stop** to do fetch firstly and then stop crawling and exit current function. 

### Function 2.  Labeling Tweets 
### Function 3.  Learning and Classifying 
### Function 4.  Twitter User information 

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Professor Tommy W.S. Chow
* Hadrien VAN LIERDE 

