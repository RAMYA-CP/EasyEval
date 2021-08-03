# easy-eval
A python script that evaluates an answer sheet with subjective type questions, the input being marking scheme with answer keys along with the answer script.  
It uses azure computer vision rest API to covert handwritten text to typed text. Keyword extraction(IBM NLU) and similarity measures(spacy) are used to evaluate and calculate the score.
