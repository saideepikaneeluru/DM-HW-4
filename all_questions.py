n# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Rules are not mutually exclusive because more than one rule can apply to a given situation, e.g., a home owner with low annual income would trigger both rule 1 and rule 3."
    answers["(b) explain"] = "The rule set is not exhaustive as there are combinations of attribute values not covered by any rule, necessitating a default class."
    answers["(c) explain"] = "Ordering might be necessary to prioritize certain rules over others, especially when multiple rules could apply."
    answers["(d) explain"] = "A default class is needed because the rule set is not exhaustive, ensuring the system can still make a prediction when no rules apply."


    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Each rule specifies a unique set of conditions, making them mutually exclusive."
    answers["(b) example"] = "The rules are not exhaustive as there could be animals that do not fit any of the provided categories, e.g., an aquatic creature that is warm-blooded."
    answers["(c) example"] = "Since the rules are mutually exclusive, each applying to a unique scenario, ordering is not necessary."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in English prose
    answers["(a) explain"] = "In back-propagation, the gradients of weights at the k+1th layer can be computed using the gradients of weights at the kth layer, utilizing the chain rule of calculus."
    answers["(b) explain"] = "While applying an ANN model, the activations at nodes at the k+1th layer are computed using the outputs of the kth layer, which is fundamental to how data flows through a network."
    answers["(c) explain"] = "The vanishing gradient problem refers to gradients becoming too small for effective optimization, not to the disappearance of training errors."
    answers["(d) explain"] = "Perfect classification of all training instances does not lead to zero gradients across all layers, as non-zero gradients are necessary for adjusting weights and potentially improving model generalization."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "independent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"  # Based on Naive Bayes assumption

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '+'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.38


    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5  
    answers["(b) K"] = 50 

    # explain_string
    answers["(a) explain"] = "A smaller K is chosen for scenario (a) to closely capture the nuances of the dataset's structure while avoiding overfitting."
    answers["(b) explain"] = "A larger K is selected for scenario (b) to ensure the classifier is robust to noise and can generalize well across overlapping data points."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float: Conditional probabilities based on the provided dataset
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # Explanation for the first case
    answers["(a) P(A=1|+) explain your answer"] = "The conditional probabilities are calculated by dividing the number of positive or negative instances where the feature equals 1 by the total number of positive or negative instances, respectively."
  
    # Probabilities for predicting class label for a test sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0

    # Predicted class label for the test sample
    answers["(b) class label"] = '+'

    # Reasoning behind the prediction
    answers["(b) Explain your reasoning"] = "The class label '+' is predicted for the test sample because the posterior probability P(+|R) is higher than P(-|R), indicating a higher likelihood of the sample belonging to the positive class."

    # Probability comparisons for parts (c) and (d)
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2
    answers["(c) A independent of B?"] = 'yes'
  
    answers["(d) P(A=1)"] = 0.5  
    answers["(d) P(B=0)"] = 0.6  
    answers["(d) P(A=1,B=0)"] = 0.3
    answers["(d) A independent of B?"] = 'yes'  

    # Conditional independence given class +
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4
    answers["(e) A independent of B given class +?"] = 'no'

    # Explanation for conditional independence
    answers["(e) A and B conditionally independent given class +, explain"] = "A and B are not conditionally independent given the class '+' because the joint probability P(A=1,B=1|+) does not equal the product of the individual probabilities P(A=1|+)P(B=1|+)."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    # answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    # answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
