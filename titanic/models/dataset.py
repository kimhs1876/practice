from dataclasses import dataclass


@dataclass
class Dataset(object):

    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> object: return self._label

    @label.setter
<<<<<<< HEAD
    def label(self, label): self._label = label
=======
    def label(self, label): self._label = label
>>>>>>> 5e545e8e553b5ed92d7980e1a9b68ccd017a4674
