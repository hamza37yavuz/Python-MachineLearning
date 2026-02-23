MACHINE LEARNING (NOTES)

NOTE:
-These notes have been created to explain and summarize the topics found in the MachineLearning folder under their respective headings.

REGRESSION

    *Multiple Linear Regression

    -In simple linear regression it can be written as y = a + bx + e
    -e: means error rate. In multiple linear regression there are more than one b values.
    -b1x1+b2x2+.... the b values affecting y can be written this way. In this regression model there is a different e value for each x value.
    -It can be written as Height = a + b(weight) + c(shoe size).
----------------------------------------------------------------------------
    *Dummy Variable
    -Dummy variable is the name given to the multiple usage of a previously used and categorized column.
    -AI models are negatively affected by this usage.
    -If there are multiple data points they should be categorized. For example it could be about where a person is from.
    -In this case all categorized columns should be used.
----------------------------------------------------------------------------
    *p-value
    H0: null hypothesis
    H1: alternative hypothesis
    p value: probability value, generally 0.05
    As the p value decreases the probability of H0 being incorrect increases.
    As the p value increases the probability of H1 being incorrect increases.
    H0: Example: the assumption that if study hours increase, success can be achieved.
    H1: Example: the assumption that if study hours increase, success may not be achieved.
    The more H1 occurs the more H0 can be refuted, and the value that describes this is the p value.
----------------------------------------------------------------------------
    *Variable Selection
    -In multi-variable models, does every variable affect the result at the same rate?
    -How should variable selection be done?

    1* Include All Variables
        -All variables are included in the system and the result is evaluated.
        -This method can be used:
          if variable selection was done
          if it is mandatory
          for exploration (which method should I use)

    2* Backward Elimination (stepwise approach)
        a) A model is built by including all variables. A model success test is performed.
        b) Significance Level SL is chosen, generally 0.05.
        c) The variable with the highest p-value is examined.
            If P>SL proceed to the next step, if not go to the last step.
        d) At this stage the variable selected in the previous step with the highest p value is removed from the system.
        e) The machine learning model is updated and we go back to step c.
        f) The machine learning process is terminated.

    3* Forward Selection
        a) A model is built by including all variables. A model success test is performed.
        b) Significance Level SL is chosen, generally 0.05.
        c) The variable with the lowest p-value is examined.
        d) The variable selected in the previous step is kept constant and another variable is selected
            and added to the system.
        e) The machine learning model is updated and we go back to step c. If p<SL is satisfied
            for the variable with the lowest p-value we go back to c, if not we proceed to the next step.
        f) The machine learning process is terminated.

    4* Bidirectional Elimination (forward and backward elimination work together)
        a) A model is built by including all variables. A model success test is performed.
        b) Significance Level SL is chosen, generally 0.05.
        c) The variable with the lowest p-value is examined.
        d) The variable selected in the previous step is kept constant, all variables are included in the system
            and the one with the lowest p value stays in the system.
        e) Variables below the SL value stay in the system.
            None of the old variables are removed from the system.
        f) The machine learning process is terminated.

    5* Score Comparison
        a) All possible models are built by determining a success criterion.
        b) The method that best satisfies the initially determined criterion is selected.
        c) The machine learning process is terminated.
----------------------------------------------------------------------------
    *POLYNOMIAL REGRESSION
    -Shows that the same variable creates a parabolic curve with different coefficients and exponent values.
    -Contains the method we will use when predicting curves.
----------------------------------------------------------------------------
    *SUPPORT VECTOR REGRESSION SVM (MACHINE)
    *SUPPORT VECTOR
    -The method normally used to separate two classes is used to separate two clusters with maximum margin
        and also used to create a margin that contains the maximum point in regression.
    -The smaller the margin, the healthier the regression will be.
    -Functions that are not linear and where this prediction method is used:

    Linear, Non-linear
    Linear          exponential
                    RBF gaussian
                    polynomial
----------------------------------------------------------------------------
    *Decision Tree DECISION TREE
    -A decision tree is created in 2-dimensional space.
    -Splits are created according to the distribution of data.
    -Predictions are made from the created splits using averages from the training set.
    -If this algorithm needs to be more sensitive, the number of splits needs to be increased.
----------------------------------------------------------------------------
    *RANDOM FOREST
    -Ensemble Learning means collective learning, using multiple models.
    -Data is divided into segments using decision trees and the divided segments are further split to benefit from this.
    -Predictions can be made by utilizing averages among these small split trees.
    -There are new methods regarding how to combine them.
    -Taking all values in decision trees can sometimes increase errors.
    -Reasons for this: - if it learns everything it memorizes, overfitting occurs
                       - if it takes too much data the tree branches too much, which reduces processing speed
__________________________________________________________________________________________________________________________

