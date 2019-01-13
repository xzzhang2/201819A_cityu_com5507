## COM5507 201819A *Social Media Data Acquisition and Processing*

### COM5507 201819A Individual Assignment 1 (20’)
- Released at 16 Oct 2018
- Deadline: 28 Oct 2018, by email (one week delay from the teaching plan)  

#### Overview
Task 1 is an automated online data acquisition challenge, i.e., to scrape some required information from one or many static webpages with Python Requests and BeautifulSoup packages in an automated manner, and store the information in a structured, machine readable data format as the output.

#### Information to be fetched
(starting from Q2, all the answers should be accompanied by the Python code)

**Q1**. The problem: what is the webpage (URL) you want to scrape? (1 mark) # suggestion: priority will be given to “public-oriented” webpages, such as governmental officials, academic institutions, Wikipedia public pages, NGOs (please check their term of use).

**Q2**. Quick warming up: please figure out the following information from the webpage from your Python code:
1. What is the “title” of this webpage, as stipulated by the “head” section? (1 mark)
2. What is the “description” of this webpage, as stipulated by the “head” section? (hint: <meta name = “description”> …, 1 mark)
3. What is the “keywords” of this webpage, as stipulated by the “head” section? (1 mark)
4. please print the first "second level headings" of your webpage, if any (if no, you can leave it blank) (1 mark).
5. please print all the text of the paragraphs of your webpage (1 mark).

**Q3**. Please identify the elements you want to scrape, by make a screen snapshot of your browser, with the “development mode.” Hover your mouse above the area of the element you want to scrape (a rough and approximate area will do). Like this (2 marks):

**Q4**. Now the scraping. Please scrape the information from the webpage, with the following requirements:
1. you are expected to scrape a set of information from the web, i.e., elements in the tables, elements in several tags, several files, or any other information that fit your purposes (5 marks);
2. you are expected to use at least one of the control flow statements to fine tune the code (5 marks);
3. You are expected to store the information in a structured format, and output the file in CSV format (2 marks). **Attention: please use “utf-8” as the encoding.**
4. Bonus (5 marks, optional) is offered for scraping multiple pages, using pre-defined rules.

#### Submission requirements
Please submit the following items:
1. A word file (word, not PDF), spelling out the your answer to Q1 and Q2, for Q3, write the following information:
  1. problem you define (what is the webpage);
  2. the tasks your code can perform (i.e., “scrape all the temperature information from the weather service); and
  3. the output (i.e., “the output is a CSV file; each row represents one city, and there are three columns representing variables: the weather, the temperature, and the degree”…etc).  
2. An .ipynb file, including all the codes. You can write comments (#) to briefly spell out the function of the codes;
3. A CSV file as the output.
4. No required word count – as long as you make sure all necessary information is clearly spelled out.
5. Once done, please put the three files in a folder, name the foler as this: “com5507_assignment01_Name_studentid”
6. Please zip (zip, not RAR) the folder, and send the zip file to me via this email address by 28 Oct 2018: xzzhang2@cityu.edu.hk


#### Representative students' works: Screen scraping

1. scraping a single page

2. scraping multiple pages (bonus)
