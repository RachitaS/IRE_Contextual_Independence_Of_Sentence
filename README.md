
Derived a method to measure the Contextual Independence of a sentence.




Application:

The contextually independent sentences can be used as a general sentence in a different document as they are independent of the context. Also, it is useful creating a sub-document of a large document such a summarization, key points report etc.




Objective:

To create a model for identifying the best possible sequence of Contextual Independent(CI) and Contextually Dependent(CD) sentences in a test document.




Description:

A sentence is produced to complete a local discourse and a document can be viewed as a sequence of local discourse units than sentences. Each local discourse unit is a sequence of Contextually independent(CI) sentence followed by contextually dependent(CD) sentences. eg: Scientists A and B discovered twin stars near the black hole in Andromeda galaxy. Also the life span of the black hole is determined by these scientists. An annotated dataset of around 100 documents in which each sentence is annotated as CI/CD will be given.Students has to use a sequence labeling scheme and create a model for identifying the best possible sequence of CI and CD sentences in a test document. The probability of each sentence ton CI can be a measure to represents it's contextual independence.Local Discourse Unit can be utilized as a better linguistic unit with more topic information than a sentence as far as automated text summarization is concerned. Contextual independence of a sentence can play a vital role in deciding it's
generality.