COMPARING REGRESSION METHODS (EVALUATION OF PREDICTIONS)

    *R Square Method

    -Sum of squared errors: sum(data - predictedData)^2
    -Sum of mean differences: sum(data - dataMean)^2
    -R^2 = 1 - SSE/SMD
    -If R^2 comes out as 0, it is said to be a dumb algorithm.
    -Because if it is 0, the average of the values should be the same as all values.
    -R^2 can take negative values but a negative result indicates the model is bad.
    -If R^2 = 1 it says it is a perfect algorithm. In the real world we have no chance of seeing 1.

    *Adjusted R Square Method

    Downsides of R square method:
    -The R^2 value is not a sensitive value. It can mask some positive work we have done.
        *Consider a linear regression with two separate coefficients. We obtained an R^2 value.
        *But we decided to add a new coefficient to the regression.
        *In this case we obtained a linear regression with 3 separate coefficients.
        *When we obtain the new R^2 value we expect the new value to be different from the old one.
        *Because the new variable should have either a positive or negative effect. However R^2 value may not change.
        *Because the new variable we added never decreases the R^2 value.
        *Because if it has a negative effect, the coefficient is taken as 0.
        *For this reason it prevents us from seeing the effect on the algorithm.
    -Due to the situation explained above, the adjusted R^2 method is used.
    -Adjusted R^2 = 1 - (1-R^2)(n-1)/(n-p-1) this is how the problem we wrote above is solved.
    -There are also different methods besides these, and we should know that they have disadvantages.
    -We should not forget that the adjusted R^2 method also has disadvantages.
    -Let us see that an important issue has been corrected here and let us not forget that there can be alternatives.
__________________________________________________________________________________________________________________________

---CLASSIFICATION PROBLEMS---
-It can be defined as predicting non-numerical data.
-If we are making numerical predictions it is regression. If we want to determine the category of data we can do classification.

--------------------------------------------------------------------------------------------------------------------------
    *LOGISTIC FUNCTION REGRESSION
    -It allows us to classify by obtaining a step function.
    -Step function: A function that gives 0 for values below a certain value and 1 for values above it.
    -A linear function, step function or sigmoid function can be used as a step function.
    -Classification can be done using one or more variables.
    -It is possible to see S-shaped functions.
    -The data to be used in this algorithm must be scaled.
    -Classification as male/female based on height and weight values falls into this category.
    -Mathematically expressed as L(t) = (e^t/e^t+1) = (e^t/e^-t+1)  t = A + Bx
----------------------------------------------------------------------------
    *CONFUSION MATRIX
    -It was created for certain data coming from medicine.
    -It gives the accuracy rate between actual and prediction.
    -It is a matrix containing predictions and actual states.
    -How a confusion matrix looks:
        [a,b] The magnitude of the ratio (a+d)/(a+b+c+d) represents the success of the model.
        [c,d] The value calculated above is expressed as accuracy.
        a -> true positive b -> false negative
        c -> false positive d -> true negative
    -True Positive Rate: if actually yes, how many were correctly classified?
    -False Positive Rate: if predicted no, how many were correctly classified?
    -Specificity: if actually no, how many were correctly classified? d/(d+c)
    -Precision: if predicted yes, how many were correctly classified? a/(a+c)
    -Sensitivity: a/(a+b)
    -Prevalence: the ratio of actual yes distribution.
    -This matrix only makes sense in classification problems.

    *ERROR TYPES
    -false positive Type 1 Error
        when something we said yes to is actually no
    -false negative Type 2 Error
        when something we said no to is actually yes
----------------------------------------------------------------------------
    -Error in SVM
    -Test data appearing within the risk area and being misclassified.

    *ACCURACY PARADOX
    -The ZeroR algorithm classifies test data according to the majority class in the training dataset.
    -It may sometimes appear more successful than a normal classification algorithm but caution should be taken.
    -In such cases we should not make decisions by only looking at Accuracy.
    -We can use different values within the confusion matrix aimed at achieving balance.

    -ROC CURVE Receiver Operating Characteristic
    -tpr = TP/TP+FN  TP -> true positive tpr -> true positive rate. A high value here INCREASES the error rate.
    -fpr = FP/FP+TN  FN -> false negative fpr -> false positive rate. A high value here DECREASES the error rate.
    -It allows us to visually understand where the machine learning algorithm stands.
    -It can be used for graphical comparison of different classification algorithms.
    -In Accuracy Lines the ratio of datasets is found according to the positive/negative ratio.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    *KNN K NEAREST NEIGHBORHOOD:
    -Data to be classified is plotted in space.
    -A data point is selected and the 3 (k) nearest neighbors are chosen.
    -Whichever class the majority of these neighbors belong to, the selected data belongs to that class.
    -If the neighbors are equal in number from each class, distance is considered.
    -What we described above is an example of lazy learning. That is, the type where no learning is done at the beginning.
    -In another version (eager learning) data is processed first and features are extracted.
    -According to the extracted features, the space is divided into regions. The data is no longer needed.
    -If new data comes in, a decision is made by looking at which region it falls in.

    -There are also different calculation methods for measuring the distance between two data points.
    -Euclidean, Minkowski, Mahalanobis are examples of these calculations.
    -It is important which measurement is suitable for which dataset, and this selection should be done carefully.

    -When using this algorithm there may be outlier data that could corrupt our dataset.
    -In this case selecting too many neighbors is not a good thing.
    -Because neighboring outlier values in such a situation will not find enough neighbors and will be included in the wrong class.
    -The number of neighbors should be selected considering the point I wrote above.

    How is the k value determined in the KNN algorithm:
        Let us review the algorithm through Voronoi cells.
        Search the web for images or data about these cell situations.
        Let us think about the state of k on this data.
        This situation has been discussed at length in the Pattern Classification book.
        A general formula has been found: sqrt(training size)/2. This is a debatable formula.
        It is not a rule. The K number can change according to your needs.
    What happens if data falls on the class boundary in the KNN algorithm:
        In this case it is calculated which one it is closer to.
        For example if the blue samples are closer to the boundary, the tie is broken.

    Resources
    You can search sklearn knn and look at the sources.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    *SVM CLASSIFICATION SVC MULTI CLASS
    -Nearly the same things are said as with the regression method.
    -In classification, a sharp separation of two classes is attempted.
    -RBF or polynomial/exponential can be used. These usages should be selected according to the dataset.
    -Not very suitable for outliers.
    -Also unscaled datasets cannot be used in SVM.
    -Cannot be used in datasets with very extreme outliers.
    -After a separation is made between two classes, the dataset is forgotten.
    -New data is classified on the class separation, that is, the space regions.
    -So the region where the data is located determines its class.
    -If it does not accept any data inside the margin it is called hard SVC.
    -If it accepts data it is called soft SVC.
