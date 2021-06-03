# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
import nltk
nltk.download('punkt')


# %%
data = pd.DataFrame({'title' : ['I slept at 8 30 pm', 'I slept at 08:30 pm', 'I slept at 20:30 hours', 'I slept at 20:30', '8:30 am']})


# %%
data.head(10)


# %%
combinedData = ''
for text in data.title:
    combinedData = combinedData+''+text+'. '

print(combinedData)


# %%
sentences = nltk.sent_tokenize(combinedData)
print(sentences)


# %%
listOfWords = []

for sentence in sentences:
    sentence = sentence.lower()
    evaluatedText = re.search('8|20|08', sentence)
    if(evaluatedText != None):
        timePeriod = sentence[evaluatedText.span()[1]:]
        if(timePeriod.find('30') > 0):
            print('timePeriod: '+timePeriod)
            if(evaluatedText.group() != '20'):
                if( timePeriod.find('pm') > 0):
                    print('Correct Answer')
                else:
                    print('Wrong Answer')
            else:
                print('Correct Answer')


# %%



