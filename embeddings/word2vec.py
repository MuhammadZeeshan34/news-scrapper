from gensim.models import Word2Vec






class word2vec_wrapper():
    """
    This class computes embeddings for any given corpus using word2vec by Tomas Mikolov -> "https://arxiv.org/abs/1301.3781"
    Word2vec is a 2 layered neral network which takes text corpus as input and returns a set of vector which can be considered as feature vectors.
    It allows to map different entities in given corpus in dimensional subspace which helps in investigating and exploring various relationships among entities i.e entity similarity
    """

    def __init__(self, sequences, learning_rate = 0.02, context_window_size = 5, reduced_dimension_size = 100):
        if len(sequences) < 5:
            ValueError("No corpus given for training")

        self.sentences = sequences
        self.alpha = learning_rate
        self.window = context_window_size
        self.size = reduced_dimension_size
        self.model =  None


    def transform(self, epochs):
        self.model = Word2Vec(sentences=self.sentences, size=self.size, alpha=self.alpha,
                              window=self.window)


    def similarity(self, entity1, entity2):
        self.model.similarity(entity1,entity2)