----------------------------------------------------------------------------
    *SVM KERNEL TRICK
    -Used for data that is not linear and cannot be solved linearly in any way.
    -The center point of the non-linear area is found and another dimension is added to the dataset.
    -The center point we determined becomes the closest point to us.
    -Values close to the center point become closer to us, values far from the center point become farther from us.
    -This provides us the opportunity to create two clusters: far and close.
    -Dimension increases can be done this way.
    -Classifications are made precisely by drawing different lines on the newly formed multi-dimensional cluster.
    -Also more than one kernel trick can be used on a dataset.
    -How is this pulling operation done:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    *NAIVE BAYES
    -Used to solve classification problems by utilizing conditional probabilities.
    -With conditional probability, the rate of buying a computer based on income level can be found.
    -You can classify people who buy computers according to their income level.
    -Its most important feature is that it can work with imbalanced datasets.
    -First the rate of buying and not buying a computer is calculated.
    -The rate of a person under 30 buying and not buying a computer.
    -In this way our classification can be done easily through the conditions we have separated.
    -Lazy learning: data comes first, it waits within that data, if data flow continues it performs learning.
    -Eager learning: before data comes, it tries to learn all possibilities from all data.
    -In big data studies, lazy learning is more advantageous.
    -Gaussian naive bayes - multinomial naive bayes - bernoulli naive bayes
    -For continuous values  - for discrete numbers  - for binary data
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    *CLASSIFICATION WITH DECISION TREE
    -We explained the splitting into regions above.
    -The area where the majority is found is classified according to the majority.
    -And for new incoming data, a decision is made according to the created regions.
    -Sometimes splitting operations can continue for values that are close to each other.
    -But here, separating all data one by one should be avoided.
    -Otherwise overfitting occurs and the program memorizes all data.
    -In decision trees, if there are no ordinal or nominal data, classifications can be started directly.
    -But if it contains numerical values, a separate algorithm is used to split the numerical values.
    -Tree branching can be solved with Quinlan's ID3 information (Gain) method.
    -Here it says that the one with the highest value will make the first branch.
    -Computers create tree structures this way.
    -We will use the CRITERION parameter from the documentation parameters.
    -Gini: the sum of the negatives of p*p
    -Entropy: the sum of the negatives of p*log(p)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    *RANDOM FOREST
    -Ensemble learning: the data is divided into parts and decision trees are created from the parts.
    -Each decision tree is finally combined and classification is done according to the majority.
    -There is an article written about motion detection in Xbox by Microsoft (link below).
    -It is an algorithm built on the majority vote algorithm.
    -N_estimators: how many trees should I create?
    -Criterion: was it specified in the decision tree?

    ADA BOOST - QDA - GAUSSIAN PROCESS - NEURAL NET


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    *CLUSTERING

    -Topics such as image processing and customer segmentation are included here.
    -The number of classes or how they will be classified is not given beforehand.
    -It is unsupervised learning.
    -There is no separation as train/test data here.
    -The difference from classification problems is that there is no class definition and train/test split.
    -It creates its own classes in its own world. Currently there is no very advanced model for it.
    -It is most commonly used in customer segmentation, market segmentation, and health image processing fields.
    -Customer segmentation -> Collaboration Filtering: grouping a customer with people similar to them.
    -It allows placing a person with no prior data into a segment.
    -It is used in areas like creating special campaigns, detecting threats and fraud, and completing missing data.
    -Threat and fraud detection is built using outlier data.
    -In missing data completion, data completions can be done according to different segments of the data.
    -It is mostly about creating segments by making sub-classifications of an already classified data.
