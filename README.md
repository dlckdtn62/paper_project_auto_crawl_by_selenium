Paper Project

By Using Selenium

Process
1. At first we access on proxy site for preventing cannot access to Adult's link
2. After we search url + 'sign up' link on Google we click first link of result
3. We check on this page has 'next' button when sign up process
 - When this page does not have next button then we directly check separate privacy link and term link
 - When this page has next button then we put the needed information on page(Checking needed things by frequently used words)
 - for prevending footer tag's information we check whether this node on footer tag or not
4. After we land on final step, 'check consent condition'
 - GDPR says each page has to have consent button or similar function
 - By using DFS after we got on privacy words or term words, we ascend to their parent and check parent whether they have button or not
 
-----------------------------------------------------------------------------------------------------------------------------------
Next Step(Needed to be done)
1. Tokenizing the words for not mechanically type the similar words
2. Finkd sign up link by using NLP model
