import json
from typing import Dict, Iterable

from allennlp.data import DatasetReader, Instance
from allennlp.data.fields import LabelField, TextField
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.tokenizers import Tokenizer, SpacyTokenizer


@DatasetReader.register("yelp-review-jsonl")
class YelpReviewJsonLinesReader(DatasetReader):
    def __init__(
        self,
        tokenizer: Tokenizer = None,
        token_indexers: Dict[str, TokenIndexer] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.tokenizer = tokenizer or SpacyTokenizer()
        self.token_indexers = token_indexers or {"tokens": SingleIdTokenIndexer()}

    def text_to_instance(self, text: str, label: int) -> Instance:
        """
        Args:
            text: a string value with the text of the Yelp review.
            label: an int value from 0 to 4 (inclusive) which corresponds to the review's star rating

        Returns:
            An allennlp.data.Instance with the fields "text" and "label".
            "text" is a TextField, and "label" is a "LabelField" where the original value of "label"
            has been increased by one and turned into a string.
        """
        # The text of the yelp review.
        # Note we need to replace the escaped newline characters and double quotes.
        text = text.replace("\\n", "\n")
        text = text.replace('\\"', '"')
        # Use the supplied tokenizer to turn the text into tokens
        tokens = self.tokenizer.tokenize(text)
        # The rating--these are numbers 0 through 4, make them strings "1" to "5"
        label = str(1 + label)
        fields = {
            "text": TextField(tokens, self.token_indexers),
            "label": LabelField(label),
        }
        return Instance(fields)

    def _read(self, file_path: str) -> Iterable[Instance]:
        with open(file_path, "r") as lines:
            for line in lines:
                if line != "":
                    data = json.loads(line)
                    yield self.text_to_instance(data["text"], data["label"])