----------------------------------------------------------------------------
    *K-MEANS
    -The number of clusters is taken as a parameter from the user.
    -There is also a version that decides on its own without taking it from the user (Ex means).
    -It randomly selects k center points.
    -Each data sample is assigned to the cluster related to the nearest center point.
    -New center points are created for each cluster and shifting is done.
    -Shifting is done according to the centers of gravity.
    -It stops when the center of gravity keeps coming out at the same place.
    -It is unsupervised learning; every data holds equal value for the model.
    -In different variations, the center point selection and parameter taking from the user may differ.
----------------------------------------------------------------------------
    **K-Means Starting Point Trap
    -The random starting point being distributed to wrong data spaces can negatively affect clustering.
    -Consider a dataset that can easily be divided into 3 classes.
    -In the case where centers are randomly distributed, there is a possibility of two centers going to one class.
    -This possibility should be taken into consideration.
    -Using different solutions instead of random center assignment would be more accurate.
----------------------------------------------------------------------------
    **K-Means++
    -It is the improved version of K-Means.
    -It calculates the distance to the nearest point from randomly selected points at each step.
    -It finds new points by taking the square of the distance as probability.
    -There is also randomness here which can cause issues.
----------------------------------------------------------------------------
    **The Importance of How Many K
    -The selection of K is important because it is an unsupervised learning algorithm.
    -The Ex means algorithm outputs the score of all clusterings within a given range.
    -But let us not forget that how to find success is another problem.
    -This scoring is done with the WCSS method (within-cluster sums of squares).
    -A center is selected and the squares of the distances of the data in its cluster to it are summed.
    -The higher this score the worse the clustering algorithm can be said to be.
    -But this score should not be reduced too much to avoid overfitting.
    -Creating a graph and making decisions based on the graph would be more accurate.
    -In the created graph, the elbow point where the slope changes suddenly is generally taken as the correct point.
    -You can get information about which method to use from "Overview of clustering methods".
    -You can get this from the scikit-learn website.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    *HIERARCHICAL CLUSTERING
    **Agglomerative
    -Works from bottom to top.
    -Each data starts as a single cluster.
    -The two closest neighbors are taken and clusters of two are created.
    -The two closest clusters are taken and a new cluster is created.
    -Continues until there is a single cluster.
    -The class structures within are not lost.
----------------------------------------------------------------------------
    **Divisive
    -Classification happens from top to bottom.
    -All data is accepted as one cluster.
    -Points close to each other are clustered. It ends when the last single point is added to a cluster.
    -In short it is the exact opposite of agglomerative.
    -It terminates when a single data point is placed in a package.
----------------------------------------------------------------------------
    *Things to Pay Attention To:
    -Distance measurement is a problem in these algorithms.
    -Distances can be shown with a distance matrix.
    -Euclidean distance can be used.

    -References are another problem. There are different solutions for this.
    -The closest points can be taken as reference.
    -The farthest points can be calculated.
    -The center point of the cluster can be taken as reference.
    -Averages can be taken as reference.
----------------------------------------------------------------------------
    **Dendrogram
    -A table structure where all points are written and placed according to the distance between them.
    -Merges can be shown in this table structure.
    -It allows the readable display that cluster merges depend on distances.
    -Hierarchical clustering is easier to see according to this table structure.
    -It provides the user the opportunity to create as many clusters as desired.
    -To obtain the most optimum structure, the longest section of the dendrogram can be examined.
----------------------------------------------------------------------------
    *WARD METHOD
    -The distance of each cluster to another cluster.
    -It uses the WCC value calculation method.
    -The optimum model can also be found using the Ward method.
    -You should research this.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    *ASSOCIATION RULE MINING/LEARNING ARM/ARL
    -3 different types can be examined: apriori, fp-growth, eclat.
    -We will examine apriori and eclat.
    -Fp-growth will be researched.
    -It can be said that these algorithms are needed due to shopping habits.
    -It is a model used when catching recurring data.
    -Like those who buy pears also bought apples.
    -It is based on the question: is it correlation or causation? Causation vs Correlation.
    -The foundation is based on the fundamental question: do machines think like humans?
    -For the computer, if two products are sold together it does not question why.
    -It just sells those two products together.
    -The computer looks at the relationship between ice cream sales and shark attacks.
    -Here computers do not consider causation, meaning they do not ask why they happen at the same time.
    -We ask and attribute it to the sun.
----------------------------------------------------------------------------
    **SUPPORT
    -Think of it as "we asked a hundred people". The existence of the action is important.
    -What percentage an action was performed.
    -Support(a) = (actions containing the existence of a) / (total number of actions)
----------------------------------------------------------------------------
    **CONFIDENCE(a->b) = (actions containing both a and b) / (actions containing a)
    -The percentage of people who performed action a that also performed action b.
    -This method can be used when there is not a single product/action.
----------------------------------------------------------------------------
    **LIFT(a->b)  confidence(a->b) / support(b)
    -It answers the question: what is the effect of action a on action b?
    -If the lift value comes out below 1, action a negatively affects action b.
    -If the lift value comes out above 1, action a positively affects action b.
