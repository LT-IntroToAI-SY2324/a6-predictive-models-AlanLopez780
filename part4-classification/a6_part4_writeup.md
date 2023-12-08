# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
The model isn't as accurate without the StandardScaler vs. with the StandardScaler. This could be because the StandardScale transforms the data so the predicted data can match the actual data as much as it can.
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
The StandardScaler model is pretty acccurate, though not fully accurate because the setup for the model is kind of vague.
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
There were very few instances where the predicted result didn't match the accurate results, but other than that, the model did well.
4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
Again, I don't know how to put the predict feature in the model.
