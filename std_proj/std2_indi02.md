## COM5507 201819A *Social Media Data Acquisition and Processing*

### COM5507 201819A Individual Assignment 2 (20’, + 10 bonus points)

- Released at 8 Dec 2018
- Deadline: 16 Dec 2018, by email  

#### Overview
Task 2 contains two data cleaning challenges. You are required to choose one question. The datasets you will be working on are either machine-readable data format as the output of data acquisition, or a ready-made data released by an academic institution. Both are close to the datasets you will meet during the workplace.

**Q1**. [if you select Q1, you do NOT need to do Q2.] In this question, you are going to work on the csv file entitled "df_original_2col.csv." The file is in the folder [exp_text] (also attached in this email for your easy reference).

The task: 
1. fetch all the URL (links starting with http or https) (12 marks)
2. store all the URLs in a new column and export the file as a csv file (8 marks)
•	Hint: you can try regular expression, and you may refer to the Python scripts shared with you earlier, on text mining, ddj_mentions.ipynb, and ddj_hashtags.ipynb.
•	Difficult point: what if a user sends more than one URL? 

**Q2**.
[if you select Q2, you do NOT need to do Q1.]
In this question, you are going to work on a ready-made dataset, "gapminder_cleaned.csv," as shared with you in the folder [processing_num] (also attached in this email for your easy reference).

The task: 
Try to use data visualization as the approach of data exploration to find out the following questions: 
1. Globally, what is the relationship between life expectancy and GDP per capita? (6 marks)
•	Hint: what about a scatter plot?
•	Hint: try this: https://pythonspot.com/matplotlib-scatterplot/
2. Will the relationship stipulated in question 1 differ across different continents? (6 marks)
3. Will the relationship stipulated in question 1 differ across different countries? (8 marks)
•	Hint: 2 and 3 are asking the same conceptual question. However, as you can probably figure out, what we are testing here is the visualization method for these two variables across different conditions (countries or continents).
•	Hint: try this: https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html



**Q3**. bonus question, 10’. OPTIONAL
Also, this question focuses on the gapminder_cleaned.csv data. 
A term called “the third-wave of democracy” was once proposed (see Samuel P. Huntington). It argues that starting from 1974, there is a trend of “major surge of democracy in history” in the world. However, it has been always argued that whether “democracy” as a political belief or as a form of governance could actually bring social well-being (or actually, the progress of social change is driven by other factors). Putting any ideological arguments or opinions aside, let’s see how the data speaks to us. 

The consideration is: 
1. suppose the year of 1974 is treated as a boundary (a milestone cutting-off point), is there any difference of the social well-being before and after that year?
2. If a general answer to 1. is “yes” (as the world is becoming healthier and richer), then which countries (or continents) benefit the most? (and which are the least?) 
  - Hint and solution: what if we start the observation by focusing on two “dependent variables:” (1) life expectancy (LE), and (2) GDP per capita (GDPPC), and compare the average LE and GDPPC before and after 1974.
  - When there is a general trend that people are enjoying longer LE and greater GDPPC, the amount of growth is different across different countries. We can consider showing (i.e., plot) the differences of our focal variables before and after 1974 vis-a-vis different countries. 
  - If 1974 is not a year of significance, given a consideration that political system has a long-term impact on social change, how about selecting other cutting-off point?
  - the above accounts for 7 marks
3. What can you learn from the above data analysis? (3 marks)
•	Hint: what is the general pattern? will there be other alternative explanation to the pattern (confounding variables, for example)? If there are other reasons (besides the political system), can you think of any? 

#### Submission requirements
Please submit the following items:
1. The ipynb file, including all the codes questions (you can use “Markdown” cells to indicate the questions). You can write comments (#) to briefly spell out the function of the codes;
2. Directly type your answer into the notebook (either as comments (#) or the Markdown).
3. If you choose Q1, then a csv file should also included as the output;
4. If you choose Q2, then plots are embedded in the notebook.
5. No required word count – as long as you make sure all necessary information is clearly spelled out.
6. Once done, please put all the files (the original dataset, the ipynb file, or the output file, if any) in one folder, and name the folder as this: “com5507_assignment02_Name_studentid”
7. Please zip (zip, not RAR) the folder, and send the zip file (zip, not RAR) to me via this email address by 16 Dec 2018: xzzhang2@cityu.edu.hk

#### Representative students' works: Data exploration and data visualization

1. fetching the URLs

2. data exploration for comparative politics and social change