----------------------------------------------------------------------------
    **EVENT FREQUENCY (APRIORI)
    -First we look at the ratios by breaking down.
    -Then we go from parts to whole and eliminate data with low frequency.
    -Then we make some combinations considering the effects of those parts on each other.
    -We try to achieve the best situation.
    -Let us do an example:
        let us have a list of products bought together.
        itemset 1, 2, 3, 4, 5
        sup     3, 3, 3, 1, 3
        Here product number 1 was ordered together with 3 different products at different times.
        APRIORI goes from parts to whole by eliminating. For example in the first step it eliminates product number 4.
        Then it makes different combinations and shows them again as a 2-item table.
        It eliminates again and finds the 3 products that sell together.
    -It is used in classifications and marketing recommendations this way.
    -There is no function or class in scikit-learn for this algorithm.
    -When you want to use it, download it from GitHub.
----------------------------------------------------------------------------
    **ECLAT ALGORITHM
    -Equivalence Class Transformation

    -Apriori -> Breadth First Search
    -Eclat -> Depth First Search

    -Eclat is much shorter in steps compared to Apriori. It is considerably shorter than Apriori.
    -The database is arranged as a vertical graph. For example which baskets product number 1 was purchased in.
    -The next steps can be reached without reading all the data.
    -The intersection of data in the vertically drawn table is examined.
__________________________________________________________________________________________________________________________

REINFORCEMENT LEARNING

    -Reinforcement learning is about robots and their movements. A robot that constantly falls gradually reduces its frequency of falling.
    -In short it refers to an algorithm learning from its mistakes.
    -It can be thought of as reaching the most optimized state in achieving the goals we define.
    -The written algorithm performs an action and observes and scores the action.
    -According to the scoring there are penalties and systems try to achieve the best state this way.
    -AlphaGo is an example of an AI that learned chess by playing against itself (you should also learn by researching).
    -In expert systems the best level it can reach can be thought of as human level.
    -But algorithms developing this way can be better than humans in specific subjects.
    -Agent -> environment -> agent -> environment: the model continuously cycles in an infinite loop.
    -Let us examine the following heading:

    *ONE ARMED BANDIT SLOT MACHINES
    -You went to a casino and saw many slot machines.
    -These machines give back 80-90% of your money.
    -You explored these machines and examined the distributions.
    -Even if they all win at the same rate, we want to examine the distributions and select the most profitable machine.
    -This theory is based on the part I wrote above.
    -It can be found with a reinforcement method. The research is up to you :)

    *A-B TEST
    -Used to find out whether an ad will be clicked by the user.
    -By showing multiple ads to users, people's reactions are measured and results are recorded.
    -By looking at the results we need to make decisions in the fastest way and with the fewest trials.
    -A decision can be made with a reinforcement method.

    [+] THE FIRST ALGORITHM OF THIS TOPIC: UCB Upper Confidence Bound

    *UPPER CONFIDENCE BOUND
    -There is a distribution behind every event.
    -The user performs an action each time (event e).
    -A score is returned in exchange for this action. Let us list the steps by giving an example of this action.
    -For example let us calculate over an ad rate, clicking 1 not clicking 0.
    -The goal is to maximize clicks.
    -We have two situations as lower bound and upper bound: perfect situation and worst situation.
    -To detect the unknown hidden distribution, some parts of the distribution are eliminated through trials.
    -After these eliminations, the best situation is tried to be obtained in the fastest way.
    -This algorithm takes the one with the highest value among alternatives after a certain stage.
    -It tries to obtain the closest situation to the optimum by accepting a certain error rate.
    -Let us look at the following scenario:

    SCENARIO
    Ad Data: the most clicked ad will be found, the first 5 days will be examined, on the 6th day the most shown ad will appear in front of the user.
----------------------------------------------------------------------------
    *Random Selection:
        -Does not make any intelligent selection, selects randomly, reward earning logic works.
        -Random ads are selected from a pool and shown to users.
        -The ones users click earn points. The ones they skip lose points.
        -Can we reach the most optimized result with this logic?
        -We will try by writing the Python code.
        -Something important here is that the click frequencies of ads are not equal.
----------------------------------------------------------------------------
    *UCB Algorithm:
    -STEP 1: In each round, let the round number be n. For each ad alternative the following numbers are kept:
        Ni(n): the number of clicks of ad number i up to that point.
        Ri(n): the total reward for ad i up to that point.
    -STEP 2: From the two numbers above, the following values are calculated:
        The average reward of the ad up to that point: Ri(n)/Ni(n)
        The potential to swing up and down for the confidence interval: di(n) = ((3/2)*(log(n)/Ni(n)))^(1/2)
    -STEP 3: The one with the highest UCB value is selected.
----------------------------------------------------------------------------
    REINFORCEMENT LEARNING:
    *THOMPSON SAMPLING:
    -Step 1: We must calculate two numbers for each action.
        Ni1(n): the number of times reward 1 has come up to that point.
        Ni2(n): the number of times reward 0 has come up to that point.
    -Step 2: For each ad we generate a random number from the Beta distribution given below.
        Oi(n) = B(N1i(n) + 1, N0i(n) + 1)
    -Step 3: We select the highest Beta value.
    -It is an algorithm that follows the Bayesian approach, closer to Bayes.
    -UCB can be called a greedy algorithm compared to this algorithm.
    -When you do not have enough data and need to both learn and apply from a small amount of data.
    -In situations where observations are not equally distributed.
    -UCB is used in jumps. Thompson is done with a linear progression.
__________________________________________________________________________________________________________________________

NATURAL LANGUAGE PROCESSING

    2 types of goals can exist:
    *Natural Language Understanding NLU
    -Like all machine learning models, it has an algorithm consisting of 3 steps.
    -Data preprocessing - feature extraction - learning. THE FOLLOWING CONCEPTS SHOULD BE RESEARCHED
        -Data preprocessing: Stopwords, case, parsers
        -Feature extraction: word counts, word groups, N-gram, TF-IDF
    *Natural Language Generation NLG

    Approaches
    *Linguistic approach
        -Analyzes according to sentence structure, performs stem and suffix analysis of words.
        -For this reason it works slowly but is more accurate.
        -Some details of the steps of this approach are below.
        -Morphology: all alternatives are listed, all possible meanings of a word are taken.
        -Syntax: the position of the word whose meanings are listed within the sentence is determined.
        -Semantics: from the meanings specified in the morphology part, which one fits the syntax is found.
        -Pragmatics: it is checked whether the word used is irony or not.
--------------------------------------------------------------------------------------------------------------------------
    *Statistical approaches
        -In text classification, it is possible to understand what topic the text is about without understanding the meaning of words.
        -In short, it examines how many times a word appears in a text.
        -N-gram finds the probabilities of certain characters appearing consecutively.
        -TF-IDF
        -Word-Gram
        -BOW Bag Of Words: can detect things like whether a mail is spam or not.
            words that are in spam mail and those that are not are put in different bags and counted from the text.
    *Hybrid approaches
        -An approach that tries to make sense of text by mixing the two approaches.
----------------------------------------------------------------------------
    *USAGE EXAMPLES
    -Author Recognition
    -Text Classification
    -Sentiment Polarity / Opinion Mining
    -Anomaly Detection
    -Text Summarization
    -Question Answering
    -Tag Finders and Keyword Extraction
----------------------------------------------------------------------------
    *LIBRARIES
    -nltk
    -Spacy: Industrial
    -nlp: Stanford University
    -OpenNLP: Apache Open Natural Language Processing
    -RAKE (Rapid Automatic Keyword Extraction)
    -Amueller Word Cloud
    -TensorFlow Word2Vec
----------------------------------------------------------------------------
    *TURKISH NATURAL LANGUAGE PROCESSING LIBRARIES
    -Zemberek
    -ITU
    -TSPELL
    -Yildiz Technical University Kemik
    -Wordnet Balkanet
    -TrMorph
    -TSCorpus
    -Metu-Sabanci Tree Bank and ITU Validation Set
----------------------------------------------------------------------------
    -In machine learning there is no situation of using ready-made data.
    In NLP machines should approach humans in terms of extracting human features.
    Machines are not equivalent to us in terms of features.
    For this reason data is first put through preprocessing, then data features are extracted.
    After that machine learning algorithms are applied.
    Data preprocessing: preprocessing, stop words, case, Parsers (html)
    Feature extraction: feature engineering, word counts, word groups, n-gram, TF-IDF
__________________________________________________________________________________________________________________________

ARTIFICIAL NEURAL NETWORKS

    -It refers to creating an artificial intelligence by forming structures similar to nerve cells in the human body.
    -Keywords:
        Neuroscience and computer science
        Neuron
        Synapse
        ANN working logic
        Gradient Descent
        Stochastic Gradient Descent
        Backpropagation

    -In this model data must absolutely be standardized, it must be in the 0-1 range.

    Note: [+] Neural networks do not always require preprocessing if your number of neurons is sufficient.
         [+] Because the extra neurons you provide do the preprocessing for you.

    -In this model outputs also come in the 0-1 range. Results are formed based on this.
    -Outputs can also be in a multiple form. Multiple outputs can be seen.
    -Weights are carried on synapses and these weights affect the decision-making process.
    -Inputs are updated with weights through an operator and transferred to the output.

    -As an example, inputs are multiplied by weights, results are summed, and the network gives output based on this result.

    -For a neuron to be activated, there is an activation function.
    -Whether activation will occur in the neuron is decided based on the output of this function.

    *Activation function and its types:
        -These functions can be thought of as the threshold value of a neuron's electrical signal in the human body.
        -Any function can be used as an activation function (generally).
        -But some functions are used more frequently.
        -Sigmoid functions: 1/(1+e^-t) is the most commonly used function.
        -Step function is a function with a threshold value, a function that makes a jump after a certain point. It returns either 1 or 0.
        -Sigmoid functions take values between 0 and 1 without a specific threshold value.
        -If thought graphically, it can be seen that it will give values in the [0,1] range as output.
        -The Rectified function gives a value of 0 in a certain range.
        -After a certain value it takes values greater than 0. A function like max(0,x) can be considered.
        -Tanh function (this will be researched)

    *Artificial Neural Networks:
        -It consists of 3 layers: input layer, hidden layer, and output layer.
        -The number of hidden layers can increase. Or the number of neurons in the hidden layer can increase.
        -The output layer and hidden layer consist of neurons.
        -In artificial neural networks, how many neurons will be in the hidden layer is important.
        -We can use the coordinate system to determine this.

        |           How to determine the number of neurons, let us look at the example below:
        | .       .     In the square on the side we want to design an artificial neural
        |               network that contains the diagonal points. We have two inputs
        | .       .     and one output. How many neurons in the hidden layer?
        |___________    We can only divide the space linearly.

        In this case if we want the diagonals to be within the output, we should use at least two neurons.

    *How Artificial Neural Networks Learn:
        -The learning here is simply about increasing and decreasing the numerical values of weights and thresholds.
        -The simplest learning Perceptron: a penalty mechanism works.
        -Penalty = 1/2 (actual - prediction)^2. With each wrong prediction, weights are multiplied by the penalty.
        -It should not be forgotten that this multiplication can also be done with different values.
--------------------------------------------------------------------------------------------------------------------------
    Gradient Descent:
        -During learning in artificial neural networks, weights are multiplied by certain values.
        -This learning process involves a lot of computation in multi-layered neural networks.
        -We need to systematize the learning process and find the right learning method.
        -If large learning rates are used, it can be observed that weights keep oscillating between 2 different values and cannot find the correct value.
        -By using small learning rates, the point where the correct condition is met is tried to be found.
        -Gradient descent is exactly the name given to this situation.
        -In short, it was created to prevent weights from going back and forth between the same values.
--------------------------------------------------------------------------------------------------------------------------
    Stochastic-Batch Gradient Descent:
        -It is a different type of gradient descent. Developed for local minimum points.
        -Let us assume we are trying to find the absolute minimum point.
        -We will need an algorithm that prevents us from taking a local minimum point as the absolute minimum.
        -Stochastic makes decisions without seeing all the data.
        -Batch looks at all the data to distinguish these minimum points.
        -There is also another algorithm called mini batch approach. It can be named as making decisions by reading a certain portion of the data.
        -The purpose of these approaches is to find the most optimum data in the dataset we receive or to give the most appropriate meaning to the data we receive.
--------------------------------------------------------------------------------------------------------------------------
    *Backpropagation (Backward Propagation)
        Algorithm Steps:
        1. Initialize the entire network with random numbers (close to zero but not zero).
        2. The first row from the dataset is given to the input layer. (Each feature is one neuron)
        3. Forward propagation is done and the ANN is updated until it gives the desired result.
        4. The difference between actual and output is calculated.
        5. Backpropagation is done and the weight on each synapse is changed by the amount it is responsible for the error. The amount of change also depends on the learning rate.
        6. Steps 1-5 are updated until the desired result is obtained.
        7. After the entire training set is run, one round (epoch). Round repetitions are done using the same datasets. (the number of rounds can be limited)
--------------------------------------------------------------------------------------------------------------------------
    -Learning rate represents the learning speed. Epoch represents the number of rounds.

    (Reinforcement learning or update all at once after running all available data through the relevant network) These are for step 6.

    *Forward Propagation
        -Let us finish this topic by discussing its difference from backpropagation.
        -Forward propagation is the process of advancing the neural network from input data to produce output.
        -Backpropagation is a learning mechanism used to update weights by propagating the error backward.
        -During the forward propagation phase the outputs of the network are calculated, while during the backpropagation phase the weights of the network are updated and the network is made to produce better results.
        -The difference is that one makes corrections while going to the result and the other corrects the weights in neurons coming from the result.

__________________________________________________________________________________________________________________________

DIMENSIONALITY REDUCTION

    *PCA:
        -Use cases: Noise filtering, Visualization, Feature extraction
                   Feature elimination/transformation, Signal processing, Image processing
        -It can be defined as dimension transformation. Of course data can be lost while transforming dimensions. Care must be taken.
        -Eigenvalue and Eigenvector are two concepts to remember here.
        -Let us remember with an example:
        [+] A matrix can have more than one eigenvalue and eigenvector.
            [1 2 0]   [1]   [3]      [1]   A*v = x*v  x: eigenvalue v: eigenvector
            [0 1 2] * [1] = [3] = 3* [1]   For this matrix 3 is the eigenvalue
            [1 0 2]   [0]   [0]      [0]   1,1,0 is the eigenvector

        -Projection matrix w: a square matrix representing the projection of a vector in a space.
        -(detail https://medium.com/kaveai/matemati%C4%9Fi-ve-python-uygulamas%C4%B1yla-lineer-regresyon-normal-denklem-dd38c43e0941)

        Algorithm Steps:
         -Let k be the dimension to be reduced to.
         -Data is standardized.
         -Eigenvalues and eigenvectors are obtained from the covariance or correlation matrix, or SVD is used. (SVD: singular value decomposition)
         -Eigenvalues are sorted from largest to smallest and k of them are taken.
         -From the selected k eigenvalues the projection matrix w is created.
         -The original dataset X is transformed using w.
         -The K-dimensional Y space is obtained.


    LDA: LINEAR DISCRIMINANT ANALYSIS
        -It performs a dimension transformation similar to PCA. But it does this job in a supervised manner.
        -That is, while PCA does unsupervised reduction, LDA does it supervised.
        -LDA reduces by considering class differences and labels.
        -In LDA the goal is to find the best dimension that separates classes from each other.
        -In PCA the goal is to find the most useful dimension that separates data from each other.
        -Read this article: https://sebastianraschka.com/Articles/2014_python_lda.html
        -The algorithm steps are actually not very different from PCA.
        -The biggest difference is in the first step. You can read the article above for detailed information.
__________________________________________________________________________________________________________________________

HOW TO SELECT A MODEL BASED ON THE PROBLEM:

    -The success of models depends on parameters.
    -Machine learning does not optimize parameters.
    -We need to optimize parameters according to our own experience and wishes.
    -The first point to pay attention to before model selection is model evaluation.
    -Until now we measured success on the test set. (we did split validation)
    -After the data was split we looked at the suitability of machine learning, but not anymore!
    -New terms: K-fold cross validation, Grid Search
        The algorithm used for model selection may differ according to the type of problem.
    -Whether a dependent variable exists is also an important criterion for this difference.
    -If there is no dependent variable, it can be said to be unsupervised learning.
    -If there is no dependent variable, it will be classification or regression.
    -After this stage, whether the dependent variable is categorical or continuous is also an important criterion.
    -Another stage is that the distinction between linear or non-linear is also important.
    -In short, examining the data well and making decisions as a result is the most correct way.

    **K-Fold Cross Validation:
         -In cross validation, in the n-fold expression let n = 4.
         -First it splits the data as +++- where - is the test set and + is the train set. It calculates the success rate.
         -Then it calculates the success rate again as ++-+. Calculates again as +-++. Calculates again as -+++.
         -It makes decisions based on the values found in these calculations. After this part there are different variations of this algorithm.
         -The decision mechanism can be based on the average of values, by taking the minimum value, or in a different way.
         -Depending on the n value here, the data is traversed n times.
         -This algorithm is mostly used for classification algorithms.


    **Grid Search
         -Optimizing the parameters that the algorithm we run will take is also important.
         -We will look at this part through code and explain it.

__________________________________________________________________________________________________________________________

XGBOOST EXTREME GRADIENT BOOSTING
    -Link to read -> https://xgboost.readthedocs.io/en/stable/
    -Can work in most environments.
    -Works fast.
    -Shows good performance on large data.
    -Makes interpretation of the problem and model possible.
__________________________________________________________________________________________________________________________

HOW TO SAVE MODELS
    -There are 3 different saving standards named Pickle, Joblib, and PMML.
    -Let us see how this operation is done through Pickle.
    -After the machine is trained, how will the model be saved to a file?
    -We will code with Python for pickle.

__________________________________________________________________________________________________________________________

NOTE: [+] Check the 2001 Jamie Hutchinson IEEE article about image processing.

CNN CONVOLUTIONAL NEURAL NETWORK
    -Artificial neural networks can use this model when processing images.
    -It should not be forgotten that the perception of the image can change according to features.
    -CNN has developed rapidly with the development of hardware units.
    -Facebook's face tagging person asking/confirming process.
    -Recognizing check signatures.
    -CNN is based on finding differences.
    -CNN's most important feature is its advantage over other models in feature extraction and finding differences.
    -In short CNN contains some steps of machine learning within itself.
    -CNN consists of 3 basic operations:
        Convolution and Non-Linear
        Pooling: (helps us shrink the image)
        Flattening
        Neural Network (activation function customizations)

    *CONVOLUTION:
    -It is actually a filter.
    -It can be said that the inputs coming from the image are transformed with a transformation operator.
    -Consider a small image.
    -Assume that we also have the network parameters to be learned.
    -The network parameters to be learned are used as a filter.
    -Each filter learns a small area.
    -The size of these filters can change from algorithm to algorithm.
    -If you have a 6x6 image, you can have 3x3 filters.
    -But in different types of CNN the sizes of these filters will also change.
    -Comparisons are made on the image with the filter.
    -Thanks to these comparisons the model performs its learning.
    -After this filtering process, a convolution matrix is obtained.
    -For multiple filters, multiple convolution matrices are obtained.
    -In this part of convolution, the borders will have been found.
    -If the image is colored, these filters are applied for each color.
    -Convolution or other operations can be skipped and matrices can be directly connected to the neural network.
    -But in this case all pixels will be included in the neural network.
    -By doing convolution, the pixels entering the neural network are reduced.

    *POOLING
    -Convolution and pooling steps can be repeated as many times as desired.
    -It has types such as max pooling or average pooling.
    -The operators in the pooling section can also change.
    -When pooling is done after convolution, the image is shrunk.
    -Pooling takes the image and highlights its important features.
    -It also ignores the unimportant ones in the same way.
    -This way images are shrunk without losing extreme points and important values.

    FLATTENING
    -It refers to transforming matrices into a 1-dimensional state.
    -This operation is done to connect the incoming input convolution matrix to neural networks.
    -The flattening operation can be done in different ways.
    -For example it can be row-based or column-based.

    For connecting to the neural network and beyond this point, the deep learning section can be referred to.
    Reading the Keras documentation is recommended.
